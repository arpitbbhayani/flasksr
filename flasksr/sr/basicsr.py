# -*- coding: utf-8 -*-
'''
    flasksr.BasicSR
    -------------------------
    The Basic Streaming Response class.
'''

from flask import Response


class BasicSR():
    '''
    This object is used to hold the Flask's Response Object and provide a way
    to stream response.
    '''
    def __init__(self, *args, **kwargs):
        #: Flask Response object
        self.stream_response = Response(self._aggregate(*args), **kwargs)

    def _aggregate(self, *fs):
        '''
        Aggregates all the arguments passed to BasicSR and yields each one in
        provided order. If any of the object passed is callable then it makes
        a function call on it and then yields it; otherwise it yields the string
        representation of the obejct passed.
        '''
        for f in fs:
            if callable(f):
                yield f()
            else:
                yield str(f)

    @property
    def response(self):
        '''
        returns the Flask Response object stored in BasicSR
        '''
        return self.stream_response
