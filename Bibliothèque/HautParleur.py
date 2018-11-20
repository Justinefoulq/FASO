
import time
import grovepi

buzzer = 8

grovepi.pinMode(buzzer,"OUTPUT")

def AllumerAlarm() :
  try:
        # Buzz for 1 second
        grovepi.digitalWrite(buzzer,1)
        print ('start')
        time.sleep(0,5)

        # Stop buzzing for 1 second and repeat
        grovepi.digitalWrite(buzzer,0)
        print ('stop')
        time.sleep(0.5)

    except KeyboardInterrupt:
        grovepi.digitalWrite(buzzer,0)
        break
    except IOError:
        print ("Error")
  
  
def EteindreAlarm():
  try:
        grovepi.digitalWrite(buzzer,0)
      

    except KeyboardInterrupt:
        grovepi.digitalWrite(buzzer,0)
        break
    except IOError:
        print ("Error")
  
  
  

    
