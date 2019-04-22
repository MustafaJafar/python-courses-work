from datetime import datetime

def read_files(name , num) :
    files_result = []
    for n in range(num) :
        full_file_name = name + str(n+1) +".txt" 
        myfile = open(full_file_name)
        mylist = myfile.read()
        myfile.close()
        mylist = mylist.splitlines()
        files_result.extend(mylist)
        #print(files_result)
    return files_result


content_list = read_files("15_merge_files\\file" , 3) #this works as I already know file names 
                                                      #bu using glob2 is mor general way

content = '\n'.join(content_list)

with open( "15_merge_files\\" + datetime.now().strftime("%Y-%m-%d-%H-%M-%S") +".txt"  ,"w") as myfile : #with close the file for you
    myfile.write(content)

'''
#solution from course :

import glob2
from datetime import datetime
     
filenames = glob2.glob("*.txt")
with open(datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt", 'w') as file:
    for filename in filenames:       
        with open(filename, "r") as f:
            file.write(f.read() + "\n")

'''
