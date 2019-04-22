myfile = open("01_sample.txt")
myfile_2 = open("07_files//01_sample.txt")
myfile_3 = open("07_fruits.txt")

content = myfile.read()
content_2 = myfile_2.read()
content_3 = myfile_3.read()
#myfile.seek(0) #move cursor to the top of the file
myfile.close()
myfile_2.close()
myfile_3.close()

print(content)
print(content_2)
print(content_3)

#processing content of files : 
content_list = content.splitlines() #make each line as an item of the list

print(content_list)