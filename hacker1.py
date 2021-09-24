import re
text='''4542867'''
regex_alternating_repetitive_digit_pair =re.compile( r"^[1-9]\d{5}\b")
matches=regex_alternating_repetitive_digit_pair.finditer(text)
for match in matches:
    print(match)

