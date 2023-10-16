document.addEventListener("DOMContentLoaded", function (e) {
  const spreadsheetSelection = document.querySelector("#spreadsheet-selection");

  function dragOverHandler(e) {
    console.log('Files over drop area');
    e.preventDefault();
    e.stopPropagation();
  }

  //  progress made here
  //https://developer.mozilla.org/en-US/docs/Web/API/DataTransferItem/webkitGetAsEntry
  // SO: https://stackoverflow.com/questions/44842247/event-datatransfer-files-vs-event-datatransfer-items

  async function dropHandler(e, spreadsheetSelection) {
    console.log('File Dropped');
    e.preventDefault();

    const files = [];
    let dataTransferObj = new DataTransfer;
    const dataTransfer = e.dataTransfer.items;

    // console.dir(await dataTransfer[0].getAsFileSystemHandle());

    for (let i = 0; i < dataTransfer.length; i++) {
      const item = dataTransfer[i].webkitGetAsEntry();
      if (item) {
        await getFileTree(item, files);
      }
    }

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

