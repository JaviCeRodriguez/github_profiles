# GitHub Profile Searcher

A minimal searcher with Flask and GitHub API

## Installation

```sh
# Clone repository
git clone https://github.com/JaviCeRodriguez/github_profiles.git

# Move on folder project
cd ./github_profiles

# Create virtual environment
python -m virtualenv venv

# Activate
venv/Scripts/activate

# Install packages
pip install -r requirements.txt
```

## Run project

Run with the next commands ([view docs for flask's envs variables](https://flask.palletsprojects.com/en/2.1.x/quickstart/)):

```sh
# On PowerShell
$env:FLASK_APP = "src/main"
$env:FLASK_ENV = "development"
flask run
```