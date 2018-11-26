import time
import grovepi

# Connect the Grove Buzzer to digital port D8
# SIG,NC,VCC,GND
buzzer = 8

grovepi.pinMode(buzzer,"OUTPUT")

def AllumerAlarm():
	i=0
	while i<4:
    		try:
        		# Buzz for 1 second
        		grovepi.digitalWrite(buzzer,1)
        		print ('start')
        		time.sleep(0.5)

        		# Stop buzzing for 1 second and repeat
        		grovepi.digitalWrite(buzzer,0)
        		print ('stop')
        		time.sleep(0.5)

    		except KeyboardInterrupt:
        		grovepi.digitalWrite(buzzer,0)
        		break
    		except IOError:
        		print ("Error")
		i=i+1


AllumerAlarm()

