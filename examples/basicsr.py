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
        render_menu(),
        render_body()
    ).response


if __name__ == '__main__':
    app.run(host='0.0.0.0')
