#this will work for the real hosts file 
#if you run it as administrator
#add the full path of fake hosts file as the program doesn't throw error when run it

import time
from datetime import datetime as dt

hosts_temp = r"D:\Courses\Summaries\python\Programs\25_app3_web_blocker\hosts"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
websites_list = ["www.facebook.com" ,"m.facebook.com" , "facebook.com"]

first_time = True

while True : 
    if ( 8 < dt.now().hour < 16 ): #working hours... 8am : 4pm
        if(first_time) :
            print("working hours... ")
            first_time = False
            with open (hosts_temp , 'r+') as file :
                content = file.read()
                for website in websites_list:
                    file.write(redirect + " " +  website+"\n")
    else :
         if(not first_time) :
            print("fun hours... ")
            first_time = True
            with open (hosts_temp , 'r+') as file :
                content = file.readlines()
                file.seek(0) #moving cursor to the top of the file
                for line in content:
                    if not any(website in line for website in websites_list):
                        file.write(line)
                file.truncate() #delete anything after the cursor
                                    #which are the old lines !                
    time.sleep(5)
