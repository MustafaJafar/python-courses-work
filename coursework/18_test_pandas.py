import pandas #library for data structures and analysis

#data structure : putting data in a certain form "Structure"
#data analysis  : to get information from data 

df1 = pandas.DataFrame([[2,4,6],[10,20,30]]) #create a dataframe

print (df1)
print()

df1 = pandas.DataFrame([[2,4,6],[10,20,30]] , columns = ["Price" , "Age","Value"])

print (df1)
print()

df1 = pandas.DataFrame([[2,4,6],[10,20,30]] , columns = ["Price" , "Age","Value"] , index = ["First" , "Second"])

print (df1)
print()

df2 = pandas.DataFrame([{"Name" : "Jhon"},{"Name" : "Jack"}])

print (df2)
print()

df2 = pandas.DataFrame([{"Name" : "Jhon" , "Surname" : "Jhons"},{"Name" : "Jack"}])

print (df2)
print()

#to make some data analysis : 
print (df1.mean()) 

#pandas dataframe : made of series
#pandas series : a column of data