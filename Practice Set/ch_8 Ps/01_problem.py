# Write a program using functions to find greatest of three numbers.

def num(a, b, c):
    if a>b and a>c:
        print(f"Greatest Number is {a}")
    elif b>a and b>c:
        print(f"Greatest Number is {b}")
    elif c>a and c>b:
        print(f"Greatest Number is {c}")

a = int(input("Enter 1st Number: "))
b = int(input("Enter 2nd Number: "))
c = int(input("Enter 3rd Number: "))
num(a, b, c)
