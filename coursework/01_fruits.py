store_address = ["Flat Street" , "18" , "New York"] #list
pins = {"Mike" : 1234 , "Joe":1111 , "Jack" : 2222}

print(store_address[0] , store_address[1] )
pin = int(input("Enter your pin code : "))

def find_in_file(user_fruit) : 
    myfile = open("01_sample.txt")
    fruits = myfile.read()
    myfile.close()
    fruits = fruits.splitlines()
    if user_fruit in fruits :
        return "That fruit is in the list."
    else : 
        return "No such fruit found!"
    

if pin in pins.values() : 
    fruit = input("Enter fruit : ")
    print(find_in_file(fruit))
else : 
    print("Incorrect pin!")
    print("This info can be accessed only by: ")
    for key in pins.keys() : 
        print(key)

