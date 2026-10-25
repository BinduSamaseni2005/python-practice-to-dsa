"""
#FACTORIAL OF A NUMBER
n=int(input("Enter a number:"))
fact=1
i=1
while i<=n:
    fact=fact*i
    i=i+1
print("Factorial of",n,"is:",fact)
"""

"""
#COUNT THE NUMBER OF DIGITS IN A NUMBER
n=abs(int(input("Enter a number:")))
count=1
while n>0:
    n=n//10
    count+=1
print(count)
"""

"""
#SUM OF DIGITS IN A NUMBER
n=int(input("Enter a number:"))
total=0
while n>0:
    digit=n%10
    total+=digit
    n=n//10
print(total)
"""