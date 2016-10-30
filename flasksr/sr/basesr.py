from flasksr.entities import Component, Layout, Dom
from flasksr.exceptions import InvalidTypeException


class BaseSR():
    def _is_component(self, obj):
        return isinstance(obj, Component)

    def _is_layout(self, obj):
        return isinstance(obj, Layout)

    def _is_dom(self, obj):
        return isinstance(obj, Dom)

    def _validate_iter_or_component(self, obj, name):
        if not isinstance(obj, Component) and type(obj) not in [list, tuple]:
            raise InvalidTypeException("The object passed in variable"
                  " named %s is instance of %s but should be either of"
                  " instance of `Component` or a list/tuple of `Component`"
                  " objects" % (name, obj.__class__.__name__))

        if type(obj) in [list, tuple] and [x for x in obj
                                           if not self._is_component(x)]:
            raise InvalidTypeException("The object passed in variable"
                  " named %s is instance of %s but should be either of"
                  " instance of `Component` or a list/tuple of `Component`"
                  " objects" % (name, obj.__class__.__name__))

    def _validate_iter_or_dom(self, obj, name):
        if not isinstance(obj, Dom) and type(obj) not in [list, tuple]:
            raise InvalidTypeException("The object passed in variable"
                  " named %s is instance of %s but should be either of"
                  " instance of `Dom` or a list/tuple of `Dom`"
                  " objects" % (name, obj.__class__.__name__))

        if type(obj) in [list, tuple] and [x for x in obj
                                           if not self._is_dom(x)]:
            raise InvalidTypeException("The object passed in variable"
                  " named %s is instance of %s but should be either of"
                  " instance of `Dom` or a list/tuple of `Dom`"
                  " objects" % (name, obj.__class__.__name__))

    def _validate_component(self, obj, name):
        if self._is_component(obj) is False:
            raise InvalidTypeException("The object passed in variable"
                  " named %s is instance of `%s` but should be an instance of"
                  " `Component`" % (name, obj.__class__.__name__))

    def _validate_layout(self, obj, name):
        if self._is_layout(obj) is False:
            raise InvalidTypeException("The object passed in variable"
                  " named %s is instance of `%s` but should be an instance of"
                  " `Layout`" % (name, obj.__class__.__name__))

    def _validate_dom(self, obj, name):
        if self._is_dom(obj) is False:
            raise InvalidTypeException("The object passed in variable"
                  " named %s is instance of `%s` but should be an instance of"
                  " `Dom`" % (name, obj.__class__.__name__))

    def _yield(self, f):
        '''
        Yields the return value of the function call of `Component`, `Layout`
        and `Dom`
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
