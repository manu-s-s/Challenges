def process(paragraph):
    paragraph=paragraph.split('.')
    i=0
    while i<len(paragraph):
        paragraph[i]=paragraph[i].split()
        j=0
        paragraph[i].reverse()
        while j<len(paragraph[i]):
            if '#' not in paragraph[i][j]:
                j+=1
                continue
            k=0
            while k<len(paragraph[i][j]):
                if paragraph[i][j][k]=='#':
                    paragraph[i][j]=paragraph[i][j].replace('#',paragraph[i][j][len(paragraph[i][j])-1-k],1)
                k+=1
            if paragraph[i][j] != paragraph[i][j][::-1]:
                paragraph[i][j]='@'*len(paragraph[i][j])
            j+=1
        paragraph[i]=' '.join(paragraph[i])
        i+=1
    return ('. '.join(paragraph)).strip()
paragraph="#al#yalam ddis our    mother tong#e. It is a langua#e spo#en in the Indian state of kerala. m#dam ha#nah teaches Malayalam. neve# is a #tudent of hannah."
print(process(paragraph))