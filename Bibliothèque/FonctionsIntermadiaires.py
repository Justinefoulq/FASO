import Poids
import RFID
import HautParleur

def PersonneDetecte():
  poidPlanche=4
  return Poids.PoidsDetect()> ( 5+ poidPlanche)

def LancerAlarm():
  if PersonneDetecte() && !(RFID.BadgeDetecte):
    HautParleur.AllumerAlarm()
    
def ArreterAlarm():
  if !(PersonneDetecte()) || (RFID.BadgeDetecte):
    HautParleur.EteindreAlarm()
  
  
