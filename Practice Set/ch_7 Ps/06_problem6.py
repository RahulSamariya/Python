# Write a program to calculate the factorial of a given number using for loop.

n = int(input("Number likho: "))
i = 1
product = 1

while i <= n:
    product *= i
    i += 1

print(f"{n} ka factorial yeh hai {product}")