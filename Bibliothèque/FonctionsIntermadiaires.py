import Poids
import RFID

def PersonneDetecte():
  poidPlanche=4
  return Poids.PoidsDetect()> ( 5+ poidPlanche)

def LancerAlarm():
	while True:
		while PersonneDetecte() and not(BadgeDetecte()):
			try:
				grovepi.digitalWrite(buzzer,1)
				print('start')
				time.sleep(0.5)
				grovepi.digitalWrite(buzzer,0)
				print('stop')
				time.sleep(0.5)
			except KeyboardInterrupt:
				grovepi.digitalWrite(buzzer,0)
				break
		grovepi.digitalWrite(buzzer,0)

