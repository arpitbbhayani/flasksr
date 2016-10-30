class Component():
    def __init__(self, render_function, *args, **kwargs):
        self.render_function = render_function
        self.args = args
        self.kwargs = kwargs

    def execute(self):
        return self.render_function(*self.args, **self.kwargs)
