a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
gcd = 1
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        gcd = i
print("The GCD of", a, "and", b, "is:", gcd)


"""
#EUCLIDIEAN WAY
#2ND WAY
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
while b!=0:
    remainder = a % b
    a = b
    b = remainder
print("The GCD is:", a)
"""