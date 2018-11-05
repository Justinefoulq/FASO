import Poids
import RFID
import HautParleur

def PersonneDetecte():
  poidPlanche=4
  return Poids.PoidsDetect()> ( 5+ poidPlanche)

def LancerAlarm():
  if PersonneDetecte() and !(RFID.BadgeDetecte):
    HautParleur.AllumerAlarm()
    
def ArreterAlarm():
  if !(PersonneDetecte()) or (RFID.BadgeDetecte):
    HautParleur.EteindreAlarm()
  
  
