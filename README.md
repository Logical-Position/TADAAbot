# T.A.D.A.A bot

 ### A Technical Audit Documentation Automation Assistant
 
An automation assistant for tech audits! Tadaa!!

## Here's what it does. (TADAAbot)


## Here's what it can't do. (TADAAbot Limitations)
1. Screenshots.
2. Think critically.
3. Access certain data sources, such as broken backlinks from AHREFs.
4. Link OneDrive resources in ppt slides
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

## How to run locally

TODO: write this up

## Data Requiring Manual Input
* SC access - bool that adjusts Yes/No image
* GA access - bool that adjusts Yes/No image
* # of Mobile Usability Issues - Adjusts integer and text
* Is Sitemap Submitted in SC - bool that adjusts Yes/No image
* Sitemap URL - string to add to end of sitemap slide
* Robots URL - string to add to end of robots slide
* Structured Data - a multiple choice drop down for the options in slide notes
* Site Content/UX - a multiple choice drop down for the options in slide notes
* Internal/External Dup Content - a multiple choice drop down for the options in slide notes
* Calls to Action - a multiple choice drop down for the options in slide notes
* Blog - a multiple choice drop down for the options in slide notes
* Canonicals - a multiple choice drop down for the options in slide notes
* Website Security - a multiple choice drop down for the options in slide notes
* Mob/Desk Page Speed - two floats for mob/desktop page speed
* # of Broken Backlinks - int 