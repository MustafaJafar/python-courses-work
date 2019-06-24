# ref : 
# https://www.w3schools.com/python/python_json.asp

'''
what is JSON ? 
  JSON is a syntax for storing and exchanging data.
  JSON is text , written with JavaScript object notation.
    "JSON : text , JS notation"
'''

import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
print(x , type(x))

# parse x: string JSONly formated into dictionary
y = json.loads(x)

# the result is a Python dictionary:
print(y , type(y)) 


x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

print(x , type(x))

# convert dictionary into JSON string :
y = json.dumps(x) 

print(y , type(y))
