#Note this file may contain some error 
	#used for demonstration

#Python Core Data Types
#Numbers 
100
1.0132

#Strings
"Hello, Maya"
"Example String"

#Lists : square braces
[1,2,3]
["abc", ["b","c"], 1]

#Dictionaries : curly braces
{"a":1 , "b":2 , "c":"abc"}

#Tuples : regular brackets , can't be changed
(1,2,3)

#Files
test_file = open("readme.txt" , "r")

#Others
None
True
False

#Get object type 
type(100)

#Python Variables 

#Assign integer to a variable 
a = 10 
b = 5

#Assign a string to a variable 
my_string = "Begining Python"

#Using variables in an expression

a + b #Add a and b
a * b #Multiply a and b

a + c #Error variable is not defined

c = a + b #Assign result to a variable

#Valid variable names : it can consist of numbers , letters & underscores
test_variable_01 = 1
_my_name = "Mustafa"

#Invalid variable names 
01_test = 123 #it can't start with a number
print = 456   #it can't be a reserved keyword


#Comments : it can be used to illustrat your code
#This is a one line comment 

''' 
	this is a comment block
'''

#Numeric Types 

#Integers "Whole numbers": like animation time slider
1234 , -22 , 0

#Floating Points Numbers : like position , rotation & scale
1.212 , -22.3 , .1

#Octal base : 8 , hex base : 16 and binary base : 2
0177            , 0xffff        , 0b110011

#Complex Numbers
3+4j , 2.0+2.0j , 2j

'''
there is a lot of math tools & functions built in python for processing numbers
	like : operators (+,-,*,/) , absolute , random & etc...
'''
#Operators
#Regular Math
5 + 5 
5 - 5 
5.5 * 2
20 / 10
#Modulus
15 / 2 
15 % 2 
#Truncation py2
3 / 2 #result = 1 not 1.5 as they are integers , in py3 3 / 2 = 1.5 
3 / 2.0 #result = 1.5
3 //2.0 #result = 2.0 = round(1.5)
#presidence 
10 * 2 + 3 #23
3 + 10 * 2 #23
(3+10) * 2 #26
#Using variables to breakup equations
a = 3 
b = 10 
c = 2 
d = a + b 
e = d * c #26

#Comparison 
10 > 2 #True
10 < 2 #False
10 >=2 #True
10 >=10#True
10 <=2 #False
10 !=2 #True
10 !=10#False

a = 5 
b = 2 
if (a > b) : 
	#do something
	pass
else:
	#do something else 
	pass


#String example

empty_string = ''
single_quotes = 'String literal in single quotes'
single_quotes = 'String's literal in single quotes' #error
double_quotes = "string literal in double quotes"
double_quotes = "string's literal in double quotes" #no error
escape_sequence = "\tInsert tab \nInsert newline"
doc_String = """this is a doc string"""
s1 = 'String 1'
s2 = "String 2"
concatenate = s1 + " and " + s2
number_of_chars = len (s1)
s1[0] #first character
s1[1] #second character
s1[-1] #last character

s1.upper() #convert to UPPERCASE
s1.lower() #convert to lowercase

s1.split(' ') #splite the string at each space "returns a list"

#Escape Sequence \ 
#Common
"newline: \n"
"line1\nline2\nline3\n"
"tab: \t"
"make\tsome\ttabs"
"double-quote: \""
"this is \"is\" a string"
'single=quote: \''
'this is \'is\' a string'
"this is 'is' a string"
'backslash: \\' #used with file paths on windows
"c:\\new_folder"
#Raw string
r"c:\new_folder"
#Other
"bell: \a"
"backspace: \b"
"formfeed: \f"

#String Operations
s1 = "abcdef"
s2 = "uvwxyz"

#Get the number of characters
len("abc")
len(s1)

#Conactenation 
s1 + s2 + " " + s1 + s2
#Repetation
s1 * 5 
print("----------------------------")
print("-" * 30)
#Iterate over a string
for c in s1 : 
	print(c)
#search for a character in a substring
"a" in s1 #Returns True if s1 contains an "a"
"abc" in s1 

#Indexing 
s1[0]  #first character
s1[3]  #fourth characater
s1[-1] #first character from the end
s1[-3] #third character from the end

#Slicing
s1[0:3] # every charcter from position 0 up to position 3 = 0 , 1 , 2 = abc
s1[2:]  #from index 2 to the end
s1[:3]  #from the start up to -but not including- index 3
s1[:-1] #from the start up to the item before the last one
s1[0:5:2] # from index 0 to index 4 offset = 2 
s1[::-1] #negative offset , result = reversed string

#Strings are not mutable "can't be modified directly!"
s = "Maya is cool"
s[0] = "m" #error

s = "m" + s[1:] #solution
s = s.replace("cool" , "awesome")

#String methods (most of maya commands depends on strings)
s = "Beginning Python for Maya"
s.upper()
s.lower()
s.isupper()
s.islower()
s.find("Python") # return index of "P"
#none of these methods changed the original string untill you assign its value to the original variable
s = s.upper()

#Number Strings
number = "1"
number.isdigit() # return True
s.isdigit() # return False
number.zfill(4) #returns 0001 ,4 digit number "you already have 1 digit" , it will fill with zeros "zfill"

s.split(" ") # result = list of words splitted by space
import os
paths = os.environ["MAYA_SCRIPT_PATH"] #returns all available paths of the mel scripts separated by ;
paths = paths.split(";")
for p in paths : 
	print(p)

#String format
a = 1 
b = 2
c = 4.32856

"The sum of a + b is {0}".format(a+b) #replace {0} wuth the sum of a+b
"a: {0} b: {1} c: {2}".format(a,b,c)
"a: %s b: %s c: %s"%(a,b,c)
"a: " + str(a) + " b: " + str(b) + " c: " + str(c)
"a: {0:04d}".format(a)
"c: {0:0.2f}".format(c)
"c: %0.2f"%(c)

#Print function #when excuting on line of code , result will be printed on the screen automatically 
temp_string = "Hello Python" 		#but for a block it won.t print anything
print temp_string #print statment works only for py2
	#instead use print function : print()
print("temp_string: {0}".format( temp_string)) 

fruits = ["apple" , "orange" , "banana"]
for fruit in fruits : 
	print(fruit)

#Lists : ordered object collections of any type "mutable"
a= [] #empty list
b=[0,1,2,3,4] #list with 5 items
c=[3.14,"abc" , [1,2,3,4]] #nested list
d = list["Python"] #break string into list of characters
e = list[range(0,10)] #list of numbers from 0 to 9

len(d) #length of d 

b + c # concatenate 
c + b # it's not the same as b+c
b * 4 #repeate b 4 times 

3.14 in c #return True
1 in c #return False

#lists are mutable : you can directly change items
b[2] = 9 
print(b[2]) # it's now become 9 

#you can access elements of the list using index
b[1] 
c[0]
c[2][0] #sub index ... 
c=[3.14,"abc" , [1,2,3,4 , ["a" , "b" , "c"] ]]
c[2][4][0] 

#List slicing
b[:2]
b[1:3]
c[:-1]

#List methods
a.append["a"] #append means add element
a.append["b"]
a.append["c"] 
a.append[b]   #append list to a list : nested list
a = ["a","b","c"] #reset 
a.extend(b)   #append b's elements to a : concatenate
a= []
a.append("Python") #list of 1 element string "Python"
a=[]
a.extend("Python")#list of all characters of "Python"
b.insert(0 , "a") #insert element a with index 0 , and simply shift the rest over
b.insert(3 , "b")
b.remove("b")   #remove by element value 
b.remove("b")   #if "b" isn't in list it will raise an error

if("a" in b ) : 
	b.remove("a")

del d[0] #remove by index !

#Sorting lists
a = [43 , 26 , 1 , 55 , 101]
b = ["dog" , "cat" , "DOG" , "CAT"]

#two tyeps of sort 

a.sort() #In place Sort
a_sorted = sorted(a) #Return Sorted list , original remains unchanged

a.sort(reverse = Ture) #sort backwards
a = [43 , 26 , 1 , 55 , 101] #reset
a_sorted = sorted(a , reverse = Ture) #sort backwards

#Sort on strings 
b.sort() #Uppercase followed by lowercased characters
b.sort(key = str.lower) #sorted in a case insenstive manner

#Dictionary 
d = {}
d = {"red" : 255 , "green" : 255 , "blue" : 255} #each value is mapped to a key
d["red"] #return value of red
d["red"] = 200 #set red to 200
d["cyan"] = 255 #mapping to a key that doesn't exist
		#will create a new key with this value 
#return value of cyan
d["cyan"]
d.get("cyan") 
#diffrence between them 
d["black"] #raise a key error as key doen't exist
d.get("black") #return None

#Membership : test if a key exist in a dictinary
"red" in d #return True
"black" in d #return False

#Built in methods
d.keys() #returns a list of all keys
d.values() #return a list of all values
d.items() #return a list of tuples each has key & its value
#example display all the values 
for k in d.keys() : 
	print(d[k])
for item in d.items() :
	print("{0} -> {1}".format(item[0] , item[1]))

#Tuples : sinilar to lists but size cannot be changed , not mutable
t = ()
t = (1,"abc") #two items tuple
t = (1,"abc" , 3 , "adf") #4 items tuple
t[0] #return 1
t[0] = 5 #error no assignment

'''
Python Scripting rules forces users to write clean readable code
Python golden rule : indentation to define blocks
'''
#Python Statments : 
#Assignment
a = 10
b = "python"

#Print Statment
print("Print text to output")

#If/Else
if a < 10 : #colons tells python that there is a block
    print("less than")
elif a == 10 :
    print("equal to")
else : 
    print("greater than")

#example
'''
if you are making a cod e for users that modify selected objects
sure , you don't want a user to get an error so 
''' 
import maya.cmds as cmds
sel = cmds.ls(sl = True)
if len(sel) >= 2 :
    for s in sel : 
	print (s)
elif len(sel) ==1 : 
    print("Please select atleast two objects")
else:
    print("No Objects Selected")

#For Loops (iterate over a seuence)
for x in range(0,10):
    if x % 2 : 
	continue #Continue excecution of the loop
    else :
	print(x)

for x in range(0,10):
    print(x)
else :         #when the condition of the loop evaluates to False
    print("on loops exit without break") #in other words on loop exit

#While Loop 
while True :
    if exitloop():
	break #exit the loop

counter = 10 
while counter > 0 :
    if counter == 5 : 
	break     #do nothing
    print(counter)
    counter -= 1
else : 
    print("on while exit")
my_string = "Maya Python"
while my_String:
    (my_string)
    my_String = my_string[1:] strip first character

#how statments evalutes
if None : #none evaluates to False
    print("This is a true statment") 

None # Evaluates to False
test = "python" #True
test = "" 	#False 
test = [1,2,3]  #True
test = []	#False
#same for dictionary & tuples
test = 1	#True
test = 0	#False "this is the only number that evalutes to False"

#Operators  
#compare :  == , > , >= , < , <= , !=
#Logical : and , or , not 
5 > 3 # True
True and Fale # False 
True or False # True
True and False or True #True "following the order of operation"
(True and False) or True # this is how the last statment evaluated
			 #and has higher order of operation than or 
			 #like multiplication and division
(1 + 2 ) * 3 != 1 + 2 * 3 

True and False or True == True or True and False
True and False or True != (True or True) and False

#Import Module (importing code ibraries to use directly in you code)
import os 
import maya.cmds as cmds

#Functions : P.S. Local Variable - Global Variable
def add(input_a , input_b):
    return input_a + input_b #return statment

print( nothing(1,2,3)) # will raise an error as functions isn't defined yet

def nothing(a, b, c, x = 5 , y = 4 , z = 2) #function with default values
    return [a , b , c ,x , y ,z]  

print(nothing(1 ,2 ,3))
print(nothing(1,2,3,4,5,6))
print(nothing(x = 2 , 1, 2,3)) #raise an error keyword argument must come 
				#default arguments

#Pass by Refrence / Value
def number_swap(num):
    num = 77
    print(num)

my_num = 5 
print("Before -> {0}".format(my_num)) #5
number_swap(my_num)
print("After -> {0}".format(my_num))  #5

def pass_by_refrence(a_list):
    a_list.append("4")
    a_list.append("5")
    a_list.append("6")

my_list = [0,1,2]
print("Before -> {0}".format(my_list)) #[0,1,2]
pass_by_refrence(my_list)
print("After -> {0}".format(my_list)) #[0,1,2,4,5,6]

def pass_by_value(a_list):
    alt_list  = list(a_list) #create a copy
    alt_list.append("4")
    alt_list.append("5")
    alt_list.append("6")

my_list = [0,1,2]
print("Before -> {0}".format(my_list)) #[0,1,2]
pass_by_value(my_list)
print("After -> {0}".format(my_list)) #[0,1,2]


def pass_by_value2(a_list):
    a_list = [4,5,6]    #you can't assign it ! but you can modify it using methods or that's what I have understood

my_list = [0,1,2]
print("Before -> {0}".format(my_list)) #[0,1,2]
pass_by_value2(my_list)
print("After -> {0}".format(my_list)) #[0,1,2]

#you can check pdf to see results !

#there is a alot of built in functions without any sort of importing  modules
#remember maya uses python 2.7.5 or 2.7.6

