
# For a given sentence, return the average word length. 
# Note: Remember to remove punctuation first.
import re
def word_length(sentence):
    pattern=re.compile(r'[a-zA-Z]+')
    matches=pattern.findall(sentence)
    print(len(matches))
sentence='Hi all, my name is Tom9...I am originally from Australia.'
word_length(sentence)