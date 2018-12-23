# coding: utf-8
# GrovePi + Grove Ultrasonic Ranger


from grovepi import *

# Connect the Grove Ultrasonic Ranger to digital port D4
# SIG,NC,VCC,GND

ultrasonic_ranger1 = 4
ultrasonic_ranger2 = 2
ultrasonic_ranger3 = 3

def PersonneDetecte() :
    while True:
        try:
            # Read distance value from Ultrasonic
            ultra1=ultrasonicRead(ultrasonic_ranger1)

        except TypeError:
            print "Error"
        except IOError:
            print "Error"

        try:
               # Read distance value from Ultrasonic
            ultra2=ultrasonicRead(ultrasonic_ranger2)

        except TypeError:
            print "Error"
        except IOError:
            print "Error"

        try:
                    # Read distance value from Ultrasonic
            ultra3=ultrasonicRead(ultrasonic_ranger3)

        except TypeError:
            print "Error"
        except IOError:
            print "Error"

        if ultra1<50 or ultra2<50 or ultra3<50 :
             return True
        else :
             return False

while True :
    print(PersonneDetecte())
