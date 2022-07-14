from typing import Type


exampleDict = {1: "Subhash", 2: "Lavanya", 3: "Varun", 4: "Krishna Vamshi"}
print(type(exampleDict))
print(exampleDict)
nestedDict = {"name": {"first": "varun", "last": "aaruru"},
              "age": 28, "profession": "student"}
print(nestedDict)
d1 = {}
d1[0] = "welcome"
d1[1] = ("tuple inside", "dictionary")
d1["name"] = "varun"
print(d1)
d1["name"] = {"first": "varun", "last": "aaruru"}
print(d1)
print(d1["name"]["last"])
d1.pop(0)  # to delete keyand value at given index
print(d1)
print(d1.keys)
print(d1.values)
d1.clear
print(d1)
key = {1, 2, 3, 4}
valu = "varun"
print(dict.fromkeys(key, valu))
