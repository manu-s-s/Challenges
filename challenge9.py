#Given two sentences, return an array that has the words that appear in one sentence and not
#the other and an array with the words in common. 
def match(sentence1, sentence2):
    sentence2=sentence2.split()
    sentence1=sentence1.split()
    common=[]
    w_in_1_not_in_2=[]
    w_in_2_not_in_1=[]

    for word in sentence1:
        if word in sentence2:
            common.append(word)
        else:
            w_in_1_not_in_2.append(word)
    for word in sentence2:
        if word not in common:
            w_in_2_not_in_1.append(word)
    print('common words',common)
    print('w_in_1_not_in_2',w_in_1_not_in_2)
    print('w_in_2_not_in_1',w_in_2_not_in_1)
sentence1 = 'We are really pleased to meet you in our city'
sentence2 = 'The city was hit by a really heavy storm'
match(sentence1, sentence2)
