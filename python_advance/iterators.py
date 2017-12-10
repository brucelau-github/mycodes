i = iter("abc")
print(i.__next__())
# 'a'
print(i.__next__())
# 'b'
print(i.__next__())
# 'c'

try:
    print(i.__next__())
# raise StopIteration
except Exception as e:
    print(e)

class MyIterator(object):
    def __init__(self, step):
        self.step = step

    def __next__(self):
        if self.step == 0:
            raise StopIteration
        self.step -= 1
        return self.step

    def __iter__(self):
        return self

for el in MyIterator(4):
    print(el)


print('generators ...')
# generators

def fib():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a+b

fibo= fib()
print(fibo.__next__())
print(fibo.__next__())
print([fibo.__next__() for i in range(10)])

print('powering ...')
def power(values):
    for v in values:
        print('powering %s'%v)
        yield v

def adder(values):
    for v in values:
        print('adding to %s' %v)
        if v % 2 == 0:
            yield v + 3
        else:
            yield v + 2

elements = [1, 4, 7, 12, 19]
res = adder(power(elements))
print(res.__next__())
print(res.__next__())


def ask_yes():
    while True:
        answer = yield
        if answer in ('yes', 'y'):
            print('bye')
        else:
            print('no not yes but %s'%answer)
f = ask_yes()
f.__next__()
import string
import random
for i in range(1000):
    f.send(random.choice(string.ascii_letters))
