import pandas as pd

df = pd.read_csv("supermarkets.csv") #header is true by defult ,to disable it : header = None
df = df.set_index("ID")
print(df , "\n") 

#label indexing loc[first index : last index , first column : other column  ]
#--------------loc------------
print(df.loc["1" : "3"] , "\n")

print(df.loc["1" : "3" , "City" : "Name"] , "\n")

print(list(df.loc[: , "Name"]) , "\n")
print(df["Name"] , "\n")

print(df.index , "\n")

print(df.loc["1" : "1",  :] , "\n" )

print(df.loc[1 , :] , "\n")

print(df.loc[1] , "\n")

print(df.loc[1] , "\n")

print(df.loc["1":"1" , "Name"] , "\n")

print(df.loc[1 , "Name"] , "\n")

#-----------iloc----------
print(df.iloc[1:3, 1:3] , "\n")
#print(df.loc[ ["1"], "Country"]) #all country column converted to list
#-----------ix------------combined indexing
print(df.ix[1 , "Name"] , "\n")
print(df.ix[1 , 4] , "\n")