# Write a recursive function to calculate the sum of first n natural numbers.

""""

sum(1) = 1 
sum(2) = 1 + 2
sum(3) = 1 + 2 + 3
sum(4) = 1 + 2 + 3 + 4
sum(n) = 1 + 2 + 3 + ... + n
sum(n) = n + sum(n-1)

"""
def sum(n):
    if n == 0:
        return 1
    else:
        return n + sum(n-1)

a = int(input("Enter the Number: "))    
print(sum(a))