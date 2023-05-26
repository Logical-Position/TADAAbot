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
        document.body.style.cursor = 'progress';

        fetch('/', {
            method: 'POST',
            body: formData,
        }).then(function(response) {
            // Do something with the response
            console.log("POST response here");
            
        }).finally((res) => {
            document.body.style.cursor = 'auto';
            enableDownload();
            console.log(res);
        });
    });

    let downloadButton = document.querySelector('button#ppt-download-button');
    // let authButton = document.querySelector('button#auth-dance-button');
    downloadButton.addEventListener('click', (e) => {
        if (downloadButton.disabled) return;
        requestDownload();
    })
    // authButton.addEventListener('click', (e) => {
    //     if (authButton.disabled) return;
    //     authDance();
    // })
    function enableDownload() {
        downloadButton.disabled = false;
        // authButton.disabled = false;
    }

    function requestDownload() {
        let downloadURL = '/download';
        makeRequest(downloadURL, (res) => {
            console.log("Request callback");
        });
    }

    function authDance() {
        console.log('Starting Auth Dance.')
        window.location.href = "/auth";
        // let authURL = '/auth'
        // let req = new XMLHttpRequest();

        // req.open("GET", authURL, true)
        // req.send()
    }

    // Handles enabling/disabling the submit buttons and very basic verification.
    let __renameThis = document.querySelector("#spreadsheet-selection");
    let generateButton = document.querySelector('input[name="generate_ppt"]');
    __renameThis.addEventListener('change', function(event) {
        if (__renameThis.value != "") {
            let parentFolder = __renameThis.files[0].webkitRelativePath.split("/")[0];
            if (parentFolder == "exports") {
                generateButton.disabled = false;
            }
            else {
                window.alert("Uploaded folder is not named 'exports'.");
                generateButton.disabled = true;
            }
        }
    });

    // MARK: File Upload Listener
    const spreadsheetSelection = document.querySelector("#spreadsheet-selection");
    spreadsheetSelection.addEventListener('change', handleFileUpload);

    function handleFileUpload() {
        // 1. Verify folder has more than 0 files, and is named `exports`.
        // 2. Uploaded file text is updated to "File Name"
        // 3. Outline the file uploader in green.
        // 4. Update the file uploader to display a placeholder folder image 
        //      along with the file name/number of files/ display text 
        //      "uploaded Folder is not exports".
        // 5. Enable "Generate PPT button"
        let filename = spreadsheetSelection.files[0].name;
        let folderName = spreadsheetSelection.files[0].webkitRelativePath.split("/")[0];
        
        let folderIsUploaded = spreadsheetSelection.value !== "";
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

    // Function for handling updating "Uploaded File" text once file has been uploaded.
    function updateUploadedFileLabel(filename) {
        const uploadedFile = document.querySelector("#uploaded-file-name");
        uploadedFile.innerText = filename + " exports folder";
    }

    // Function for handling updating the border color of the upload file container when a valid file is uploaded.
    function outlineFileInput() {
        let uploadFileContainer = document.querySelector("#upload-file-container");
        uploadFileContainer.style.borderColor = "green";
        uploadFileContainer.classList.add("completed-indicator");
    }

    // Function for removing file upload image/text and replacing it with placeholder folder image and folder name
    // FIXME: Folder name does not update when uploaded folder is replaced
    // FIXME: Potential issue with image sizing -- sometimes is extra large
    function updateFileInputImage(filename) {
        const uploadedFile = document.querySelector("#uploaded-file-name");

        // Remove excess text/upload image from file uploader once a file is uploaded
        let fileContainerContent = document.querySelector("#droparea")
        fileContainerContent.remove();
        
        // Create placeholder folder image element
        let placeholderFolderImage = document.createElement("img");
        placeholderFolderImage.src = "static/assets/folder-upload-overwrite.svg";

        // Create folder name element
        let folderName = document.createElement("span");
        folderName.innerText = filename;
        folderName.classList.add("text-xl", "font-semibold", "pt-4")
        
        // Create container for the placeholder folder image and folder name
        let placeholderContainer = document.createElement("div");
        placeholderContainer.classList.add("flex", "flex-col","justify-center",);
        placeholderContainer.appendChild(placeholderFolderImage);
        placeholderContainer.appendChild(folderName);
        
        // Add the placeholder container to the file uploader
        let uploadFileContainer = document.querySelector("#upload-file-container");
        uploadFileContainer.appendChild(placeholderContainer);
    }  

});


function makeRequest(path, callback) {
    let req = new XMLHttpRequest();
    req.responseType = 'blob';
    req.onload = function(e) {
        // https://stackoverflow.com/questions/22724070/prompt-file-download-with-xmlhttprequest
        let blob = e.target.response;
        let contentDispo = e.currentTarget.getResponseHeader('Content-Disposition');
        console.log(e.currentTarget);
        console.log(contentDispo);
        console.log(blob);
        saveBlob(blob);
        //callback(e);
    };

    req.open("GET", path, true);
    req.send();
}

function saveBlob(blob) {
    // let assetRecord = this.getAssetRecord();
    let fileName = 'pop_ppt.pptx';
    let tempEl = document.createElement("a");
    document.body.appendChild(tempEl);
    tempEl.style = "display: none";
    let url = window.URL.createObjectURL(blob);
    tempEl.href = url;
    tempEl.download = fileName;
    tempEl.click();
    window.URL.revokeObjectURL(url);
}

// function doSomething(event) {
//     event.preventDefault();
//     makeRequest("/", (req) => {
//         alert(req.responseText);
//     });
// }

// function runAudit(event) {
//     event.preventDefault();
//     makeRequest("/audit", (req) => {
//         alert(req.responseText);
//     });
// }