#works only on Win

# msvcrt is a windows specific native module
import msvcrt
import time

"""
this program listens and display buttons presse on keyboard 
events supported : 
    on_press
"""

# asks whether a key has been acquired
def kbfunc():
    x = msvcrt.kbhit() #this is boolean for whether the keyboard has been hit
    if x:
        ret = msvcrt.getch() #getch acquires the character encoded in binary ASCII
    else:
        ret = False
    return ret


while True:

    x = kbfunc()      #acquire the keyboard hit if exists

    #if we got a keyboard hit

    if x == b'\x1b' : # esc
        print ("Quite")
        break
    
    elif x == b'\xe0':
        x = kbfunc() 
        if x == b'H' : 
            print ("up")
        elif x == b'P' : 
            print ("down")
        elif x == b'M' : 
            print ("right")
        elif x == b'K' : 
            print ("left")
        #time.sleep(0.3)
    
    elif x :
        print (x)
        #time.sleep(0.3)
    