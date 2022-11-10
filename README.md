# T.A.D.A.A bot

 ### A Technical Audit Documentation Automation Assistant
 
An automation assistant for tech audits! Tadaa!!

## Here's what it does. (TADAAbot)
1. Prompts for the location of the Sitebulb exports folder and the domain of the target site. 
2. Detects export files in the hints folder that are used in the tech audit.
3. Creates a new master Excel file in the Sitebulb exports folder.
4. Makes API requests to our favorite SEO tools (Moz, AHREFS, SEMRUSH, Search Console, Siteliner, etc.) for data needed in tech audit.
5. Scrapes homepage for any existing Google Analytics and Search Console tags (how much crawling should be done?)
6. Checks for existence and contents of robots.txt and sitemap.
7. Calculates totals for various tech audit metrics (broken links, images missing alt text, ect.)
8. Consolidates all data into the master file.
9. Organizes master spreadsheet by creating a main overview sub-sheet, as well as a sub-sheet for each export file and its data.
10. Populates tech audit PowerPoint slides with data, using PowerPoint's placeholder text feature. (File explorer select for ppt template?)
11. Adjusts SEO recommendation template based on data for each slide.
12. Displays real-time completion status messages in main window during operation. 


## Here's what you do. (The Analyst)
1. Get an impression of the target site; click around, read some words, search for noindex tags, swap your device view. How does it all make you feel?
2. Open/Install? the TADAA.exe from your download? (Figure out how to package? mac/windows/linux?)
3. Paste the target domain in its text field.
4. Click the 'Select Sitebulb Exports Folder' button (must extract from ZIP).
5. Navigate to the extracted Sitebulb exports folder.
6. Begin the automation process by clicking the 'Begin Automation' button.
7. Ponder the absurd nature of reality (And SEO) for a number of seconds.
8. Input credentials for corresponding SEO service when prompted.
9. Verify successful operation by checking status messages in main window.
10. Get top-level breakdown in overview tab of master Excel file created during the operation.
11. Dig deeper in each individual sub-sheet to better understand the issues and their severity.
12. Inspect the live site for examples of any detected issues, and search for noindex tags on all types of pages (homepage, collections, categories, products, blogs, etc.)
13. Consult your favorite SEO tool (Sitebulb/Screaming Frog, GA/SC, SEMRUSH, etc.) or the raw Sitebulb exports to analyze more data.
14. Deliver your judgements and prioritize solutions based on issue severity.


#### BONUS
- Seek out and analyze competitor sites, if applicable to project and/or client.
- Analyze historical dips or rises in traffic, keywords, or another metric to see if any reasonable connections might be made to any discovered technical issues.
- Search for noindex tags!


### Python Libraries Used
- PySimpleGUI - for the graphical user interface.
- python-pptx - for PowerPoint shenanigans.
- openpyxl - for Excel shenanigans.
- csv - for.. csv shenanigans.
- Beautifulsoup - for html parsing and web scraping.
- requests - for making API requests.
- os - for file management.
- tkinter - for file explorer dialogue.
- Pyinstaller - for packaging the project and creating an .exe.