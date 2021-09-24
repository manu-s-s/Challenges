# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
# The string will only contain lowercase characters a-z
import sys
text=input('enter text: ')
if text==text[::-1]:
    print('palindrome')
    sys.exit(0)
for i in range(len(text)):
    k=text[0:i]+text[i+1:]
    if k==k[::-1]:
        print('palindrome')
        sys.exit(0)
print('not palindrome')
