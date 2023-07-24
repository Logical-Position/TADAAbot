document.addEventListener("DOMContentLoaded", function() {
    // let button = document.querySelector('button#something-button');
    // button.addEventListener("click", (e) => {
    //     doSomething(e);
    // });

    // let auditButton = document.querySelector('button#audit-button');
    // auditButton.addEventListener("click", (e) => {
    //     runAudit(e);
    // });


    let tadaaForm = document.querySelector('form#tadaa-form');
    tadaaForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(tadaaForm);
        // set cursor to show progress
        // progess bar goes through stages of completion
        document.body.style.cursor = 'progress';
        updatePptButton("Generating PPT...");
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

            
        }).then(function(response) {
            // Do something with the response  
        }).finally(() => {
            document.body.style.cursor = 'auto';
            
            updatePptButton("Downloaded PPT");
            // requestDownload(); not sure why its on here twice
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
    let test = document.querySelector("#spreadsheet-selection");
    let generateButton = document.querySelector('input[name="generate_ppt"]');
    test.addEventListener('change', function(event) {
        if (test.value != "") {
            let parentFolder = test.files[0].webkitRelativePath.split("/")[0];
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
    const spreadsheetSelection = document.querySelector("#spreadsheet-selection");
    spreadsheetSelection.addEventListener('change', handleFileUpload);

    function handleFileUpload() {
        // 1. Verifying folder is exports folder and there are more than 0 files.
        // 2. Uploaded file text is updated to "File Name"
        // 3. Outline the file uploader in green.
        // 4. Update the file uploader to display a placeholder folder image 
        //      along with the file name/number of files/ display text 
        //      "uploaded Folder is not exports".
        // 5. Enable "Generate PPT button"

        // Reset progress bar 
        // handleProgressBar("0");
        
        // FIXME: Errors if this runs when no files are uploaded.
        let filename = spreadsheetSelection.files[0].name;
        let folderName = spreadsheetSelection.files[0].webkitRelativePath.split("/")[0];
        
        let folderIsUploaded = spreadsheetSelection.value != "";
        let folderIsExports = folderName === "exports";

        let isUploadValid = folderIsUploaded && folderIsExports;
        if (isUploadValid) {
            // console.log(spreadsheetSelection.files.length)
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

    let folderName = "";
    // Function for handling updating "Uploaded File" text once file has been uploaded.
    function updateUploadedFileLabel(filename) {
        const uploadedFile = document.querySelector("#uploaded-file-name");
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
        const uploadedFile = document.querySelector("#uploaded-file-name");
        
        // Remove excess text/upload image from file uploader once a file is uploaded
        // The issue is when you .remove() the element #droparea, you no longer have this element on the DOM for future reference.
        // Temp fix: loop #droparea to check and see if it has children until it has none, then proceed.
        let fileContainerContent = document.querySelector("#droparea")
        while(fileContainerContent.firstChild) {
            fileContainerContent.removeChild(fileContainerContent.firstChild);
        }
        
        // Create placeholder folder image element
        let placeholderFolderImage = document.createElement("img");
        placeholderFolderImage.src = "static/assets/folder-upload-overwrite.svg";
        placeholderFolderImage.classList.add("w-10");

        // Create folder name element
        folderName = document.createElement("span");
        folderName.innerText = filename;
        folderName.classList.add("text-xl", "font-semibold", "pt-4");
        
        // Create container for the placeholder folder image and folder name
        let placeholderContainer = document.createElement("div");
        placeholderContainer.classList.add("flex", "flex-col","items-center");
        placeholderContainer.appendChild(placeholderFolderImage);
        placeholderContainer.appendChild(folderName);
        
        // Add the placeholder container to the file uploader
        fileContainerContent.appendChild(placeholderContainer);
    }
});

function makeRequest(path, callback) {
    let req = new XMLHttpRequest();
    req.responseType = 'blob';
    req.onload = function(e) {
        // https://stackoverflow.com/questions/22724070/prompt-file-download-with-xmlhttprequest
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
