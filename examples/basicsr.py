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
