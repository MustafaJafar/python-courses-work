import pandas as pd

df = pd.read_csv("supermarkets.csv") #header is true by defult ,to disable it : header = None
df = df.set_index("ID")
print(df , "\n")

#remove 
df_new = df.drop("City" , 1) # 1 : column , 0 : rows
print(df_new, "\n")

df_new = df_new.drop(1 , 0) # 1 : column , 0 : rows
print(df_new, "\n")

df_new = df_new.drop(df_new.index[2:4] , 0) # 1 : column , 0 : rows
print(df_new, "\n")

df_new = df_new.drop(df_new.columns[0:3] , 1) # 1 : column , 0 : rows
print(df_new, "\n")

#add column
df["Continent"] = df.shape[0]*["North America"] #list with length of df.index (rows)
                                                #df.shape returns (rows , cols)
print (df , "\n")                               

#update column
df["Continent"] = df["Country"] + "," + "North America"
print (df , "\n")                               

#add row 
df_t = df.T #T = transposed
df_t[7] = ["My Address" , "My City", "My State","My Country" ,  "My Shop" , 10 , "My Continent"]
df = df_t.T
print(df , "\n")
