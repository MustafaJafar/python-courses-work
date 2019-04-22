import os 
import pandas 

print(os.listdir() , "\n")

df_csv = pandas.read_csv("supermarkets.csv") #header is true by defult ,to disable it : header = None
df_csv = df_csv.set_index("ID")
print(df_csv , "\n") 

df_json = pandas.read_json("supermarkets.json")#the columns have not in the same order
df_json = df_json.set_index("ID")
print(df_json , "\n")

#excel needs : 
#       pip install xlrd
#df_excel = pandas.read_excel("supermarkets.xlsx" , sheet_name = 0)#you should specify the sheet number
#df_excel = df_excel.set_index("ID")
#print(df_excel , "\n")

df_comma =  pandas.read_csv("supermarkets-commas.txt")
df_comma = df_comma.set_index("ID")
print (df_comma , "\n")

df_semicol =  pandas.read_csv("supermarkets-semi-colons.txt" , sep = ";")
df_semicol = df_semicol.set_index("ID")
print (df_semicol , "\n")

#also pandas can read a file from internet : ex : https://pythonhow.com/supermarkets.csv

#df_csv_internet = pandas.read_csv("https://pythonhow.com/supermarkets.csv")
#df_csv_internet = df_csv_internet.set_index("ID")
#print (df_csv_internet , "\n")

#df_json_internet = pandas.read_json("https://pythonhow.com/supermarkets.json")
#df_json_internet = df_json_internet.set_index("ID")
#print (df_json_internet , "\n")