print("QUESTION_1")
print("CONVERT TO C deg TO F deg")
print("--------------------------")
C =float(input("Enter the temperature :"))
F =(C*9/5)+32
print("Temperature in Fahrenheit :",F)
print("                                                ")
print("QUESTION_2")
print("EVEN OR ODD CHECKER")
print("-------------------")
N =int(input("Enter the value :"))
if N%2==0:
    print("Value is even")
else:
    print("Value is odd")
print("                                                ")
print("QUESTION_3")
print("LEAP YEAR CHECKER")
print("-------------------")
y =int(input("Enter the year :"))
if y%400==0:
    print("leap year")
elif y%100==0:
    print("not leap year")
elif y%4==0:
    print("leap year")
else:
    print("not a leap year")
print("                                                ")
print("QUESTION_4")
print("AREA AND PRIMETER OF CIRCLE")
r = int(input("Enter radius of the circle :"))
import math
a = math.pi*r*r
p = 2*math.pi*r
print("Area of circle :",a)
print("Perimeter of the circle :",p)
print("                                                ")
print("QUESTION_5")
n =int(input("Enter the value :"))
if n<0:
    print("factorial is not defined for negative numbers")
else:
    f = 1
    for i in range(1,n+1):
        f *= i
        print(f)
#if n < 0: checks for negative numbers; factorial isn’t defined.
#f = 1: initializes the product.
#for i in range(1, n+1): f *= i multiplies all numbers from 1 to n iteratively."""
    








    
    
    

    
    




