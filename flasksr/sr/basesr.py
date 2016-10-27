from flasksr.exceptions import InvalidTypeException


class BaseSR():
    str_types = [str]

    try: temp = unicode
    except: pass
    else: str_types.append(unicode)

    def _validate_renderability(self, obj, name):
        if type(obj) not in [list, tuple] and type(obj) not in str_types:
            raise InvalidTypeException("The object passed in variable"\
                  " named %s should be either a `str` to be rendered or a"\
                  " list/tuple of `str` that are to be rendered" % (name))

        if type(obj) in [list, tuple] and [x for x in obj
                                           if type(x) not in str_types]:
            raise InvalidTypeException("The object passed in variable"\
                  " named %s should be either a `str` to be rendered or a"\
                  " list/tuple of `str` that are to be rendered" % (name))

    def _yield(self, f):
        '''
        Yields the value f representing the render string.
        '''
        yield f

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
