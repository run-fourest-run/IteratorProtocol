import itertools

############## Counter function #############
# Infinite loop
counter = itertools.count()
counter_starts = itertools.count(start=5)
counter_step = itertools.count(step=3)

# calling __next__ will return values from 1 -> infinite
# print(next(counter))
# print(next(counter))
# print(next(counter))


# Good for assigning an index to a list
data = [100,200,300,400,500,600,1000]


#Zip function takes two iterables and connects them.
# Because the list is variably lengthed this is good for doing this I guess
daily_data = list(zip(counter,data))
daily_data_step = list(zip(counter_step,data))


############## Zip_Longest function #############

counter_step = itertools.count(step=5)
# daily_data = list(zip(itertools.zip_longest(range(3),data)))



counter_step = itertools.count(step=100,start=100)
daily_data = list(itertools.zip_longest(range(100),data))
print(daily_data)








