# Given an array containing None values fill in the None values with most recent 
# non None value in the array
def fill(array):
    i=0
    while i+1<len(array):
        if array[i+1]==None:
            array[i+1]=array[i]
        i+=1
    print(array)
fill([1,None,2,None,4,5])


