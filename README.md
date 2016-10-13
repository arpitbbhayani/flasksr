# FlaskSR

FlaskSR provides an easy way to add streaming HTTP Responses for Flask.

## Why should you use this?

When the user sees something happening on the screen; the site has begun to render in response to their request. This critical first step tells the user that the site is responding to their action.
This measure is called "Time to First Paint". Today most of the websites are trying to minimize this measure. In order to enable this it is necessary to not send the complete response in one go but to push partial responses multiple times.

![flasksr-comparison](https://cloud.githubusercontent.com/assets/4745789/19354772/86697410-9185-11e6-83d0-a0c26f29e3d5.gif)

## Installation
Install the extension with the following command:

```
$ pip install flasksr
```

## Usage
Once installed, the FlaskSR is easy to use. Let's walk through setting up a basic application. Also please note that this is a very basic guide: we will be taking shortcuts here that you should never take in a real application.

To begin we'll set up a Flask app:

```py
from flask import Flask
from flasksr import BasicSR

app = Flask(__name__)


def render_menu():
    return """<ul style="list-style-type: none; margin: 0; padding: 0;">
        <li><a href="/">Home</a></li>
        <li><a href="#">News</a></li>
        <li><a href="#">Contact</a></li>
        <li><a href="#">About</a></li>
    </ul>"""


def render_body():
    return """
        <div style="margin-top: 50px;">Hello World!</div>
    """


@app.route('/')
def hello():
    return BasicSR(
        render_menu,
        render_body
    ).response


if __name__ == '__main__':
    app.run(host='0.0.0.0')
```

## Documentation

Complete documentation for FlaskSR is available on [FlaskSR's GitBook](https://arpitbbhayani.gitbooks.io/flasksr/).

## Contributing

We welcome contributions! If you would like to hack on FlaskSR, please follow these steps:

 - Fork this repository
 - Make your changes
 - Submit a pull request after running make check (ensure it does not error!)
 - Please give us adequate time to review your submission. Thanks!
