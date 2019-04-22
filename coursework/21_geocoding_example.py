#pass address to a service and get longitude and latitude cooredinates
    #this means geo coding
from geopy.geocoders import ArcGIS
import pandas

nom = ArcGIS()  

n = nom.geocode("3995 23rd st, San Francisco, CA  94114") #(road name , city , zip code , country)
print(n) #it will print none if you used wrong address

df = pandas.read_csv(r"20_pandas\supermarkets.csv") 
df["Full Address"] = df["Address"] + ", " + df["City"]+", " + df["State"]+ ", "+df["Country"]

print(df , "\n")
 
df["Coordinates"] = df["Full Address"].apply(nom.geocode) #apply a method for each column

print(df.Coordinates[0].latitude)
 
df["Latitude"] = df["Coordinates"].apply(lambda x : x.latitude if x != None else None)
df["Longitude"] = df["Coordinates"].apply(lambda x : x.longitude if x != None else None)

print(df , "\n")