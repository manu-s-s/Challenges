'''Given an integer, n, positive number from 1 to 100 , perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird Input Format'''
def weird(number):
    if number%2!=0:
        print('weird')
    elif number%2==0:
        if number in range(2,6):
            print('not weird')
        if number in range(6,21):
            print('weird')
        if number>20:
            print('not weird')
