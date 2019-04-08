# Декоратор, считающий и выводящий количество вызовов декорируемой функции.

def wrapper(*args, **kwargs):
         wrapper.count += 1
         res = func(*args, **kwargs)
         print("{0} была вызвана: {1}x".format(func.__name__, wrapper.count))
         return res
     wrapper.count = 0
     return wrapper


# ПАРАМЕТРИЗУЕМЫЙ декоратор, добавляющий тэги (подобно примеру из практики).

from functools import partial

def _pseudo_decor(fun, argument):
    def ret_fun(*args, **kwargs):
        #do stuff here, for eg.
        print ("decorator arg is %s" % str(argument))
        return fun(*args, **kwargs)
    return ret_fun

real_decorator = partial(_pseudo_decor, argument=arg)

@real_decorator
def foo(*args, **kwargs):
    pass

# Придумать любой свой декоратор.

def double(f):
    def aux(*xs, **kws):
        return 2 * f(*xs, **kws)
    return aux

@double
def function(a):
    return 10 + a

print function(3)