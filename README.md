# FlaskSR

FlaskSR provides an easy way to add streaming HTTP Responses for Flask.

## Why should you use this?

Most of the websites are trying to minimize "Time to First Paint". This can be done by streaming partial responses to client. FlaskSR enables this functionality in n easy way for [Flask Web Framework](http://flask.pocoo.org/). With FlaskSR you can start streaming partial HTTP responses depending on layout to client so that client starts seeing some content along the way instead of seeing all of the site's content at once.

Advantages:
 - Minimizes Time for first paint.
 - No impact on SEO - as nothing goes via AJAX calls.
 - Start rendering important part of your page first so user start seeing important things first.
 - Improves perceived performance of the page.

## Installation
Install the extension with the following command:

```
$ pip install flasksr
```

## FlaskSR in action
![impact](https://cloud.githubusercontent.com/assets/4745789/19834915/7354d69a-9e9a-11e6-8ab6-b7b95146a25c.gif)

## Usage
Once installed, the FlaskSR is easy to use. Let's walk through setting up a basic application. Also please note that this is a very basic guide: we will be taking shortcuts here that you should never take in a real application.

To begin we'll set up a Flask app:

```py
from flask import Flask
from flasksr import BasicSR, Dom

app = Flask(__name__)


def render_menu():
    return """
        <ul style="list-style-type: none; margin: 0; padding: 0;">
            <li><a href="/">Home</a></li>
            <li><a href="#">News</a></li>
            <li><a href="#">Contact</a></li>
            <li><a href="#">About</a></li>
        </ul>
    """


def render_body():
    return """
        <div style="margin-top: 50px;">Hello World!</div>
    """

def render_first():
    return """
        <html>
            <head>
                <title>FlaskSR Example</title>
            </head>
            <body>
    """

def render_last():
    return """
            </body>
        </html>
    """


@app.route('/')
def hello():
    return BasicSR(
        Dom(render_first),
        Dom(render_menu),
        Dom(render_body),
        Dom(render_last)
    ).response


if __name__ == '__main__':
    app.run(host='0.0.0.0')
```

Above example shows a very basic top down response streaming with [BasicSR](https://arpitbbhayani.gitbooks.io/flasksr/content/sr/basicsr.html) For advanced usage when you want a particular part of your page to get rendered first you can use [LayoutSR](https://arpitbbhayani.gitbooks.io/flasksr/content/sr/layoutsr.html)

## Examples
You can find examples and sample usage [here](https://github.com/arpitbbhayani/flasksr/tree/master/examples)

## Documentation

Complete documentation for FlaskSR is available on [FlaskSR's GitBook](https://arpitbbhayani.gitbooks.io/flasksr/).

## Contributing

We welcome contributions! If you would like to hack on FlaskSR, please follow these steps:

 - Fork this repository
 - Make your changes
 - Submit a pull request after running make check (ensure it does not error!)
 - Please give us adequate time to review your submission. Thanks!
