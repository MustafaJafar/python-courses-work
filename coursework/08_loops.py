myfile = open("01_sample.txt")
content = myfile.read()
myfile.close()

for item in content :
    print(item)

content_list = content.splitlines() #make each line as an item of the list

for item in content_list :
    print(item)

print()

mylist = [1, 2, 3, 4, 5] 
for item in mylist:
    if item > 2:
        print(item)

myfile = open("07_fruits.txt")
content = myfile.read()
myfile.close()
content_list = content.splitlines() 
for item in content_list :
    print(len(item))
