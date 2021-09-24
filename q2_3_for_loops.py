def process(paragraph):
    paragraph=paragraph.split('.')
    para=[]
    for sentence in paragraph:
        sentence=sentence.split()
        sentence.reverse()
        sent=[]
        for word in sentence:
            if '#' in word:
                i=0
                while i<len(word):
                    if word[i]=='#':
                        word=word.replace('#',word[len(word)-1-i],1)
                    i+=1
                if word!=word[::-1]:
                    word='@'*len(word)
                i+=1
            sent.append(word)
        para.append(' '.join(sent))
    return(('. '.join(para)).strip()) #End space is removed. If strip is applied, total characters 148 instead of 149.
paragraph = "#al#yalam is our mother tong#e. It is a langua#e spo#en in the Indian state of kerala. m#dam ha#nah teaches Malayalam. neve# is a #tudent of hannah."   
print(process(paragraph))