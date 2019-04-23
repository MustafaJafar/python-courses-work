import firebase_admin 
from firebase_admin import credentials
from firebase_admin import db
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
p = GPIO.PWM(12, 50)
q = GPIO.PWM(13, 200)
cred = credentials.Certificate('iffr-cf346-firebase-adminsdk-hcik9-d6215733e1.json')
default_app  = firebase_admin.initialize_app(cred,  {'databaseURL': 'https://iffr-cf346.firebaseio.com/'})

ref = db.reference('data')
ox = 0
p.start(0)
q.start(0)
while True:
    x = ref.get()
    if(ox!=x):
        ox =  90
        if(x==1):
            p.ChangeDutyCycle(ox)
            q.ChangeDutyCycle(0)
        elif (x==2):
            p.ChangeDutyCycle(0)
            q.ChangeDutyCycle(ox)
        elif (x==0):
            p.ChangeDutyCycle(0)
            q.ChangeDutyCycle(0)
        time.sleep(.2)
        print(x)

p.stop()		
GPIO.cleanup()