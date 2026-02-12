#4. Function with Default Arguments
# Write a function to calculate simple interest.
# Keep rate default as 5%.

p=int(input("Enter the principal amount"))
t=int(input("Enter the time period"))

def simple(p,t,r=5):
    return (p*r*t)/100

result = simple(p,t)
print(result)
