# Introduction

This is the starter code for the MLHLocalhost Twitter Bot Workshop

The root directory contains the final project configured for Heroku.
The starter-project folder contains the skeleton code for the workshop.
The final-project folder is a working example of the workshop project.
### Note: Need to add a keys.py file to final-project for it to work

# Installation

This project requires the following tools:

- Python - The programming language used by Flask.
- [Tweepy](http://www.tweepy.org/) - A wrapper library for easily accessing the Twitter API
- [Flask](http://flask.pocoo.org/) - A microframework for Python web applications
- [Jinja2](http://jinja.pocoo.org/docs/2.10/) - A templating language for Python, used by Flask.

To get started, install Python

## Getting Started

**Step 1. Clone this repo into a fresh folder**

```
$ git clone https://github.com/Siunami/MLH-Localhost-Twitter-Feed.git
$ cd MLH-Localhost-Twitter-Feed
```

**Step 2. Create a Virtual Environment and install Dependencies.**

Create a new virtual environment, if you haven't already:
```
$ python -m venv venv
```

Activate the environment:
```
$ source venv/bin/activate
```

Next, we need to install the project dependencies, which are listed in `requirements.txt`.

```
(venv) $ pip install -r requirements.txt
```

Now we're ready to start our server which is as simple as:

```
(venv) $ FLASK_APP=app.py flask run
```

Open http://localhost:5000 to view it in your browser.
