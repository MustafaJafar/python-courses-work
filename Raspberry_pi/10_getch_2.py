#works on Win , Linux
import keyboard ,  time # using module keyboard

#after quiting : I don't know why I find keys I pressed typed in the terminal 

while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('q'):  # if key 'q' is pressed 
            print('Quite')
            time.sleep(0.3)
            break  # finishing the loop
        elif(keyboard.is_pressed('w')) :
            print('w')
            time.sleep(0.3)
        elif(keyboard.is_pressed('a')) :
            print('a')
            time.sleep(0.3)
        elif(keyboard.is_pressed('s')) :
            print('s')
            time.sleep(0.3)
        elif(keyboard.is_pressed('d')) :
            print('d')
            time.sleep(0.3)
        else:
            pass
    except:
        break  # if user pressed a key other than the given key the loop will break