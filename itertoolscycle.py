import itertools
################ itertools Cycle ##################

# Could be used for a lot of practical applications.
# For example a switch where you want to cycle through a bunch of specific values

listcolors = ['red','blue','green','purple']
switch = ('on','off')




counter = itertools.cycle([1,2,3,4,5])
counter_colors = itertools.cycle(listcolors)
counter_colors = itertools.cycle(switch)

print(next(counter_colors))
print(next(counter_colors))

print(next(counter_colors))
print(next(counter_colors))
print(next(counter_colors))
print(next(counter_colors))
print(next(counter_colors))
print(next(counter_colors))