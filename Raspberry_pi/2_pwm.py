'''to use GPIO numbering type
GPIO.setmode(GPIO.BCM)
   to use pin numbering type
GPIO.setmode(GPIO.BOARD)'''
import RPi.GPIO as GPIO
import time 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
p = GPIO.PWM(11,100)
c = GPIO.PWM(12,100)
p.start(0)
c.start(0)
for i in range(100):
    p.ChangeDutyCycle(i)
    c.ChangeDutyCycle(i)  
    time.sleep(0.1)
p.stop()
c.stop()
GPIO.cleanup()
