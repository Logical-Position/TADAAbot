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
* Normalize <main> container (or a child <div> container) across site
* Adjust padding at top of FAQ page
* Remove horizontal scroll on FAQ page
* Add arrows to results tabs to indicate interaction
* Format arrows across the site to match FAQ page arrows
* Move "Start Auth Dance" button from Home to page to Extras page
* Add disabled state to "Download Audit PPT" button on Home page
* Fix bug with manual input radio buttons preventing all questions from being answered
	* The problem was too much copy paste -- the solution lies in the "names" of the inputs.
	* Read here for another hint: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/radio#defining_a_radio_group
* Remove id duplication from manual input fields
	* We don't want two different radio buttons to have the id="yes"; we can differentiate this with more specific id's, like id="sc-access-yes" and id="sc-access-no".
	* IDs are meant to be global identifiers: https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id

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
