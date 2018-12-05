import serial
import pickle

ser = serial.Serial('/dev/ttyACM0',9600)

def BadgeDetecte():
  res=True
  i=0
  CodeCarte = ser.readline()
  Fichier=open('../ListeAdmin.txt','rb')
  admin=pickle.load(Fichier)
  Fichier.close
  while i< len(admin) and res:
    if admin[i] == CodeCarte:
      res = False
    i=i+1
  return not(res)

print(BadgeDetecte())

