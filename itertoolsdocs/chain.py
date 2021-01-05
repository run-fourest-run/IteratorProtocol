import itertools

'''
Make an iterator that returns elements from the first iterable until its exhausted. Then proceed to the next
iterable, until all the iterables are exhausted.

Used for treating consecutive sequences as a single sequence

'''


def chain(*iterables):
    for it in iterables:
        for element in it:
            yield element

def from_iterable(iterable):
    # itertools.chain.from_iterable(['abc','def']) -> a b c d e f
    for it in iterable:
        for element in it:
            yield element


data1 = [10,20,30,40,50]
data2 = [60,70,80,90,100]
chained_data = itertools.chain(data1,data2)

it = iter(data1)
it1 = next(it)
print(it1)
it1 = next(it)
print(it1)
it2 = next(it)
print(it1,it2)
