#!/usr/bin/env python
# coding: utf-8

# In[5]:


#you can grab each page manully 
#or better : figure out the rule of how page i=url changes 
import requests , pandas
from bs4 import BeautifulSoup

#get web page #00 == first page , 10 == second , 20 == third
base_url = "https://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/#t=0&s="
#list to hold the data
l = []
#you can set the range manully or you can set number of pages automatically 
#page_nr = soup.find_all("a" , {"class" : "Page"})[-1].text #this will return 3
#page_nr = int(page_nr) * 10 #will = 30

for pages in range(0 , 30 , 10) : #replace 30 with page_nr
    req = requests.get(base_url+str(pages)+".html")
    #load content
    cont = req.content

    soup = BeautifulSoup(cont , "html.parser")
    
    all = soup.find_all("div" , {"class" : "propertyRow"})
    
    
    
    for item in all : 
        d = {}

        d["Address"] = item.find_all("span" , {"class" : "propAddressCollapse"})[0].text
        d["Price"] = item.find_all("h4" , {"class" : "propPrice"})[0].text.replace("\n" ,"")

        try :
            d["Locality"] = item.find_all("span" , {"class" : "propAddressCollapse"})[1].text
        except : 
            d["Locality"] = None
            
        try :
            d["Beds"] = item.find_all("span" , {"class" : "infoBed"})[0].text
        except : 
            d["Beds"]= None
        try :
            d["Area"] = None
        except : 
            d["Area"] = item.find_all("span" , {"class" : "infoSqft"})[0].text
        try : 
            d["Full Baths"] = item.find_all("span" , {"class" : "infoValueFullBath"})[0].text
        except :
            d["Full Baths"] = None
        try : 
            d["Half Baths"] = item.find_all("span" , {"class" : "infoValueHalfBath"})[0].text
        except :
            d["Half Baths"] = None

        for column_group in item.find_all("div" , {"class" : "columnGroup"}) : 
            for feature_group , feature_name in zip (column_group.find_all("span" , {"class" : "featureGroup"}) ,column_group.find_all("span" , {"class" : "featureName"}) ) :
                if ("Lot Size" in feature_group.text) : 
                    d["Lot Size"] = feature_name.text
        l.append(d)
    
df = pandas.DataFrame(l , columns =['Address' , 'Locality' , 'Area' ,'Lot Size', 'Price' ,'Beds', 'Full Baths', 'Half Baths' ])
df.to_csv("2_Output.csv")
df


# In[ ]:




