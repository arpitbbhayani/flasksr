class Dom():
    def __init__(self, component_id, render_function, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.render_function = render_function

    def execute(self):
        return """%(dom_string)s""" % {
            'dom_string': self.render_function(*self.args, **self.kwargs)
        }
