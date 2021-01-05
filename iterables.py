'''Iterator is an object that represents a stream of data. Repeaded calls to the iterators __next__ method
return successive items in the stream. When no objects are found a StopIteration Exception is raised.'''



#Iterable
nums = [1,2,3,4,5,6,7,8,9,10]

## an object needs the __iter__ method to be an iterable

#for loop calling iter on our object returning an iterator that we can loop over
for num in nums:
    pass
    # print(num)

#Iterators
# Object with a state so that it remembers where it is during iteration. They also know how to get their
# next value with a __next__ dunder method.

#Iterator
# Remember calling the __iter__ method on an iterable returns an iterator.
i_nums = iter(nums)
i_nums = nums.__iter__()


#dir prints all of the dunder methods
# you can see the nums list as an iter dunder. So it's an iterable
for x in dir(i_nums):
   #  print(x)
    pass



# Iterators are objects that remember their state. If we run the __next__ method we should get the next value
# in the iterable. A StopIteration exception is raised at the end. 

print(next(i_nums))
print(next(i_nums))
print(next(i_nums))
print(next(i_nums))
print(next(i_nums))
print(next(i_nums))
print(next(i_nums))
print(next(i_nums))
print(next(i_nums))
print(next(i_nums))
print(next(i_nums))
print(next(i_nums))
