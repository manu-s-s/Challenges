incd = ['a', 'b', 'b', 'c','d','e','f','c','c']
w = ['a', 'b' ,'d']
indeces=[]
for i, x in enumerate(incd):
    if x in w:
        indeces.append(i)

print(indeces)