document.addEventListener("DOMContentLoaded", main);

// MARK: UI

/**
 * Components we're modifying:
 * - Generate button
 * - Filename label
 * - Manual inputs toggle
 * - Secondary manual inputs
 * - DB Link
 * - File upload input
 */

function handleFileUpload(spreadsheetSelection) {
    // 1. Verifying folder is exports folder and there are more than 0 files.
    // 2. Uploaded file text is updated to "File Name"
    // 3. Outline the file uploader in green.
    // 4. Update the file uploader to display a placeholder folder image 
    //      along with the file name/number of files/ display text 
    //      "uploaded Folder is not exports".
    // 5. Enable "Generate PPT button"

    // FIXME: Errors if this runs when no files are uploaded.
    let folderName = "";

    // Receiving `spreadsheetSelection from two possible sources
    // determines whether we use webkitRelativePath[click] vs Path[drag-n-drop]
    let path = spreadsheetSelection.files[0].path
    let webKitPath = spreadsheetSelection.files[0].webkitRelativePath

    
    if(webKitPath === "") {
        folderName = path.split("/")[0];
    }
    else if (webKitPath !== null && webKitPath !== undefined) {
        folderName = webKitPath.split("/")[0];
    }
    else {
        folderName = "";
    }

    let filename = spreadsheetSelection.files[0].name;
    let folderIsUploaded = spreadsheetSelection.value != "";
    let folderIsExports = folderName === "exports";

    let isUploadValid = folderIsUploaded && folderIsExports;
    let generateButton = document.querySelector('input[name="generate_ppt"]');

    if (isUploadValid) {
        filename = filename.split("_");

        // Check for ".com" TLD or other common TLD's and get the previous item in array (Temporary solution).
        // Could look into using Public Suffix List package from npm, but not sure how viable it is considering our underscore naming convention.
        // https://www.npmjs.com/package/psl 
        for(let i = 0; i < filename.length; i++) {
            if(filename[i] === "com" || filename[i] === "net" || filename[i] === "org" || filename[i] === "net" || filename[i] === "co" || filename[i] === "us") {
                filename = filename[i - 1] + "." + filename[i];
            }

        }
            filename = filename.charAt(0) + filename.slice(1);
            // updateUploadedFileLabel(filename);
            outlineFileInput();
            updateFileInputImage(filename);

            // update manual inputs field
            let manualDomainInput = document.getElementById("domain_url");
            manualDomainInput.value = filename;  
            generateButton.disabled = false;          
    }
    else {
        alert("Uploaded folder is not named exports.")
        generateButton.disabled = true;
    }
}

function handleDomainNameChange(e) {
    let newName = e.target.value;
    // updateUploadedFileLabel(newName);

    // Check if files have been uploaded before changing the name inside the droparea.
    if(spreadsheetSelection.length > 0) updateFileInputImage(newName);  
}

// Function for handling updating "Uploaded File" text once file has been uploaded.
function updateUploadedFileLabel(filename) {
    // Discussion: It's a good practice to catch your potential errors.
    // Here, we add a try-catch handler so, if an error does happen, the program does not crash and continues executing
    // Without this, the program crashes because the targeted element doesn't exist -- it's commented out
    // Another approach is to check if `uploadedFile` is a valid object before we try to do something with it, like set it's `innerText` property
    // What if we don't want to add this boilerplate to every function that updates a part of the UI? 
    // Is there an abstract helper function(s) that we can make?
    try {
        const uploadedFile = document.querySelector("#uploaded-file-name");
        uploadedFile.innerText = filename;
        uploadedFile.value = filename;
    } catch (e) {
        console.error(e);
        // Discussion: This will only print to the user's local browser console (i.e. on the analyst's computer)
        // What else can we do with an error?
    }
    /**
     * Another approach
    const uploadedFile = document.querySelector("#uploaded-file-name");
    if (uploadedFile !== null || uploadedFile !== undefined) {
        // Do stuff with the element
        uploadedFile.innerText = filename;
        uploadedFile.value = filename;
    } else {
        // Report and handle an error
        console.error("oops! something went wrong!");
    }
    */
}

// Function for handling updating the border color of the upload file container when a valid file is uploaded.
function outlineFileInput() {
    let uploadFileContainer = document.querySelector("#upload-file-container");
    uploadFileContainer.classList.add("completed-indicator");
}

// Function for removing file upload image/text and replacing it with placeholder folder image and folder name
function updateFileInputImage(filename) {    
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

function updatePptButton(text) {
    const pptButton = document.querySelector("#submit-input");
    pptButton.value = text;
};

function handleTadaaSubmission(e, tadaaForm) {
    e.preventDefault();
    const formAction = tadaaForm.getAttribute('action');
    const formData = new FormData(tadaaForm);
    // set cursor to show progress
    // progess bar goes through stages of completion
    document.body.style.cursor = 'progress';
    updatePptButton("Generating PPT...");
    fetch(formAction, {
        method: 'POST',
        body: formData,
    }).then((res) => {
        return res.json();

    }).then((data) => {
        console.log(data);
        requestDownload(data['id']);

    })
    // .then((res) => {

    // })
    .finally(() => {
        document.body.style.cursor = 'auto';
        updatePptButton("Downloaded PPT");
    });
}


// MARK: Networking

/**
 * - Sending audit request to server
 * - Receiving data and PPT file from server
 * - Saving and downloading PPT
 */

function requestDownload(auditId) {
    let downloadURL = `/download/${auditId}`;
    makeRequest(downloadURL, (res, filename) => {
        // https://stackoverflow.com/questions/22724070/prompt-file-download-with-xmlhttprequest
        // https://stackoverflow.com/questions/29192301/how-to-download-a-file-via-url-then-get-its-name
        // let contentDispo = e.currentTarget.getResponseHeader('Content-Disposition');
        // let filename = contentDispo.match(/filename[^;=\n]*=((['"]).*?\2|[^;\n]*)/)[1];
        saveBlob(res, filename);
    });
}

function makeRequest(path, callback) {
    let req = new XMLHttpRequest();
    req.responseType = 'blob';
    req.onload = function(e) {
        // https://stackoverflow.com/questions/22724070/prompt-file-download-with-xmlhttprequest
        let blob = e.target.response;
        // console.log(e);
        let contentDispo = e.currentTarget.getResponseHeader('Content-Disposition');
        console.log(contentDispo)
        let filename = contentDispo.match(/filename[^;=\n]*=((['"]).*?\2|[^;\n]*)/)[1];
        callback(blob, filename);
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

// MARK: Main

function main() {
    // Add event listeners

    // MARK: TADAA Form
    let tadaaForm = document.querySelector('form#tadaa-form');
    tadaaForm.addEventListener('submit', function(e) {
        handleTadaaSubmission(e, tadaaForm);
    });

    // MARK: File Upload Listener
    const spreadsheetSelection = document.querySelector("#spreadsheet-selection");
    spreadsheetSelection.addEventListener('change', function(e) {
        handleFileUpload(spreadsheetSelection);
    });


    // MARK: Domain Input Change
    let domainInput = document.getElementById('domain_url');
    domainInput.addEventListener("input", handleDomainNameChange);
    

    // MARK: Duplicate Content
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

    // MARK: Structured Data
    const structuredDataCorrect = document.querySelector("#correct_structured_data");
    const structuredDataNotCorrect = document.querySelector("#incorrect_structured_data");
    const numStructuredData = document.querySelector("#structured_data_errors");
    
    // try {
    //     structuredDataCorrect.addEventListener("change", function(e) {
    //         if (structuredDataCorrect.checked) {
    //             numStructuredData.disabled = false;
    //         }
    //     });
        
    //     structuredDataNotCorrect.addEventListener("change", function(e) {
    //         if (structuredDataNotCorrect.checked) {
    //             numStructuredData.disabled = true;
    //         }
    //     });
    // } catch (err) {
    //     console.error("Failed to attached listeners to structredData");
    //     console.error(err);
    // }
    
    let confetti = new Confetti('confetti');
    confetti.setCount(25);
    confetti.setSize(2);
    confetti.setPower(42);
    confetti.setFade(true);
    confetti.destroyTarget(false);
}


