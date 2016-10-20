from flasksr.exceptions import InvalidTypeException


class BaseSR():
    def _validate_callability(self, obj, name):
        if not callable(obj) and type(obj) not in [list, tuple]:
            raise InvalidTypeException("The object passed in variable"\
                  " named %s should be either a function of a list or"\
                  " tuple of functions that returns rendering"\
                  " string" % (name))

        if type(obj) in [list, tuple] and [x for x in obj if not callable(x)]:
            raise InvalidTypeException("The object passed in variable"\
                  " named %s should be either a function of a list or"\
                  " tuple of functions that returns rendering"\
                  " string" % (name))

    def _validate_function_callability(self, obj, name):
        if not callable(obj):
            raise InvalidTypeException("The object passed in variable"\
                  " named %s should be a function" % (name))

    def _yield(self, f):
        '''
        Yields the return value of the function call for a callable object
        '''
        yield f()

    def _yield_all(self, l):
        '''
        Given a iterable like list or tuple the function yields each of its
        items with _yield
        '''
        if l is not None:
            if type(l) in [list, tuple]:
                for f in l:
                    for x in self._yield(f): yield x
            else:
                for x in self._yield(l): yield x
