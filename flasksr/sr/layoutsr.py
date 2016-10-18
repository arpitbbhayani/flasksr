# -*- coding: utf-8 -*-
'''
    flasksr.LayoutSR
    -------------------------
    The Layout based Streaming Response class.
'''

from flask import Response
from flasksr.exceptions import InvalidTypeException


class LayoutSR():
    '''
    This object is used to hold the Flask's Response Object and provide a way
    to stream response. And place it with respect to provided layout.
    '''
    def __init__(self, *args, **kwargs):
        self.layout = None
        self.pre_stream = None
        self.post_stream = None
        self.components = args
        self.kwargs = kwargs

        if 'layout' in kwargs:
            self.layout = kwargs.pop('layout')
            self._validate_callability(self.layout, 'layout')

        if 'pre_stream' in kwargs:
            self.pre_stream = kwargs.pop('pre_stream')
            self._validate_callability(self.pre_stream, 'pre_stream')

        if 'post_stream' in kwargs:
            self.post_stream = kwargs.pop('post_stream')
            self._validate_callability(self.post_stream, 'post_stream')

    def _validate_callability(self, obj, name):
        if not callable(obj) and type(obj) not in [list, tuple]:
            raise InvalidTypeException("The object passed in variable"\
                  "named %s should be either a function of a list or"\
                  "tuple of functions that returns rendering"\
                  "string" % (name))

        if type(obj) in [list, tuple] and [x for x in obj if not callable(x)]:
            raise InvalidTypeException("The object passed in variable"\
                  "named %s should be either a function of a list or"\
                  "tuple of functions that returns rendering"\
                  "string" % (name))

    def _yield(self, f):
        '''
        Yields a string representation for a non-callable object
        Yields the return value of the function call for a callable object
        '''
        if callable(f): yield f()
        else: yield str(f)

    def _yield_all(self, l):
        '''
        Given a iterable like list/tuple/set the function yields each of its
        items with _yield
        '''
        if l is not None:
            if type(l) in [list, tuple]:
                for f in l:
                    for x in self._yield(f): yield x
            else:
                for x in self._yield(l): yield x

    def _aggregate(self):
        '''
        The function aggreagtes all pre_stream, layout and post_stream and
        components, and yields them one by one.
        '''
        # Yielding everything under pre_stream
        for x in self._yield_all(self.pre_stream): yield x

        # Yielding layout
        for x in self._yield_all(self.layout): yield x

        # Yield LayoutSR Specific Content
        yield """
        <div id="streaming-div">
        <script>
            // http://www.w3.org/TR/dom/
            // http://updates.html5rocks.com/2012/02/Detect-DOM-changes-with-Mutation-Observers
            // https://developer.mozilla.org/en-US/docs/DOM/MutationObserver
            var MyMutationObserver = (function () {
              var prefixes = ['WebKit', 'Moz', 'O', 'Ms', '']
              for(var i=0; i < prefixes.length; i++) {
                if(prefixes[i] + 'MutationObserver' in window) {
                  return window[prefixes[i] + 'MutationObserver'];
                }
              }
              return false;
            }());

            if(MyMutationObserver) {
              // Use MutationObserver
              // select the target node
              var target = document.querySelector('#streaming-div');

              // create an observer instance
                var observer = new MyMutationObserver(function(mutations) {
                    mutations.forEach(function(mutation) {
                        if(mutation.type == 'childList') {
                            var obj = mutation.addedNodes[0];
                            if(obj instanceof HTMLElement) {
                                var referenceId = obj.getAttribute("refsrid");
                                if(referenceId) {
                                    var content = obj.innerHTML;
                                    var x = document.getElementById("streaming-div-layout").querySelectorAll("*[srid='"+referenceId+"']")[0].innerHTML = content;
                                    obj.innerHTML = '';
                                }
                            }
                        }
                    });
                });

              // configuration of the observer:
              var config = { attributes: false, childList: true, characterData: true }

              // pass in the target node, as well as the observer options
              observer.observe(target, config);

              document.addEventListener("DOMContentLoaded", function(event) {
                observer.disconnect();
              });
            }
            else {
              // Fallback
              alert("MutationObserver not found");
            }
        </script>
        """

        # Yielding components
        for x in self._yield_all(self.components): yield x

        # Yield LayoutSR Specific Content
        yield """</div>"""

        # Yielding everything under post_stream
        for x in self._yield_all(self.post_stream): yield x

    @property
    def response(self):
        '''
        Returns the Flask Response object stored in LayoutSR
        '''
        return Response(self._aggregate(), **self.kwargs)
