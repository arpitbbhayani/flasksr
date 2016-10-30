from flask import Flask
from flasksr import LayoutSR, Component, Layout, Dom

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


def render_layout():
    '''This function returns the render string of the layout of the page.
    '''

    return """
        <div style="width: 100%;">
            <div ref-sr-id="left-side" style="float:left; width: 45%"></div>
            <div ref-sr-id="right-side" style="float:right; width: 45%"></div>
        </div>
    """

def render_left():
    '''This function returns the render string of the left half of the page
    '''

    return """
        <div style="background: green;">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut placerat metus lectus, sed dignissim turpis egestas vel. Proin quis nibh nulla. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean magna mauris, pellentesque at tincidunt at, varius at velit. Nam ultricies dui eget nisl aliquam mattis. Morbi commodo, orci ac interdum sagittis, urna massa vulputate lorem, non mollis mauris est ultricies lectus. Phasellus non lacus a felis fringilla scelerisque. Mauris et enim consectetur, scelerisque enim non, mattis est. Aenean eget diam a diam aliquam congue ac vel mi. Curabitur sollicitudin ultrices tellus in blandit. Quisque non auctor est, quis faucibus erat. Donec porta elit libero, eu pellentesque mi malesuada a. Suspendisse ut faucibus ligula, non sodales nulla. Nunc vehicula blandit ullamcorper. Fusce mattis ultrices urna in elementum.
            Pellentesque at euismod libero. Cras pretium vulputate mi, feugiat ullamcorper nunc accumsan ac. Proin quam ante, laoreet quis sapien id, bibendum pretium nisl. Nulla pulvinar lobortis scelerisque. Curabitur venenatis, orci eget congue tristique, magna ipsum auctor mi, eget tincidunt augue mi in nisi. Mauris nibh felis, lobortis at varius ac, faucibus quis sapien. Suspendisse eu porta metus, non lacinia erat. Sed id eros at massa commodo placerat quis eget lacus. Nullam sed odio quis libero vehicula consequat. Maecenas id neque nec lectus porttitor cursus. Suspendisse ultricies nisl ligula, non tempus est dignissim in. Nam id suscipit enim. Mauris arcu tortor, efficitur eu nisi at, pretium placerat neque. Sed mattis dapibus sagittis. Mauris a ligula vitae neque ullamcorper sodales.
        </div>
    """

def render_right():
    '''This function returns the render string of the right half of the page
    '''

    return """
        <div style="background: blue;">
            Quisque consequat nunc vitae ex hendrerit, in tempor felis eleifend. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Phasellus euismod erat accumsan tellus consequat imperdiet. Nulla facilisi. Proin tristique orci et risus convallis, vel pretium lorem bibendum. Proin nec rutrum urna. Aenean luctus convallis rhoncus. Quisque bibendum augue eu luctus luctus. Suspendisse posuere libero leo, sed vehicula felis posuere non. Fusce hendrerit, lorem eu hendrerit tempus, neque mauris dignissim dui, et ultricies turpis velit vel lorem. Sed scelerisque sit amet libero ac auctor. Donec mollis faucibus rutrum. Aliquam erat volutpat. Quisque imperdiet tellus in pulvinar gravida.
            Fusce eu erat sem. Curabitur rutrum libero nec orci iaculis placerat. Ut sed egestas arcu. Aliquam facilisis ullamcorper risus nec vestibulum. Duis gravida leo quis tempor dignissim. Nulla consectetur cursus libero, a dapibus nunc iaculis nec. Phasellus vel lacus vitae velit consequat mollis. Integer pulvinar odio vel libero posuere, sit amet ornare ante ornare.
        </div>
    """


@app.route('/')
def hello():
    return LayoutSR(
        Component("right-side", render_right),
        Component("left-side", render_left),
        layout=(Layout(render_layout),),
        pre_stream=(Dom("head", render_first),
                    Dom("top-menu", render_menu),),
        post_stream=Dom("footer", render_last)
    ).response


if __name__ == '__main__':
    app.run(host='0.0.0.0')
