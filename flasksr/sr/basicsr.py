from flask import Response


class BasicSR():
    def __init__(self, *args, **kwargs):
        self.stream_response = Response(self._aggregate(*args), **kwargs)

    def _aggregate(self, *fs):
        for f in fs:
            if callable(f):
                yield f()
            else:
                yield str(f)

    @property
    def response(self):
        return self.stream_response
