#  Write a python function to print multiplication table of a given number.

def mulit(n):
    for i in range(1, 11):
        print(f"{n} * {i} = {n*i} ")
    
n = int(input("Enter the number: "))
mulit(n)

def mulit(n):
    i = 1
    while (i <= 10):
        print(f"{n} * {i} = {n*i} ")
        i += 1
    
n = int(input("Enter the number: "))
mulit(n)
