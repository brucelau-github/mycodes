def p_decorate(fun):
    def func_wrapper(name):
        return '<p> %s </p>' % fun(name)
    return func_wrapper


@p_decorate
def get_text(name):
    return 'this is %s' % name

def n_get_text(name):
    return 'this is %s' % name

print(get_text('bruce'))
dec_f = p_decorate(n_get_text)
print(dec_f('bruce'))
