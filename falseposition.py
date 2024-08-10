'''
Algorithm to automate the regula falsi method
1. define the polynomial (done)
2. get the value of epsilon from user (significant digits) (predefined but can do)
3. solve polynomial for f(x) starting from 0 (done)
4. if adjacent values of f(x) are positive and negative, save the values of x0 and x1 (done as xp and xq)
5. call the regula falsi method function and input the two values of x (done)
6. return next value of x (done)
7. check if error of the two values of x is less than epsilon. if not, goto step 5
8. print final value of x
'''

#importing the necessary libraries
import math

#defining polynomial function
def f(x):
    return x**3-5*x+3
#defining regula falsi function
def regulafalsi(xp,xq):
    r = (xp*f(xq)-xq*f(xp))/(f(xq)-f(xp)) #xp is smaller value, xq is greater value
    return r

#defining minimum error
error = eval(input("Enter the error (eg. 0.0005): "))

i=1
while (f(i)*f(i+1)>=0):
    i=i+1
xp=i
xq=i+1
print("Root lies between",xp, "and",xq)
#print(f(xp))
#print(f(xq))
#print(regulafalsi(xp, xq))
while(abs(xp-xq)>error):
    xtemp=regulafalsi(xp,xq) #temp var to store a value of x, before assigning it to xp or xq
    if (f(xtemp)*f(xq)<0):
        xp=xtemp #changes the lower limit
    elif(f(xtemp)*f(xp)<0):
        xq=xtemp #changes the upper limit

print("Approximate root is", xq)
