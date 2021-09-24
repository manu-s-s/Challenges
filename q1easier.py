def check_condition(number):
    for i in range(0,len(number),2):
        if int(number[i])%2!=0:
            return False
    prime_list=[]
    for z in range(2,9):
        m=0
        for k in range(2,z//2):
            if z%k==0:
                m=1
        if m==0 and z!=4:
            prime_list.append(z)   #creating a list of single digit prime numbers 
    for j in range(1,len(number),2):
        if int(number[j]) not in prime_list:
            return False
    return True
print(check_condition('2742'))
