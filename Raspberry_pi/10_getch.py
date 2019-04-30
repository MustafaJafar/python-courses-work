#Linux Only as no termios on Win
import sys, tty, termios, time

def getch() : 
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try : 
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally : 
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

 
 
while True : 
    
    char = getch()
    if (char == "q") :
        print ("exiting program")
        break  
    else :
        print (char)
    time.sleep(0.01)
     


