"""Can you change the values inside a list which is contained in set S?
s = {8, 7, 12, "Harry", [1,2]}"""

s = {8, 7, 12, "Harry", [1,2]}

s[4][0] = 10

# set are imutable and we cannot have list as elemnets in the set 
# yeh chez unshasble hoti hai isliye error aayega