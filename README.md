# Installation

This project requires the following tools:

- Python - The programming language used by Flask.
- [Tweepy](http://www.tweepy.org/) - A wrapper library for easily accessing the Twitter API
- [Flask](http://flask.pocoo.org/) - A microframework for Python web applications
- [Jinja2](http://jinja.pocoo.org/docs/2.10/) - A templating language for Python, used by Flask.

## Getting Started

**Step 1. Clone this repo into a fresh folder**

**Step 2. Create a Virtual Environment and install Dependencies.**

Create a new virtual environment:
```
$ python -m venv venv
```

Activate the environment:
```
$ source venv/bin/activate
```

Install the project dependencies, which are listed in `requirements.txt`.

```
(venv) $ pip install -r requirements.txt
```
:

```
(venv) $ FLASK_APP=app.py flask run
```

Open http://localhost:5000 to view it in your browser.
