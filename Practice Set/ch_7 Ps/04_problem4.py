# Write a program to find whether a given number is prime or not

n = int(input("Enter a number: "))

for i in range(2, n):
    if n % i == 0:
        print(f"Given number {n} is not prime")
        break
else:
    print(f"Given number {n} is prime")
