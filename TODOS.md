# TADAAbot TODOs

* [ ] Launch date scheduled for June 6th!
	* [ ] Schedule meeting with Tursi.

## General
* [ ] Remove unused comments and code
* [ ] Remove `console.log` and `print` statements
* [ ] Upload test data to repo
* [ ] Make `prod` default branch once `0.0` is pushed
	* [ ] Delete `main` branch

## Server-side
* [ ] Implement database API
* [ ] Migrate Railway project to lpseodeveloper@gmail.com
* [X] Migrate Google Cloud Console project to lpseodeveloper@gmail.com account
	* [X] Ensure there's nothing left in personal account

## Client-side
* [X] Make 'Generate PPT' button the "end of the road"
	* [X] PPT should automatically download once finished
	* [X] Remove 'Download Audit Powerpoint' button from UI
* [ ] Change ppt filename to same as sent over server

### Manual Input Fixes

* [ ] Change Robot (#8) manual inputs to multiple radio options.
* [x] Change Calls to Action (#12) to yes/no radio.
* [x] Change Blog (#13) to Yes/No radio
	* [ ] If yes, another yes/no radio for if it's updated regularly
* [x] Change Duplicate Content (#11) to Yes/No radio
	* [ ] If yes, give field to explain where the duplicate content is mostly located.

* [x] Remove navigation links from header
* [x] Add feedback to file upload input
	* [x] Above the input, add text saying what folder to upload
	* [x] Below, display text describing the files currently uploaded
	* [x] Create an image representation of the folder and files
	* [x] Add outline / shadow / something to describe the state (e.g. red and green)
* [x] Remove id duplication from manual input fields
	* The problem was too much copy paste -- the solution lies in the "names" of the inputs.
	* Read here for another hint: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/radio#defining_a_radio_group
	* We don't want two different radio buttons to have the id="yes"; we can differentiate this with more specific id's, like id="sc-access-yes" and id="sc-access-no".
	* IDs are meant to be global identifiers: https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id

