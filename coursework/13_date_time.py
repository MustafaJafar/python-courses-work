from datetime import datetime

now = datetime.now() 
then = datetime(2000 , 12 , 31)

delta = now - then

whenever = datetime.strptime("2015-12-31" , "%Y-%m-%d")
whenever_2 = datetime.strptime("2015:12:31:20:59" , "%Y:%m:%d:%H:%M")

print (delta)
print(whenever)
print(whenever_2)

#for more codes about strptime : 
#http://strftime.org/