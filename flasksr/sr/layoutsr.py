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

        # Function from kwargs that renders the layout for components
        self.layout = None

        # Function(s) that needs to be rendered before component stream begins
        self.pre_stream = None

        # Function(s) that needs to be rendered after component stream ends
        self.post_stream = None

        # Function(s) each of which renders one component
        self.components = args

        # kwargs passed to LayoutSR
        self.kwargs = kwargs

        # ID of the DIV element where all components are initially streamed
        self.stream_div_id = 'stream-div'

        # ID of the DIV element inside which layout of components is defined
        self.stream_div_layout_id = 'stream-div-layout'

        if 'layout' in kwargs:
            self.layout = kwargs.pop('layout')
            self._validate_function_callability(self.layout, 'layout')

        if 'pre_stream' in kwargs:
            self.pre_stream = kwargs.pop('pre_stream')
            self._validate_callability(self.pre_stream, 'pre_stream')

        if 'post_stream' in kwargs:
            self.post_stream = kwargs.pop('post_stream')
            self._validate_callability(self.post_stream, 'post_stream')

        if 'stream_div_id' in kwargs:
            self.stream_div_id = kwargs.pop('stream_div_id')

        if 'stream_div_layout_id' in kwargs:
            self.stream_div_layout_id = kwargs.pop('stream_div_layout_id')

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
        <div id="%s">
        <script>
            var MyFlaskSRMutationObserver = (function () {
                var prefixes = ['WebKit', 'Moz', 'O', 'Ms', '']
                for(var i=0; i < prefixes.length; i++) {
                    if(prefixes[i] + 'MutationObserver' in window) {
                        return window[prefixes[i] + 'MutationObserver'];
                    }
                }
                return false;
            }());

            if(MyFlaskSRMutationObserver) {
                var target = document.getElementById('%s');
                var observerFlaskSR = new MyFlaskSRMutationObserver(function(mutations) {
                    mutations.forEach(function(mutation) {
                        var obj = mutation.addedNodes[0];
                        if(obj instanceof HTMLElement) {
                            var referenceId = obj.getAttribute('sr-id');
                            if(referenceId) {
                                document.getElementById('%s').querySelectorAll("*[ref-sr-id='"+referenceId+"']")[0].innerHTML = obj.innerHTML;
                                obj.innerHTML = '';
                            }
                        }
                    });
                });
                var config = {
                    childList: true
                }
                observerFlaskSR.observe(target, config);
                document.addEventListener("DOMContentLoaded", function(event) {
                    observerFlaskSR.disconnect();
                });
            }
            else {
                console.log("MutationObserver not found!");
            }
        </script>""" % (
            self.stream_div_id,
            self.stream_div_id,
            self.stream_div_layout_id
        )

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
