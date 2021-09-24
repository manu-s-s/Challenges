import itertools
from functools import reduce
from math import gcd
def non_coprime_subarrays (a, n):
    # Your Code Goes Here
    count=0
    
    for L in range(1,n+1):
        for subset in itertools.combinations(a,L):
            
            if reduce(gcd,subset)>1:

                count+=1
    return count

n = int(input())
a = input()
a=[int(x) for x in a.split()]
print(a)
print(non_coprime_subarrays(a,n))
