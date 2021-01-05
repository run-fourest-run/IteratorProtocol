import itertools


# Combinations are all the different ways that you can group a certain number of items where the order does not matter
# Permutations are all the different ways that you can group a certain number of items where the order does  matter


letters = ['a','b','c','d']
numbers = [0,1,2,3,4,5]
names = ["alexander","spencer","Jared","Allen"]

result = itertools.combinations(names,3)
for item in result:
    print(item)