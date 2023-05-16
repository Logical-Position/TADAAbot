# TADAAbot TODOs

* [ ] Launch date scheduled for June 6th!

## General
* [ ] Remove unused comments and code

## Server-side
* [ ] Connect Search Console API
	* [ ] Fix scope issue with Google APIs
* [ ] Connect Google Firestore Database
* [ ] Connect Google Cloud Storage
* [ ] Migrate Google Cloud Console project to lpseodeveloper@gmail.com account
	* [ ] Ensure there's nothing left in personal account
* [ ] Resolve Flask Dance issues

## Client-side
* [x] Remove navigation links from header
* [ ] Make 'Generate PPT' button the "end of the road"
	* [ ] PPT should automatically download once finished
	* [ ] Remove 'Download Audit Powerpoint' button from UI
* [x] Add feedback to file upload input
	* [x] Above the input, add text saying what folder to upload
	* [x] Below, display text describing the files currently uploaded
	* [x] Create an image representation of the folder and files
	* [x] Add outline / shadow / something to describe the state (e.g. red and green)
* [ ] Change ppt filename to same as sent over server
* [x] Remove id duplication from manual input fields
	* The problem was too much copy paste -- the solution lies in the "names" of the inputs.
	* Read here for another hint: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/radio#defining_a_radio_group
	* We don't want two different radio buttons to have the id="yes"; we can differentiate this with more specific id's, like id="sc-access-yes" and id="sc-access-no".
	* IDs are meant to be global identifiers: https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id

