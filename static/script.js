document.addEventListener("DOMContentLoaded", function() {
    let tadaaForm = document.querySelector('form#tadaa-form');
    tadaaForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(tadaaForm);
        // set cursor to show progress
        document.body.style.cursor = 'progress';
        updatePptButton("Generating PPT...");

        // logs what is being sent on the form.
        // for(let pair of formData.entries()) {
        //     console.log(pair[0]+ ', '+ pair[1]); 
        // }

        fetch('/', {
            method: 'POST',
            body: formData,
        }).then(function(res) {
            // Do something with the response
            return res.json();
        }).then((data) => {
            // console.log(data);
            const ts = data['ts'];
            // TODO: This still isn't great; the server and client should 
            //      coordinate the exact file to be downloaded. This is still
            //      just educated guessing.
            const client = data['client_name'];
            const pptName = `${client}-${ts}.pptx`
            requestDownload(ts, pptName);

            const auditsId = data['audits_id'];
            updateRawDataLink(auditsId);

        }).finally(() => {
            document.body.style.cursor = 'auto';
            updatePptButton("Downloaded PPT");
        });
    });

    function requestDownload(ts, filename) {
        let downloadURL = `/download/${ts}`;
        makeRequest(downloadURL, (res) => {
            // https://stackoverflow.com/questions/22724070/prompt-file-download-with-xmlhttprequest
            // https://stackoverflow.com/questions/29192301/how-to-download-a-file-via-url-then-get-its-name
            // let contentDispo = e.currentTarget.getResponseHeader('Content-Disposition');
            // let filename = contentDispo.match(/filename[^;=\n]*=((['"]).*?\2|[^;\n]*)/)[1];
            saveBlob(res, filename);
        });
    }

    // Handles enabling/disabling the submit buttons and very basic verification.
    let fileUploadContainer = document.querySelector("#spreadsheet-selection");
    let generateButton = document.querySelector('input[name="generate_ppt"]');
    fileUploadContainer.addEventListener('change', function(event) {
        if (fileUploadContainer.value != "") {
            let parentFolder = fileUploadContainer.files[0].webkitRelativePath.split("/")[0];
            if (parentFolder == "exports") {
                generateButton.disabled = false;
            }
            else {
                window.alert("Uploaded folder is not named 'exports'.");
                generateButton.disabled = true;
            }
        }
    });

    const blogCheckElem = document.querySelectorAll("input[name='blog']");
    // Apply listener to blog options listening for change
    
    blogCheckElem.forEach((item) => {
        item.addEventListener("change", function(e) {
            // Secondary options become available once yes is checked, might be a cleaner way to do this later.
        const secondaryBlogOptions = document.querySelectorAll("input[name='blog_updated_regularly']");

            if(blogCheckElem[0].checked) {
            secondaryBlogOptions.forEach(item => item.disabled = false);
            }
            else if (!blogCheckElem[0].checked) {
            secondaryBlogOptions.forEach(item => item.disabled = true);
            }
        });
        
    });

    const duplicateContentCheck = document.querySelectorAll("input[name='duplicate_content']");

    duplicateContentCheck.forEach((item) => {
        item.addEventListener("change", function(e) {
            const duplicateTextBox = document.querySelector("#duplicate_text");
            if(duplicateContentCheck[0].checked) {
                duplicateTextBox.disabled = false;
            }
            else if(!duplicateContentCheck[0].checked) {
                duplicateTextBox.disabled = true;
            }
        });
    });

    // MARK: File Upload Listener
    fileUploadContainer.addEventListener('change', handleFileUpload);

    const uploadedFile = document.querySelector("#uploaded-file-name");
    const fileImage = document.getElementById("file-upload-image");
    const folderName = document.getElementById("folder-name");
    const exportsWarning = document.getElementById("exports-only-warning");

    function handleFileUpload() {
        // 1. Verifying folder is exports folder and there are more than 0 files.
        // 2. Uploaded file text is updated to "File Name"
        // 3. Outline the file uploader in green.
        // 4. Update the file uploader to display a placeholder folder image along with the file name/number of files/ display text "uploaded Folder is not exports".
        
        // FIXME: Errors if this runs when no files are uploaded.
        // Upon cancel click, filename returns undefined.
        // Check has to be done to see if fileUploadContainer.files exists first.  
        if(fileUploadContainer.files.length > 0) {
            //sucessfulFormReset works so long as the files change.
            sucessfulFormReset();
            let filename = fileUploadContainer.files[0].name;
            let folderName = fileUploadContainer.files[0].webkitRelativePath.split("/")[0];
        
            let folderIsUploaded = fileUploadContainer.value != "";
            let folderIsExports = folderName === "exports";

            let isUploadValid = folderIsUploaded && folderIsExports;
                if (isUploadValid) {
                    filename = filename.split("_")[0];
                    filename = filename.charAt(0).toUpperCase() + filename.slice(1);
                    updateUploadedFileLabel(filename);
                    outlineFileInput();
                    updateFileInputImage(filename);
                }
                else {
                    alert("Uploaded folder is not named exports.")
                }
        }   
        else if (!fileUploadContainer.files.length > 0 ) {
            cancelForm()
        }
            
    }

    function sucessfulFormReset() {
        // Reset form on sucessful PPT upload/download.
        updatePptButton("Generate PPT");
        const rawDataLink = document.getElementById("raw-data-link");
        rawDataLink.classList.add("disabled-raw-data-link");
        rawDataLink.href="#";
    }

    function cancelForm() {
        let uploadFileContainer = document.querySelector("#upload-file-container");
        updatePptButton("Generate PPT");
        fileImage.src = "static/assets/upload-placeholder.svg";
        folderName.innerText = "Click to Upload";
        folderName.className = "mb-2 text-sm text-neutral-500";
        exportsWarning.style.display = "block";
        uploadedFile.innerText = "";
        uploadFileContainer.classList.remove("completed-indicator");
        generateButton.disabled = true;
    }

    // let folderName = "";
    // Function for handling updating "Uploaded File" text once file has been uploaded.
    function updateUploadedFileLabel(filename) {
        uploadedFile.innerText = filename;
        folderName.innerText = filename;       
    }

    // Function for handling updating the border color of the upload file container when a valid file is uploaded.
    function outlineFileInput() {
        let uploadFileContainer = document.querySelector("#upload-file-container");
        uploadFileContainer.classList.add("completed-indicator");
    }

    // Function for removing file upload image/text and replacing it with placeholder folder image and folder name
    function updateFileInputImage(filename) {
        // Select Elements to be edited on each upload
        let placeholderFolderImage = document.querySelector("#file-upload-image");
        placeholderFolderImage.src = "static/assets/folder-upload-overwrite.svg";

        // Create folder name element
        folderName.innerText = filename;

        // Remove previous classes and add appropriate ones for when file is uploaded.
        folderName.className = "text-xl font-semibold pt-4";

        let exportsWarning = document.querySelector("#exports-only-warning");
        exportsWarning.style.display = "none";
    }
});

function makeRequest(path, callback) {
    let req = new XMLHttpRequest();
    req.responseType = 'blob';
    req.onload = function(e) {
        let blob = e.target.response;
        callback(blob);
    };

    req.open("GET", path, true);
    req.send();
}

function saveBlob(blob, filename) {
    // let assetRecord = this.getAssetRecord();
    // console.log(filename);
    let tempEl = document.createElement("a");
    document.body.appendChild(tempEl);
    tempEl.style = "display: none";
    let url = window.URL.createObjectURL(blob);
    tempEl.href = url;
    tempEl.download = filename;
    tempEl.click();
    window.URL.revokeObjectURL(url);
}

function updatePptButton (text) {
    const pptButton = document.querySelector("#submit-input");
    pptButton.value = text;
};

function updateRawDataLink(id) {
    const elId = "raw-data-link";
    const disabledClass = "disabled-raw-data-link";
    const anchor = document.getElementById(elId);
    if (anchor) {
        anchor.href = `/db/${id}`;
        anchor.classList.remove(disabledClass);
    }
}
