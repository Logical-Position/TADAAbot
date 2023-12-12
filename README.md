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
Hosted on: Lightsail Ubuntu - ver. 22.04 LTS(Jammy Jellyfish)
### Structure:
* Application runs on a docker container which receives requests from Nginx proxy on host machine: 
  * Nginx Proxy(80) > Tadaa Docker Container(5000)

### Installation:
1. Clone repository: `git clone git@github.com:Logical-Position/TADAAbot.git` into home directory.
1. Create .env file for needed login/session variables in auth.py

### Nginx Setup:
* Nginx config file required w/symlink between `/etc/nginx/sites-available && /etc/nginx/sites-enabled`.

### Docker Setup:
* Build Docker image from Github repository clone: `docker build -t tadaa ~/TADAAbot/`
* Run Docker container from image: `docker run --restart always --name tadaa --env-file ~/.env -dp 5000:5000 tadaa`

### Updating to latest Prod release:
* Will need to stop and remove prior image/container before building one with the same name/ports.
1. Pull latest changes on production branch: `git pull origin/prod`
2. Rebuild new docker image
3. Run new container

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