import itertools

# usually used to pass in a stream of constants to a function like map or zip 


repeat = itertools.repeat(50, times=50)


'''
for x in repeat:
    string = "This is my message {} times".format(x)
    print(string)
'''

squares = map(pow,range(10) ,itertools.repeat(2))
print(list(squares))
