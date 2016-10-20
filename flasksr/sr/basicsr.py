# -*- coding: utf-8 -*-
'''
    flasksr.BasicSR
    -------------------------
    The Basic Streaming Response class.
'''

from flask import Response
from flasksr.sr.basesr import BaseSR


class BasicSR(BaseSR):
    '''
    This object is used to hold the Flask's Response Object and provide a way
    to stream response.
    '''
    def __init__(self, *args, **kwargs):
        self.components = args
        self.kwargs = kwargs

        if self.components:
            self._validate_callability(self.components, 'args')

    def _aggregate(self):
        '''
        Aggregates all the arguments passed to BasicSR and yields each one in
        provided order. If any of the object passed is callable then it makes
        a function call on it and then yields it; otherwise it yields the
        string representation of the obejct passed.
        '''
        # Yielding components
        for x in self._yield_all(self.components): yield x

    @property
    def response(self):
        '''
        returns the Flask Response object stored in BasicSR
        '''
        return Response(self._aggregate(), **self.kwargs)
