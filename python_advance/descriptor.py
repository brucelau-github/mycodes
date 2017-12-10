# property class
class UpperString(object):
    def __init__(self):
        self._value = ''
        print('initial vlaue')
    def __get__(self, instance, klass):
        print('get vlaue')
        return self._value
    def __set__(self, instance, value):
        print('set vlaue')
        self._value = value.upper()
    def __delete__(self, instantce):
        print('delete vlaue')
        del self._value


class SimpleClass:
    foo = UpperString()


simple = SimpleClass()


#simple.foo = 'foo'
setattr(simple, 'foo', 'foo')
getattr(simple, 'foo')
delattr(simple, 'foo')
