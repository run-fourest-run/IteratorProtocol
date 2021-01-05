import itertools
import operator
'''
make an iterator that returns accumulated sums, or accumulated results of other binary functions (specificed
by optional func arg


func arguement: if this is supplied, it should be a function of two arguements. Elements of the input iterable
may be any type that can be accepted as arguements to func.


number of output elements generally matches the number from input iterable

'''



'''equivalant too '''


def accumulate(iterable, func=operator.add, *, initial=None):

    # accumulate([1,2,3,4,5]) -> [1,3,6,10,15]
    # accumulate([1,2,3,4,5],initial=100) ->[100,101,103,106,110,115]
    it = iter(iterable)
    total = initial
    if initial is None:
        try:
            total = next(it)
        except StopIteration:
            return
    yield total
    for element in it:
        total = func(total,element)
        yield total


# amoritze a 5% loan of 1000 with 4 annual payments of 90

cashflows = [1000, -90, -90, -90, -90]
amortized_cashflows = list(accumulate(cashflows, lambda bal, pmt: bal*1.05 + pmt))
for x in amortized_cashflows:
    print(x)


'''testing itertools '''

itertest = itertools.accumulate(cashflows)
for x in itertest:
    pass

itertest2 = itertools.accumulate(cashflows)


cashflows = [1000, -90, -100, -90, -90]
test_minimum_cashflows = list(accumulate(cashflows,min))
print('the elements of the list should equal: [1000,-90,-100,-100,-100]... it equals{}'.format(test_minimum_cashflows))


test_lambda = list(accumulate(cashflows, lambda bal,pmt: bal *1.07 + pmt))

