"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

"""
def list_check(k,number_list):
    i=0
    while i<len(number_list):
        j=i+1
        while j<len(number_list):
            if number_list[i]+number_list[j]==k:
                return True
            j+=1
        i+=1
print(list_check(10,[11,15,3,7]))
