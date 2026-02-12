#1. Write a Function to Perform Arithmetic Operations
# Create separate functions for addition,
#subtraction, multiplication, and division.
# Call them based on user input.

print("Choose 1 for addition, choose 2 for subtraction, choose 3 for division")
choice = int(input())
a=int(input("Enter the first number"))
b=int(input("Enter the second number"))

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def div(a,b):
    if a==0:
        print("Cannot divide by zero")
    else :
        return a/b

if choice == 1:
    result=add(a,b)
    
elif choice == 2:
    result=sub(a,b)

elif choice == 3:
    result=div(a,b)

print(result)
