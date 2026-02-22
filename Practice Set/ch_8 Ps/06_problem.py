# Write a python function which converts inches to cms

def inches_to_cms(inches):
    cms = inches * 2.54
    return cms

n = int(input("Enter the Number: "))
print(inches_to_cms(n))