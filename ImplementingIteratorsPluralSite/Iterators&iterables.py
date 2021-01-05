'''
Iterators decouple Retrieval from the structure

'''

# This is an implicit data structure
# also a representation of a binary tree
expr_tree = ['*','+','-','a','b','c','d']
iterator = iter(expr_tree)
#Remember that the itercallback function __iter__ has to return an iterator.



def _is_perfect_length(sequence ):
    ''' Predicate function: Is true if sequence has a length of 2^n -1, otherwise false'''
    n = len(sequence)
    return ((n+1) & n ==0) and ( n != 0)




class LevelOrderIterator:
    def __init__(self,sequence):
        #Guard clause
        if not _is_perfect_length(sequence):
            raise ValueError (
                f"Sequence of length {len(sequence)} does not represent a perfect binary tree with 2n -1"
            )
        self._index = 0
        self._sequence = sequence

    def __next__(self):
        if self._index > len(self._sequence):
            raise StopIteration
        else:
            result = self._sequence[self._index]
        return result


iterator = LevelOrderIterator(expr_tree)
i = next(iterator)
print(i)
i = next(iterator)
print(i)


predicate_dict = {i: _is_perfect_length(["x"] * i) for i in range(0,32)}
for key,value in predicate_dict.items():
    print(key,value)