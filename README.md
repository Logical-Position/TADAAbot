# TADAA

## What is it?

The "Technical Audit Document Automation Assistant", or _TADAA_ is a tool for Analyst's to help streamline the process of preparing tech audit presentations.

## Local (Development)

### Installation

_This application runs on Python. Please ensure you have at least Python 3.10 installed._

To run this project locally for development purposes:

1. Clone the repository: `git clone git@github.com:Logical-Position/TADAAbot.git`
1. Change into the directory: `cd TADAAbot`
1. Install the required packages: `pip3 install -r requirements.txt`
1. Compile tailwindcss: `tailwindcss -i ./tadaa/tailwind/input.css -o ./tadaa/static/styles/tailwind.css`

### Usage

Once the above installation steps are complete, run the development server with the command:
```
flask run
```

## Server (Production)

Currently, this is hosted on an AWS EC2 instance running Ubuntu 22.xx.

A systemd daemon named `tadaa.service` launches the application at server start-up.

gunicorn and nginx are leveraged for handling HTTP requests.

### Installation

TODO

### Usage

TODO

## Roadmap
Completed:
* Parsing of Sitebulb files for relevant SEO data
* _

In progress:
* Automatic creation of tech audit presentation

Future:
* Display "short-list" of audit findings after audit is ran
* SC API
* Analytics API