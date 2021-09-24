def excludeItem(item1, item2):

    result=[]  

    for item in item1:                           # iterating over items in the first list
        if item in item2 and item not in result: # checking whether the
                                                 # output value is unique(no duplicate)
            result.append(item)                  # appending such items to the result list

    return result 
