class Frozen:
    '''
    An interesting feature that is almost never used by developers is slots.
    They allow you to set a static attribute list for a given class with the
    __slots__ attribute, and skip the creation of the __dict__ list in each
    instance of the class.  They were intended to save memory space for classes
    with a very few attributes, since __dict__ is not created at every instance.
    '''
    __slots__ = ['ice','cream']

    this_is_same_way = 'static attribute'

print(dir(Frozen))
