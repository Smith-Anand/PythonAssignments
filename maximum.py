#Function to Find Largest of Three Numbers
# Accept three numbers as parameters.
# Return the largest number.

a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
c = int(input("Enter the third number"))

def large(a,b,c):
    if a > b and a > c:
         largest=a
         return largest
    elif b > a and b > c :
         largest = b
         return largest
    else:
        return c

result = large(a,b,c)
print(result)
    
