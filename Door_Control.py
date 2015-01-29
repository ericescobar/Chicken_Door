#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import signal
import sys
#Argument processing, open, close, open x, close x
'''if int(sys.argv[2])>45:
        print 'Please choose a shorter time'
if sys.argv[1]!='close' or sys.argv[1]!='open':
        print 'Please choose "open" or "close"'
        sys.exit(0)
if len(sys.argv)>3:
        print 'Too many arguments!'
        sys.exit(0)
elif len(sys.argv)==2:
        print 'Forcing door to ',str(sys.argv[1]),' for ',str(sys.argv[2]),' se$
        Door_Action=sys.argv[1]
        Door_Time=sys.argv[2]
elif len(sys.argv)==1:
        print 'Forcing door to ',str(sys.argv[1])
        Door_Action=sys.argv[1]
'''
#Setting up Board GPIO Pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(35,GPIO.OUT)
GPIO.setup(37,GPIO.OUT)
GPIO.setup(33,GPIO.IN)#Locked
GPIO.setup(31,GPIO.IN)#Open
TimeStart=time.clock()
runTime=0
#Clean kill of script function (Stops Motor, cleans GPIO)
def signal_handler(signal, frame):
        print 'Performing safe shutdown!'
        GPIO.output(37,False)
        GPIO.output(35,False)
        GPIO.cleanup()
        sys.exit('Motors shutdown, GPIO cleaned')

#Check door status from Magnets
BottomHall=GPIO.input(31)
TopHall=GPIO.input(33)
if BottomHall==0:print 'Door is locked'
if TopHall==0:print 'Door is open'
if BottomHall==1:print 'No magnet sensed on lock'
if TopHall==1:print 'No magnet sensed top'

if 0==0: #Debug Code
#if BottomHall==0: #Door is locked
        print 'The door is locked!'
        print 'The door is going up!'
        while TopHall==1 and runTime<10:
                GPIO.output(35,True)
                GPIO.output(37,False)
                TopHall=GPIO.input(33)
                runTime=time.clock()-TimeStart
#if 0==0:
elif TopHall==0 and BottomHall==1: #Door is open
        print 'The door is open!'
        print 'The door is going down!'
        while BottomHall==1 and runTime<35:
                GPIO.output(35,False)
                GPIO.output(37,True)
                BottomHall=GPIO.input(31)
                runTime=time.clock()-TimeStart
runTime=time.clock()-TimeStart
print 'Total Time: '+str(runTime)
GPIO.cleanup()

