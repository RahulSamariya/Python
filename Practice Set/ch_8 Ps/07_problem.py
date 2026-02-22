# Write a python function to remove a given word from a list ad strip it at the same time.

def rem(l, word):
    n = []
    for i in l:
        if not (i == word):
            n.append(i.strip(word))
    return n


l = ["Rahul", "Harry", "Neev", "an", "Rohan"]
print(rem(l, "Harry"))
