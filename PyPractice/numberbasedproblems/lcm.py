a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
lcm = max(a,b)
while True:
    if lcm % a == 0 and lcm % b == 0:
        break
    lcm += 1
print("The LCM of", a, "and", b, "is:", lcm)

#2ND WAY
"""
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
x=a
y=b
while y!=0:
    remainder = x % y
    x = y
    y = remainder
gcd = x
lcm = (a*b)//gcd
print("The LCM is:", lcm)
"""