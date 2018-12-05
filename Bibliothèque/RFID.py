import serial

ser = serial.Serial('/dev/ttyACMO',9600)

def BadgeDetecte():
  res=True
  CodeCarte = ser.readline()
  Fichier=open('ListeAdmin.txt','rb')
  admin=pickle.load(Fichier)
  Fichier.close
  while i< len(admin) and res:
    if admin[i] == Codecarte:
      res = False
    i=i+1
  return not(res)

print(BadgeDetecte())
