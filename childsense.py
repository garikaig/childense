#Raspberry Pi Motion Detector Code
import requests # required for the webhook to trigger the event on IFTTT
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
try:
  while True:
    if GPIO.input(23): #If there is a movement, PIR sensor gives input to GPIO 23
       requests.post('https://maker.ifttt.com/trigger/child_room_exit_entry_detected/with/key/jZWj1lUlXVucDaenGbKAcJg0KM0_ggnt9h5B40LNb07')
       GPIO.output(24, True) #Output given to Buzzer through GPIO 24
       GPIO.output(17, GPIO.HIGH) # turn on the LED light as well
       time.sleep(1) #Buzzer turns on for 1 second
       GPIO.output(24, False)
       GPIO.output(17, GPIO.LOW) # turn off the LED light
       time.sleep(5)
    time.sleep(0.1)
except KeyboardInterrupt:
  GPIO.cleanup()
