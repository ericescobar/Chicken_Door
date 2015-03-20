#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import signal
import sys
import httplib, urllib #for Push Notifications
import subprocess


#Setting up Board GPIO Pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(38,GPIO.OUT)
GPIO.setup(40,GPIO.OUT)
#Clean kill of script function (Stops Motor, cleans GPIO)
def Safe_Kill():
        print 'Performing safe shutoff!'
        GPIO.output(38,False)
        GPIO.output(40,False)
        GPIO.cleanup()
        sys.exit('Lights out!')
print 'Light on!'
GPIO.output(38,False)
GPIO.output(40,True)
time.sleep(2)
cmd = "fswebcam -q -r 640x480 Zip.jpg"
subprocess.Popen(cmd , shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
time.sleep(2)
Safe_Kill()
