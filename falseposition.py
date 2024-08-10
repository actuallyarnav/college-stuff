'''
Algorithm to automate the regula falsi method
1. define the polynomial (done)
2. get the value of epsilon from user (significant digits) (done)
3. solve polynomial for f(x) starting from 0 (done)
4. if adjacent values of f(x) are positive and negative, save the values of x0 and x1 (done as xp and xq)
5. call the regula falsi method function and input the two values of x (done)
6. return next value of x (done)
7. check if error of the two values of x is less than epsilon. if not, goto step 5 (done)
8. print final value of x (done)
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
print("predefined function is x**3-5*x+3")

#defining minimum error
decimalplaces = eval(input("How many decimal places should the answer be correct to?: "))
try:
    decimalplaces = int(decimalplaces) #converts input to int type
except ValueError:
    print("Invalid input! Please enter a valid integer.") #if it can't, it throws up an error
error = (1/2)*(10**(- decimalplaces))

#defining significant digits
sd = input("How many significant digits should the answer contain?: ")
try:
    sd = int(sd)
except ValueError:
    print("Invalid input! Please enter a valid integer.")
i=1
while (f(i)*f(i+1)>=0):
    i=i+1
xp=i
xq=i+1
#perform approximations to find root
while(abs(xp-xq)>error): #works until 2 adjacent roots have a difference less than the error
    xtemp=regulafalsi(xp,xq) #temp var to store a value of x, before assigning it to xp or xq
    if (f(xtemp)*f(xq)<0):
        xp=xtemp #changes the lower limit
    elif(f(xtemp)*f(xp)<0):
        xq=xtemp #changes the upper limit

answer = f"{xq:.{sd}g}" #formatting the result to contain preferred amount of significant digits

print("Approximate root is", answer)

#work to do:
#find a way to input a function, instead of predefining it in the code
