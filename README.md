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
gunicorn and nginx are leveraged for handling HTTP requests.

Hosted on: Lightsail Ubuntu - ver. 22.04 LTS(Jammy Jellyfish)
### Structure:
* Application runs on a docker container which receives requests from Nginx proxy on host machine: 
  * Nginx Proxy(80) > Tadaa Docker Container(5000)
* `dock` bash file in home directory for bash commands

### Docker Setup:
* Dockerfile and .dockerignore found in TADAAbot directory for build process
* Tadaa currently restarts any time docker daemon restarts using `--restart always` flag.

### Installation:
* Prerequisites: Nginx and Docker Install
    * Nginx setup required `/etc/nginx/sites-available && /etc/nginx/sites-enabled` for proxypass.
1. Clone repository: `git clone git@github.com:Logical-Position/TADAAbot.git` into ~/ directory.
1. Create .env file for needed login/session variables
1. Source `dock` file in terminal: 
`source dock` -> (`build` - `stopprod` - `runprod`)
2. Build Docker Image: 
`build` -> (`docker build -t tadaa ~/TADAAbot/`)
1. Run Production: 
`runprod` -> (`docker run --restart always --name tadaa --env-file ~/.env -dp 5000:5000 tadaa`)

### Updating to latest Prod release:
* Will need to stop and remove prior image/container before building one with the same name/ports.
1. Pull latest changes on production branch: `git pull origin/prod`
2. Rebuild new docker image: `build`
3. Run new container: `runprod`
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