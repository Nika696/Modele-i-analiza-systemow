import sys

print("Task 1")

for x in range(56,101):
    print("X: ", x)
    print("Y: ", 2*x**2+2*x)
    print("-"*20)

print("Task 2")

def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)

print("Insert your value: ")
y = int(input())
print("Factorial: ", factorial(y))

print("-"*20)

print("Task 3")

z = [5, 3, 8, 2, 1, 8]

def min(x):
    minimum = 999999999999999999
    minimum_index = 0
    for i in range(len(x)):
        if x[i] < minimum:
            minimum = x[i]
            minimum_index = i
    
    return minimum, minimum_index

print("Min: ", min(z))