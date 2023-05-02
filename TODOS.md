# TADAAbot TODOs

## Server-side
* Save final ppt to a dynamically (uniquely) named file
* Fix scope issue with Google APIs
* Connect Google Firestore Database
* Connect Google Cloud Storage
* Migrate Google Cloud Console project to lpseodeveloper@gmail.com account
* Resolve Flask Dance issues
* ~~Save files to desired file structure (/uploads/<domain-name>/)~~
    * ~~Use of `secure_filename` can be dropped while in development~~
* ~~Better understand Flask filepaths~~

## Client-side
* Add a "tadaa!" animation once a file is uploaded
* Discuss end vision of UI
* Change download filename from `empty.pptx` to sent filename
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
* ~~Integrate tailwind.css~~
* ~~Create list of routes / pages / views needed~~
* ~~Adjust /results view to be single-column~~
* ~~Create inputs for all manual data:~~
	* ~~CMS - possibly optional, just for internal data.~~
	* ~~SC access - bool that adjusts Yes/No image~~
	* ~~GA access - bool that adjusts Yes/No image~~
	* ~~Num of Mobile Usability Issues - Adjusts integer and text~~
	* ~~Is Sitemap Submitted in SC - bool that adjusts Yes/No image~~
	* ~~Sitemap URL - string to add to end of sitemap slide~~
	* ~~Robots URL - string to add to end of robots slide~~
	* ~~Structured Data - a multiple choice drop down for the options in slide notes*~~
	* ~~Site Content/UX - a multiple choice drop down for the options in slide notes*~~
	* ~~Internal/External Dup Content - a multiple choice drop down for the options in slide notes*~~
	* ~~Calls to Action - a multiple choice drop down for the options in slide notes*~~
	* ~~Blog - a multiple choice drop down for the options in slide notes*~~
	* ~~Canonicals - a multiple choice drop down for the options in slide notes*~~
	* ~~Website Security - a multiple choice drop down for the options in slide notes*~~
	* ~~Mob/Desk Page Speed - two floats for mob/desktop page speed~~
	* ~~Num of Broken Backlinks - Adjusts integer and text~~
	* ~~Reformat Home page/create Login page template.~~

## Documents
* Think of place for PPT template
	- `static/assets` is for frontend files, so that doesn't work
* ~~Sort done TODOS to the bottom~~
	- ~~Maybe make a script to do this~~
* ~~Reformat README into:~~
	- ~~Overview~~
	- ~~Resources~~
	- ~~Local Installation~~
	- ~~Move Contributors to a new file~~
* ~~Create a `docs` folder~~
	- ~~Move diagrams and Excalidraw files~~

## Production
### Front End
* Remove navigation links from header
* Make 'Generate PPT' button the "end of the road"
	* PPT should automatically download once finished
	* Remove 'Download Audit Powerpoint' button from UI
* Add feedback to file upload input
	* Above the input, add text saying what folder to upload
	* Below, display text describing the files currently uploaded
	* Create an image representation of the folder and files
	* Add outline / shadow / something to describe the state (e.g. red and green)

### Back End
* Connect Firebase and Storage
* Connect Search Console API
 
