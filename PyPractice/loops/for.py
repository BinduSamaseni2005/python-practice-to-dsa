"""
#PRINT NUMBERS FROM 1 TO N
n=int(input("Enter a number: "))
for i in range(1,n+1):
    print(i)
"""

"""
#PRINT NUMBERS FROM N TO 1
n=int(input("Enter a number:"))
for i in range(n,0,-1):
    print(i)
"""

"""
#PRINT ALL EVEN NUMBERS FROM 1 TO N
n=int(input("Enter a number:"))
for i in range(1,n+1):
    if i%2==0:
        print(i)
"""

"""
#SUM OF NUMBERS FROM 1 TO N
n=int(input("Enter a number:"))
sum=0
for i in range(1,n+1):
    sum=sum+i
print("Sum of numbers from 1 to",n,"is:",sum)
"""

"""
#MULTIPLICATION TABLE OF A NUMBER
n=int(input("Enter a number:"))
for i in range(1,11):
    print(n,"x",i,"=",n*i)  
"""

"""
#FACTORIAL OF A NUMBER
n=int(input("Enter a number:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print("Factorial of",n,"is:",fact)
"""

"""
#COUNT THE NUMBER OF DIGITS IN A NUMBER
n=int(input("Enter a number:"))
count=0
for i in str(n):
    count=count+1
print("Number of digits in",n,"is:",count)
"""

"""
#SUM OF DIGITS IN A NUMBER
n=input("Enter a number:")
total=0
for digit in n:
    total+=int(digit)
print(total)
"""