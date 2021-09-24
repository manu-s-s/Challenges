def move_zero(array):
    i=0
    for item in array:
        if item==0:
            array.remove(item)
            array.append(0)
            i+=1   
    print(array)
move_zero([1,0,2,3,0,1221,22,2])
