'''
Algorithm to automate the regula falsi method
1. define the polynomial
2. get the value of epsilon from user (significant digits)
3. solve polynomial for f(x) starting from 0
4. if adjacent values of f(x) are positive and negative, save the values of x0 and x1
5. call the regula falsi method function and input the two values of x
6. return next value of x
7. check if error of the two values of x is less than epsilon. if not, goto step 5
8. print final value of x
'''
#importing the necessary libraries
import math

#defining polynomial function
def f(x):
    return x*math.log10(x)-1.2

#defining regula falsi function
def regulafalsi(xp,xq):
    r = (xp*f(xq)-xq*f(xp))/(f(xq)-f(xp))
    return r

#defining minimum error
error = 0.0005

i=1
while (f(i)*f(i+1)>=0):
    i=i+1
xp=i
xq=i+1
print("Root lies between",xp, "and",xq)
print(f(xp))
print(f(xq))

print(regulafalsi(xp, xq))

