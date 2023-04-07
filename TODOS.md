# TADAAbot TODOs

## Server-side
* ~~Save files to desired file structure (/uploads/<domain-name>/)~~
    * ~~Use of `secure_filename` can be dropped while in development~~
* Save final ppt to a dynamically (uniquely) named file
* ~~Better understand Flask filepaths~~
* Fix scope issue with Google APIs
* Connect Google Firestore Database
* Connect Google Cloud Storage
* Migrate Google Cloud Console project to lpseodeveloper@gmail.com account
* Resolve Flask Dance issues

## Client-side
* Discuss end vision of UI
* ~~Integrate tailwind.css~~
* ~~Create list of routes / pages / views needed~~
* ~~Adjust /results view to be single-column~~
* ~~Create inputs for all manual data; see "Data Requiring Manual Input" section in [README.md](/README.md#data-requiring-manual-input)~~
* Change download filename from `empty.pptx` to sent filename
* ~~Reformat Home page/create Login page template.~~
* Dark Mode/Light Mode Toggles
* Profile/Logout Buttons
* Enable drag and drop folder upload
* Remove header from login view by restructuring template files per [the hierarchy diagram](/tadaa_template-hierarchy.png)
* Finish building out the Results view
* Create drop down / select lists for manual data with multiple options

## Documents
* Sort done TODOS to the bottom
	- Maybe make a script to do this
* Reformat README into:
	- Overview
	- Resources
	- Local Installation
	- Move Contributors to a new file
* Create a `docs` folder
	- Move TODOS into it
	- Move CONTRIBUTORS
	- Move diagrams and Excalidraw files
* Think of place for PPT template
	- `static/assets` is for frontend files, so that doesn't work
