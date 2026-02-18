Marks = {

  "rahul" : 100,
  "Jay"   : 99,
  "Shrey" : 33,
  "list"  : [1,5,889,2],
        0 : "joy",
  }

# print(Marks["rahul"])
# print(Marks["list"])

print(Marks.items()) # print all { key value } pairs
print(Marks.keys()) # keys print kar ka dega like 100, 99 , 33

Marks.update({"Jay": 89})
print(Marks["Jay"])

print(Marks.get('Rahul1')) #Return the none
# print(Marks('Rahul1'))
# Will show error and noty run the code
