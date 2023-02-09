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
            console.log('hello');
            console.log(response.json());
            console.log(response);
        }).finally(() => {
            document.body.style.cursor = 'auto';
            enableDownload();
        });
    });

    let downloadButton = document.querySelector('button#ppt-download-button');
    downloadButton.addEventListener('click', (e) => {
        if (downloadButton.disabled) return;
        requestDownload();
    })
    function enableDownload() {
        downloadButton.disabled = false;
    }

    function requestDownload() {
        let downloadURL = '/download'
        makeRequest(downloadURL, (res) => {
            console.log("Request callback");
        });
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
    let fileName = 'empty.pptx'
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

