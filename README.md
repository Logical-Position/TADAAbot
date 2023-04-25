# T.A.D.A.A bot

### A Technical Audit Documentation Automation Assistant.
 
An automation assistant for tech audits! _Tadaa!!_

## Overview

### Here's what it does. (TADAAbot)
* Takes the things
* Organizes the data
* Returns the stuff

### Here's what you do. (The Analyst)
* Input the things
* Think about SEO
* Get the stuff

## Installation

### Local

* Install Python (https://www.digitalocean.com/community/tutorials/install-python-windows-10)
* Install VScode (https://code.visualstudio.com/)
* Clone project from Github (https://github.com/Logical-Position/TADAAbot)
    1. Click on the "Code" button on the right-hand side of the Tadaa repository page.
    2. Select the "Clone with HTTPS" option, and copy the HTTPS URL that appears.
    3. Open your terminal or command prompt and navigate to the directory where you want to clone the repository.
    4. Type git clone followed by the HTTPS URL you copied earlier, and press Enter.
    5. You will be prompted to enter your GitHub username and password. Enter the credentials associated with the account that has access to the private organization.
    6. Once you have entered your credentials, the repository will be cloned to your local machine.
* Create virtual environment (https://docs.python.org/3/library/venv.html)
    1. Open the cloned project directory using VS code, open a new terminal using the 'Terminal' tab, and run this command: python -m venv venv
        This will create a new folder named "venv" in the project directory, which contains a copy of the Python executable, as well as the standard Python libraries.
    2. To activate the virtual environment, run the following command: venv\Scripts\activate.bat ('source venv/bin/activate' on macOS)
    3. You should now see a <venv> tag in front of your terminal.
* Install the project dependencies by running this command: pip install -r requirements.txt
* Start the server by running this command: python main.py
* Open the app by following the 'Running on' local IP link located in the terminal.
* Tadaa!

#### Tailwind Integration

* SOURCE: https://flowbite.com/docs/getting-started/flask/
* npm install -D tailwindcss
* npx tailwindcss init
* > add './templates/**/*.html' to the content array
* > import Tailwind CSS directives @tailwind base; @tailwind components; @tailwind utilities;
* add <link rel="stylesheet" href="{{ url_for('static',filename='dist/css/output.css') }}"> to base.html
* run `npx tailwindcss -i ./static/src/input.css -o ./static/dist/css/output.css --watch`

### Server

TODO

## Resources

https://excalidraw.com/

https://www.makeareadme.com/

### Google Firestore Documentation

* [Initialization](https://firebase.google.com/docs/firestore/quickstart#python)
* [Adding data](https://firebase.google.com/docs/firestore/quickstart#add_data)
* [Reading data](https://firebase.google.com/docs/firestore/quickstart#read_data)
* TODO: Find a more detailed write-up than the "Quick Start"

### Application Flow

![TADAA Flow Diagram](https://github.com/Logical-Position/TADAAbot/blob/dev/docs/tadaa-state-diagram.png)

## Meta Data and Aggregate Analyses

TODO