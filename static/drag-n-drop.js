document.addEventListener("DOMContentLoaded", function (e) {
  const spreadsheetSelection = document.querySelector("#spreadsheet-selection");
  function dragOverHandler(e) {
    e.preventDefault();
    e.stopPropagation();
  }
// Drop handler function
  async function dropHandler(e, spreadsheetSelection) {
    e.preventDefault();
    const files = [];
    let dataTransferObj = new DataTransfer;
    const dataTransfer = e.dataTransfer.items;

    for (let i = 0; i < dataTransfer.length; i++) {
      const item = dataTransfer[i].webkitGetAsEntry();
      if (item) {
        await getFileTree(item, files);
      }
    }
// Function for handling converting file into file object that is needed,
// if it's a directory it runs a reader and then pulls the file on the same level.
    async function getFileTree(item, files, path = '') {
      if (item.isFile) {
        const file = await new Promise((resolve) => item.file(resolve));
        file.path = path + item.name; // Add the path to the file object
        dataTransferObj.items.add(file);

      } else if (item.isDirectory) {
        const dirReader = item.createReader();
        const entries = await new Promise((resolve) => dirReader.readEntries(resolve));
        for (let i = 0; i < entries.length; i++) {
          await getFileTree(entries[i], files, path + item.name + '/');
        }
      }
    }
    // Now 'files' array contains standard JavaScript file objects.
    spreadsheetSelection.files = dataTransferObj.files
    handleFileUpload(spreadsheetSelection)
  };

  // File Drag and Drop Listener
  const dragndropArea = document.querySelector('.drop-zone');
  dragndropArea.addEventListener('dragover', dragOverHandler);
  dragndropArea.addEventListener('drop', function (e) {
    dropHandler(e, spreadsheetSelection);
  });
});

