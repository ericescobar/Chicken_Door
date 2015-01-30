#!/usr/bin/python
import time
import signal
import sys

if len(sys.argv)>3: #Tests if you've entered too many arguments
    print "You've entered too many arguments!"
    print "Exiting program..."
    sys.exit(0)

if len(sys.argv)>2: #Argument for door action time
    try:
        float(sys.argv[2])
    except:
        print 'Error: ',str(sys.argv[2]),' is not a number!'
        print "Exiting program..."
        sys.exit(0)
    if int(sys.argv[2])>45: #Checks that a time longer than 45s isn't entered
            print 'Please choose a time less than 45s'
            print "Exiting program..."
            sys.exit(0)

if len(sys.argv)>1: #Argument for door action
    if sys.argv[1]!='close' and sys.argv[1]!='open':
            print 'Please choose "open" or "close"'
            print "Exiting program..."
            sys.exit(0)

if len(sys.argv)==3:
    print 'Forcing door to',str(sys.argv[1]),'for',str(sys.argv[2]),'seconds'
    Door_Action=sys.argv[1]
    Door_Time=sys.argv[2]
if len(sys.argv)==2:
    print 'Forcing door to ',str(sys.argv[1])
    Door_Action=sys.argv[1]
    Door_Time=45 #This is a safety time
if len(sys.argv)==1:
    Door_Action='default' #Will reverse door state
    Door_Time=45 #This is a safety time