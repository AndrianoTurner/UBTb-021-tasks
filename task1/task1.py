import itertools

def cartesian_product(left,right):
    return itertools.product(left,right)


res = list(cartesian_product([1,2,3],[4,5,6]))

print(res)