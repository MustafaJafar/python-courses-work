import firebase_admin 
from firebase_admin import credentials
from firebase_admin import db
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
l1 = GPIO.PWM(15, 200)
l2 = GPIO.PWM(13, 200)
r1 = GPIO.PWM(8, 200)
r2 = GPIO.PWM(10, 200)
cred = credentials.Certificate('iffr-cf346-firebase-adminsdk-hcik9-d6215733e1.json')
default_app  = firebase_admin.initialize_app(cred,  {'databaseURL': 'https://iffr-cf346.firebaseio.com/'})

ref = db.reference('data')
ox = 0
l1.start(0)
l2.start(0)
r1.start(0)
r2.start(0)
ox =  50
while True:
    x = ref.get()
    if(x==1):
        l1.ChangeDutyCycle(0)
        l2.ChangeDutyCycle(ox)
        r1.ChangeDutyCycle(0)
        r2.ChangeDutyCycle(ox)
    elif (x==2):
        l1.ChangeDutyCycle(ox)
        l2.ChangeDutyCycle(0)
        r1.ChangeDutyCycle(ox)
        r2.ChangeDutyCycle(0)
    elif (x==3):
        l1.ChangeDutyCycle(0)
        l2.ChangeDutyCycle(ox)
        r1.ChangeDutyCycle(ox)
        r2.ChangeDutyCycle(0)
    elif (x==4):
        l1.ChangeDutyCycle(ox)
        l2.ChangeDutyCycle(0)
        r1.ChangeDutyCycle(0)
        r2.ChangeDutyCycle(ox)
    elif (x==0):
        l1.ChangeDutyCycle(0)
        l2.ChangeDutyCycle(0)
        r1.ChangeDutyCycle(0)
        r2.ChangeDutyCycle(0)
    time.sleep(.2)
    print(x)

l1.stop()
l2.stop()
r1.stop()
r2.stop()	
GPIO.cleanup()
