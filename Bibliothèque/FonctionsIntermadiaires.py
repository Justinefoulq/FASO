import RFID
from grovepi import *
import time

ultrasonic_ranger1 = 4
ultrasonic_ranger2 = 2
ultrasonic_ranger3 = 3
buzzer = 8
led = 6

   
def PersonneDetecte() :
    while not(RFID.BadgeDetecte()):
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
          #LancerAlarme()
          #AllumerLed()
          digitalWrite(buzzer,1)
          digitalWrite(led,1)
          time.sleep(1)
          digitalWrite(buzzer,0)
          digitalWrite(led,0)

while True:
  PersonneDetecte()
  time.sleep(10)


