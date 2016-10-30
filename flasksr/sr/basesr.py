from flasksr.entities import Component
from flasksr.exceptions import InvalidTypeException


class BaseSR():
    def _validate_iter_or_component(self, obj, name):
        if not isinstance(obj, Component) and type(obj) not in [list, tuple]:
            raise InvalidTypeException("The object passed in variable"
                  " named %s is of type %s but should be either of instance"
                  " of `Component` or a list/tuple of `Component`"
                  " objects" % (type(obj), name))

        if type(obj) in [list, tuple] and [x for x in obj
                                           if not self._is_component(x)]:
            raise InvalidTypeException("The object passed in variable"
                  " named %s is of type %s but should be either of instance"
                  " of `Component` or a list/tuple of `Component`"
                  " objects" % (type(obj), name))

    def _validate_component(self, obj, name):
        if self._is_component(obj) is False:
            raise InvalidTypeException("The object passed in variable"
                  " named %s is of type `%s` but should be of type"
                  " `Component`" % (type(obj), name))

    def _is_component(self, obj):
        return isinstance(obj, Component)

    def _yield(self, f):
        '''
        Yields the return value of the function call of `Component`
        '''
        yield f.execute()

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
