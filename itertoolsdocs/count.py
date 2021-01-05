import itertools


'''
make an iterator that returns evenly spaced values starting with number start, 

often used with count to generate consecutive data points'''



'''equivilant to... '''


count = itertools.count(0,1)

# Infinite Loop
for x in count:
    print(x)


def count(start=0,step =1):
    n = start
    while True:
        yield n
        n += step