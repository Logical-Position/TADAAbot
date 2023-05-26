# Code Reviews

* Discuss what piece of the application to review
* Determine what files (or functions) and in what order to read through

When Reading the Code:
* Question the code's function
* Question the code styling
* Leave notes for developments regarding edits or refactoring

## May 26th Notes

### Files to review:

main.py

templates/
	base.html
	index.html

static/
	script.js
	style.css

### Walkthrough:

1. Someone requests `tadaa.lp-tools.com/`
2. Request hits the `/` route of Flask route (main.py)
3. Flask generates HTML document from templates
4. Flask sends HTML document over to user; user recieves it in browser
5. User clicks upload input
6. User selects something to upload
7. Frontend verifys upload
8. User enters manual if applicable and clicks "Generate PPT" button
9. Frontend sends form data to Flask server, and prevents default action on client side
10. Flask recieves form data and makes request for TADAA to generate PPT
11. TADAA finishes PPT and Flask sends response to client

---

12. User clicks "Download Audit PPT" button

### Notes:

metalbuildingsales_com_all_exports
www_elegancelamps_com_all_exports

*_all_exports

www_elegancelamps_com_all_exports

STRIP _all_exports

GIVE www_elegancelamps_com

REPLACE _ WITH .

www.elegancelamps.com