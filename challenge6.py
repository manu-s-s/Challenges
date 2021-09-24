# Given an array of integers, determine whether the array is monotonic or not
def monotonic(array):
    i=0
    j=0
    while i+1<len(array):
        if array[i]<=array[i+1]:
            i+=1
        else:
            break
    while j+1<len(array):
        if array[j]>=array[j+1]:
            j+=1
        else:
            break
    if (j+1==len(array)) or (i+1==len(array)):
        print("monotonic")
arr=[]
n=int(input('Enter number of elements'))
i=0
for i in range(n):
    arr.append(input('>>> '))
    i+=1
monotonic(arr)

    

