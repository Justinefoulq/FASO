import serial
import Admin.py

def BadgeDetecte(): 
  ser = serial.Serial('/dev/ttyACMO',9600)
  CodeCarte = ser.readline()
  admin = Admin.ListeAdmin()
  for i in admin :
    if i == CodeCarte :
      return True
  return False
  
