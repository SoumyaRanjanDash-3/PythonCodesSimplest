#calculaton of mean,variance,standard deviation
from math import *
print('''Enter the set by sq brackets "[e,l,e,m,e,n,t,s]" separated by comma''')
l=eval(input("Elements of set : "))

mean_sum=0
for i in l:
    mean_sum+=i
mean=mean_sum/len(l)

var_in=0
for i in l:
    var_in=var_in+((i-mean)**2)
var=var_in / (len(l)-1)



print("The entered set is" ,l )
print("mean : ",mean)
print("Variance :" ,var)
print("Standard deviation: ",sqrt(var))
