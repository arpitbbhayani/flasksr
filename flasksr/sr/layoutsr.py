# -*- coding: utf-8 -*-
'''
    flasksr.LayoutSR
    -------------------------
    The Layout based Streaming Response class.
'''

from flask import Response
from flasksr.sr.basesr import BaseSR


class LayoutSR(BaseSR):
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
            self._validate_function_callability(self.layout, 'layout')

        if 'pre_stream' in kwargs:
            self.pre_stream = kwargs.pop('pre_stream')
            self._validate_callability(self.pre_stream, 'pre_stream')

        if 'post_stream' in kwargs:
            self.post_stream = kwargs.pop('post_stream')
            self._validate_callability(self.post_stream, 'post_stream')

        if self.components:
            self._validate_callability(self.components, 'args')

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
            var MyMutationObserver = (function () {
                var prefixes = ['WebKit', 'Moz', 'O', 'Ms', '']
                for(var i=0; i < prefixes.length; i++) {
                    if(prefixes[i] + 'MutationObserver' in window) {
                        return window[prefixes[i] + 'MutationObserver'];
                    }
                }
                return false;
            }());

            var observer = null;
            if(MyMutationObserver) {
                var target = document.querySelector('#streaming-div');
                var observer = new MyMutationObserver(function(mutations) {
                    mutations.forEach(function(mutation) {
                        var obj = mutation.addedNodes[0];
                        if(obj instanceof HTMLElement) {
                            var referenceId = obj.getAttribute("refsrid");
                            if(referenceId) {
                                var content = obj.innerHTML;
                                var x = document.getElementById("streaming-div-layout").querySelectorAll("*[srid='"+referenceId+"']")[0].innerHTML = content;
                                obj.innerHTML = '';
                            }
                        }
                    });
                });

                // configuration of the observer:
                var config = {
                    childList: true
                }
                observer.observe(target, config);
                document.addEventListener("DOMContentLoaded", function(event) {
                    observer.disconnect();
                });
            }
            else {
                // Fallback
                alert("MutationObserver not found");
            }
        </script>"""

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
