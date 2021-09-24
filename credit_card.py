import re
def credit_card_check(number):
    number=re.sub(r'^(\d{4})-?(\d{4})-?(\d{4})-?(\d{4})$',r'\1\2\3\4' ,number)
    if re.search(r'^(([456])(?!\2{3}))((\d)(?!\4{3})){14}[0-9]$',number):
        return 'Valid'
    else:
        return 'Invalid'
n=int(input())
a=[]
for i in range(n):
    a.append(input())
for i in range(n):
    print(credit_card_check(a[i]))
