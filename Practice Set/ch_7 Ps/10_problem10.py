#  Write a program to print multiplication table of n using for loops in reversed order.

j = int(input("Enter the number: "))
i = 1
n = 10

while n >= 1:
    print(f"{j} x {n} = {j*n}")
    n -= 1