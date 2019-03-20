import sys
from matplotlib.pyplot import *

print("Task 1")

for x in range(56,101):
    print("X: ", x)
    print("Y: ", 2*x**2+2*x+2)
    print("-"*20)

print("Task 2")

def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)

print("Insert your value: ")
value = int(input())
print("Factorial: ", factorial(value))

print("-"*20)

print("Task 3")

z = [5, 3, 8, 2, 1, 8]

def min(x):
    minimum = x[0]
    minimum_index=[]
    minimum_index.append(0)

    for i in range(len(x)):
        if x[i] < minimum:
            minimum = x[i]
            minimum_index = i
    
    return minimum, minimum_index

print("Min: ", min(z))
print("Min: ", min(z)[0], " index: ", min(z)[1])

print("-"*20)
print("Task 4")

# Ask user for range
incorrect_input = True
while(incorrect_input):
    print("Give range for plot of f(x)=x^2")
    print("From: ")
    x1 = int(input())
    print("To: ")
    x2 = int(input())
    print("X1: ", x1, " X2: ", x2)
    if(x1 < x2):
        incorrect_input = False



# Create empty list
y_axis=[]
x_axis=[]


# Generate points for function f(x) = x^2
for i in range(x1,x2+1):
    y_axis.append(i**2)
    x_axis.append(i)

plot(x_axis,y_axis)
show()
