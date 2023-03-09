# root.py
# Author Niall Horgan
# Get the square root of a number using Newtons method



num = float(input("Please enter a positive number: "))
    
guess = num / 2.0

while abs(num - guess ** 2) > .0001:
    guess = 0.5 *(guess + num / guess)
print (guess)
    







