# ref 
# https://stackoverflow.com/questions/209840/convert-two-lists-into-a-dictionary-in-python

import json

keys = ['a', 'b', 'c']
values = [1, 2, 3]
dictionary = dict(zip(keys, values))

print(dictionary , type(dictionary))

y = json.dumps(dictionary) 

print(y , type(y))


keys = ['a', 'b', 'c']
values = [(1,1), (2,2), (3,3)]
dictionary = dict(zip(keys, values))

print(dictionary , type(dictionary))

y = json.dumps(dictionary) 

print(y , type(y))

x = json.loads(y)

print(x , type(x))
print(x["a"] , type(x["a"]))



# read file
with open('0_example.json' , 'r') as myfile:
    data=myfile.read().replace('\n', '')

# parse file
obj = json.loads(data)
print(obj , type(obj))
