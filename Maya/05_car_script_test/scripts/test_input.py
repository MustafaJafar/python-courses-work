testVar = input("Please Enter attributes : ") 
last_char =""
my_list = []
while testVar : 
    if testVar[0].isdigit() and last_char :
        last_char = last_char*10 + float(testVar[0])
        print(last_char)
    elif testVar[0].isdigit() : 
        last_char = float(testVar[0])
        print(last_char)
    else :
        last_char = 0 

    testVar = testVar[1:]
