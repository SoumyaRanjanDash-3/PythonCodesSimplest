#from math import *
#print(lcm(33,55))
def hcfnaive(a,b):
    if(b==0):
        return a
    else:
        return hcfnaive(b,a%b)

def lcmnaive(a,b):
    if (a==0 or b ==0):
        return a or b
    else:
        return a*b//hcfnaive(a,b)


a,b=[int(x) for x in input("Enter 2 nos:").split(",")]


print ("The gcd of {} and {} is : ".format(a,b),end="")
print (hcfnaive(a,b))
print ("The lcm of {} and {} is : ".format(a,b),end="")
print(lcmnaive(a,b))
