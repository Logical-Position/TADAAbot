# T.A.D.A.A bot

 ### A Technical Audit Documentation Automation Assistant
 
An automation assistant for tech audits! Tadaa!!

## Here's what it does. (TADAAbot)
* Takes the things
* Organizes the data
* Returns the stuff

## Here's what you do. (The Analyst)
* Input the things
* Think about SEO
* Get the stuff

## How to run locally

* Install Python (https://www.digitalocean.com/community/tutorials/install-python-windows-10)
* Install VScode (https://code.visualstudio.com/)
* Clone project from Github (https://github.com/Logical-Position/TADAAbot)
    1. Make sure you have an account on GitHub and have been granted access to the private LP organization.
    2. Once you are granted access, you can navigate to the repository you want to clone.
    3. Click on the "Code" button on the right-hand side of the repository page.
    4. Select the "Clone with HTTPS" option, and copy the HTTPS URL that appears.
    5. Open your terminal or command prompt and navigate to the directory where you want to clone the repository.
    6. Type git clone followed by the HTTPS URL you copied earlier, and press Enter.
    7. You will be prompted to enter your GitHub username and password. Enter the credentials associated with the account that has access to the private organization.
    8. Once you have entered your credentials, the repository will be cloned to your local machine.
* Create virtual environment (https://docs.python.org/3/library/venv.html)
    1. Open the cloned project directory using VS code, open a new terminal using the 'Terminal' tab, and run this command: python -m venv venv
        This will create a new folder named "venv" in the project directory, which contains a copy of the Python executable, as well as the standard Python libraries.
    2. To activate the virtual environment, run the following command: venv\Scripts\activate.bat ('source venv/bin/activate' on macOS)
    3. You should now see a <venv> tag in front of your terminal.
* Install the project dependencies by running this command: pip install -r requirements.txt
* Start the server by running this command: python main.py
* Open the app by following the 'Running on' local IP link located in the terminal.
* Tadaa!


## Data Requiring Manual Input
* CMS - possibly optional, just for internal data.
* SC access - bool that adjusts Yes/No image
* GA access - bool that adjusts Yes/No image
* Num of Mobile Usability Issues - Adjusts integer and text
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
* Num of Broken Backlinks - Adjusts integer and text 

## Flow

![TADAA Flow Diagram](https://github.com/Logical-Position/TADAAbot/blob/dev/tadaa-state-diagram.png)

## Meta Data and Aggregate Analyses
## 
## Contributors
* Jake Applehans
* Mic Ruopp
* Jordan Schwartz
* Jack Ross
