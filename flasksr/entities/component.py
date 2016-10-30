class Component():
    def __init__(self, component_id, render_function, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.id = component_id
        self.render_function = render_function

    def execute(self):
        return """
            <sr-component id="%(id)s">%(dom_string)s</sr-component>
        """ % {
            'id': self.id,
            'dom_string': self.render_function(*self.args, **self.kwargs)
        }
