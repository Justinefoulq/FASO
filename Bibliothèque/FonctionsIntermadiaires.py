#import RFID.py
from grovepi import *
import time

ultrasonic_ranger1 = 4
ultrasonic_ranger2 = 2
ultrasonic_ranger3 = 3
buzzer = 8
led = 6

def AllumerLed() :
  #pinMode(led,"OUTPUT") 
  try:
      #Blink the LED
      digitalWrite(led,1)     # Send HIGH to switch on LED
      print ("LED ON!")
      time.sleep(0.5)

      digitalWrite(led,0)     # Send LOW to switch off LED
      print ("LED OFF!")

  except KeyboardInterrupt:   # Turn LED off before stopping
      digitalWrite(led,0)
  except IOError:             # Print "Error" if communication error encountered
      print ("Error")

def LancerAlarme():
    try:
      digitalWrite(buzzer,1)
      print('start')
      time.sleep(0.5)
      digitalWrite(buzzer,0)
      print('stop')
    except KeyboardInterrupt:
      digitalWrite(buzzer,0)
   
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
          #LancerAlarme()
          #AllumerLed()
          digitalWrite(buzzer,1)
          digitalWrite(led,1)
          time.sleep(0.7)
          digitalWrite(buzzer,0)
          digitalWrite(led,0)
        

PersonneDetecte()
