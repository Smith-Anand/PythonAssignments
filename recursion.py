#Function to Calculate Factorial (Using Recursion)
# Implement factorial using:
#o Normal function
#o Recursive function

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

n = int(input("Enter the number of which you want the factorial"))
result= factorial(n)
print(result)
