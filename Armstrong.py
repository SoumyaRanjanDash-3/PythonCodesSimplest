#Addition of cube of digit of number is equalto the number
def armstrong(n):
from math import *
n=int(input("Enter a number: "))
sum=0
temp=n
while temp>0:
    digit=temp%10
    sum += digit **3
    temp//=10

if n==sum:
    print("The entered number is an armstrong number")
else:
    print("SORRY !!! The entered number is not an armstrong number")
return
