# Write a Python program to do arithmetical operations addition and division.
def add(a,b):
    c = a + b
    print(c)
    
def multiply(a,b):
    c = a * b
    print(c)
    
def substract(a,b):
    c = a-b
    print(c)

def divide(a,b):
    if b != 0:
        c = a / b
        print(c)
    else:
        print("Cannot divide by zero")   

add(2,3)
multiply(2,3)
substract(2,3)
divide(2,3)