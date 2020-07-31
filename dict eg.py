dict = {'Name': 'Zara', 'Age': 7, 'pin': 123};
print("Equivalent String : %s" % str (dict))
dict1=dict.copy()
print(dict1)
print(dict['Name'])
print(dict.get('Age'))
dict['Name']='Aswin'
print(dict)
for i in dict:
    print(dict[i])
for x in dict.values():
    print(x)
for a,b in dict.items():
    print(a,b)
del dict['pin']
print(dict)
print(len(dict))
dict.pop('Age')
print(dict)
dict.clear()
print(dict)
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("age", 1965)

print(x)