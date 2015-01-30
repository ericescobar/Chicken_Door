#!/usr/bin/python
import time
import signal
import sys

print 'Door action: ',sys.argv[1]
print 'Seconds: ',sys.argv[2]
print 'Number of arguments: ',len(sys.argv)

if len(sys.argv)>3:
    sys.exit()
if len(sys.argv)==3:
    try:
        float(sys.argv[2])
    except:
        print 'Error: ',str(sys.argv[2]),' is not a number!'
    if int(sys.argv[2])>45: #Checks that a time longer than 45s isn't entered
            print 'Please choose a time less than 45s'
            sys.exit(0)
            
if sys.argv[1]!='close':# or sys.argv[1]!='open':
        print 'Please choose "open" or "close"'
        sys.exit(0)
if len(sys.argv)>3:
        print 'Too many arguments!'
        sys.exit(0)
elif len(sys.argv)==2:
        print 'Forcing door to ',str(sys.argv[1]),' for ',str(sys.argv[2]),' seconds'
        Door_Action=sys.argv[1]
        Door_Time=sys.argv[2]
elif len(sys.argv)==1:
        print 'Forcing door to ',str(sys.argv[1])
        Door_Action=sys.argv[1]
print 'Reached end!'
