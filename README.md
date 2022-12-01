# T.A.D.A.A bot

 ### A Technical Audit Documentation Automation Assistant
 
An automation assistant for tech audits! Tadaa!!

## Here's what it does. (TADAAbot)
1. Prompts for the location of the Sitebulb exports folder and the domain of the target site. 
2. Matches files in the hints folder that are used in the tech audit.
3. Creates a new master Excel file that will contain all data used in the tech audit, and lots more.
4. Makes API requests to Search Console, Siteliner, Pagespeed insights, and other sources of data used in tech audit, and more.
5. Scrapes homepage for any existing Google Analytics tags, Search Console Tags, robots.txt, and sitemap.
6. Checks if the client site is GA/SC verified under a target LP Google account.
7. Calculates totals for various tech audit metrics (broken links, images missing alt text, ect.)
8. Organizes master Excel file with a main overview sheet that contains data totals, as well as a sub-sheet for each export file/api object and all its raw data.
9. Populates all PowerPoint slides with data.
10. Adjusts SEO recommendation text based on data.
11. Displays current status messages during the operation.

## Here's what it can't do. (TADAAbot Limitations)
1. Screenshots.
2. Think critically.
3. Access certain data sources, such as broken backlinks from AHREFs. (for now)
4. Link resources in ppt slides
5. ??


## Here's what you do. (The Analyst)
1. Get an impression of the target site; click around, read the words, search for noindex tags, swap your device view. How does it all make you feel?
2. Go to the TADAAbot web app.
3. Paste the target domain in its text field.
4. Click the 'Select Sitebulb Exports Folder' button.
5. Navigate to the extracted Sitebulb exports folder (must be extracted from ZIP).
6. Begin the automation process by clicking the 'TADAA' button.
7. Ponder the absurd nature of reality (And SEO) for a number of seconds.
8. Input credentials for corresponding SEO service if prompted.
9. Verify successful operation by checking status messages in main window.
10. Get top-level breakdown in Overview tab of master Excel file created during the operation.
11. Dig deeper in each individual sub-sheet to inspect the issues for their severity. Ex: Are the broken links on an unfinished lorem ipsum template page? Did Sitebulb act strangely and pick up something that isn't on the site anymore?
12. Inspect the live site for examples of any detected issues, and search for noindex tags on all types of pages (homepage, collections, categories, products, blogs, etc.)
13. Consult your favorite SEO tool (Sitebulb/Screaming Frog, GA/SC, SEMRUSH, etc.) or the raw Sitebulb exports to analyze more data.


#### BONUS
- Seek out and analyze competitor sites, if applicable to project and/or client.
- Analyze historical dips or rises in traffic, keywords, or another metric to see if any reasonable connections might be made to any discovered technical issues.
- Search for noindex tags!


### Python Libraries Used
- Flask - for creating the web framework.
- python-pptx - for PowerPoint shenanigans.
- openpyxl - for Excel shenanigans.
- csv - for.. csv shenanigans.
- requests - for making API requests.
- os - for file management.

### Possible Future Functionalities
- Utilize a database and store historical TA data. 
- Run comparisons between current audit and historical audit data.
- Data Visualization Templates.
- Get additional API data not used in tech audit from sources like Moz, GA, etc.
- Programmatically access SERPs results using the Custom Search API.

### Possible Future Projects
- Create an 'SEO Analyst Tools' web app dashboard where TADAAbot is only one of the included tools.
- Site Migration Tool
- Competitive Analysis Tool
- Blog Strategy Tool
- 
