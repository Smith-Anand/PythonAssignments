a=int(input("Enter the first number"))
b= int(input("Enter the second number"))

def add(a,b):
    return a+b
def mul(a,b):
    return a*b
def calc(func, a,b):
    return func(a,b)

result= calc(add,a,b)
print(result)
    
