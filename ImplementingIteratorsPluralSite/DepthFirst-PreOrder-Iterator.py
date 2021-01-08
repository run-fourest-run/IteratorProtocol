'''
depth first in-order tree traversal:

'''



# in Module helper functions

def _in_

class InOrderIterator:

    def __init__(self,sequence):
        if not _is_perfect_length(sequence):
            raise ValueError(f"sequence of length {len(sequence)} does not represent a perfect binary tree")
        self._sequence = sequence
        self._stack = []
        self._index = 0


    def __next__(self):
        if (len(self._stack == 0) and (self._index >= len(self._sequence)):
            raise StopIteration

        while self._index < len(self.sequence):
            self._stack.append(self._index)
            self._index = _left_child(self._index)

        index = self._stack.pop()
        result = self._sequence[index]
        self._index = _right_child(index)
        return result

    def __iter__(self):
        return self



'''These are module-level helper functions'''


def _is_perfect_length(sequence):
    n = len(sequence)
    return ((n +1) & n==0) and  (n != 0)

def _left_child(index):
    pass

def _right_child(index):
    pass
