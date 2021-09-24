#prime numbers in a range
prime_list=[]
for z in range(2,9):
    m=0
    for k in range(2,z//2):
        if z%k==0:
            m=1
    if m==0 and z!=4:
        prime_list.append(z)
print(prime_list)

