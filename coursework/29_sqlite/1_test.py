import sqlite3

#connect to data base
conn = sqlite3.connect("lite.db")

#create cursor object
cur = conn.cursor()
#write to database
cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT , quantity INTEGER , price REAL)")
cur.execute("INSERT INTO store VALUES ('Glass' , 8 , 10.5)")
#commit changes
conn.commit()
#close connection
conn.close()