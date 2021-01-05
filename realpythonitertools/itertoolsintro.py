'''itertools is a module that implements a number of iterator building blocks. Functions in itertools operate
on iterators to produce more complex iterators'''

test_list_0 = [95000,95000,95000,95000]
test_list_1 = [117000,117000,121000,120000]
test_list_2 = ['alex','joe','anthony','david']

'''zip example'''

def see_zip_type():
    return_iterator = zip(test_list_1,test_list_2)
    print(return_iterator)

print(list(zip(test_list_1,test_list_0)))
print (list(map(len,test_list_2)))
print (list(map(sum,zip(test_list_1,test_list_0))))