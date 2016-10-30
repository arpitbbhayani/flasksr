class Layout():
    def __init__(self, render_function, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.render_function = render_function

    def execute(self):
        return """
            <sr-layout id="%(id)s">%(dom_string)s</sr-layout>
        """ % {
            'id': self.id,
            'dom_string': self.render_function(*self.args, **self.kwargs)
        }
