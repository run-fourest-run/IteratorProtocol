import itertools


'''
make an iterator return elements from the iterable and saving copy of each. When the iterable is exhausted,
return elements from the saved copy. Repeates indefinetly. 

'''

iterable = [1,2,3,4,5,6,7,8]
cycle = itertools.cycle(iterable)
for x in cycle:
    print(x)

'''equivilant too'''
def cycle(iterable):
    saved = []
    for element in iterable:
        yield element
        saved.append(element)
    while saved:
        for element in saved:
            yield element