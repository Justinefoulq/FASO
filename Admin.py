import serial

ser = serial.Serial('/dev/ttyACMO',9600)
admin=[]

def creerAdmin ():
  admin= admin + [ser.readline()]
  return admin
  
def supprAdmin ():
  for i in admin:
    if i == ser.readline():
      i=nil
  return admin


def ListeAdmin():
  return admin

def QueFaire():
  print("Voulez vous Ajouter('A'), Supprimer('S'), ou Voire('V') les admins?")
  action=readline()
  if action = 'A':
    admin=creerAdmin()
  else if action ='S':
    admin=supprAdmin()
  else 
    for i in admin:
      println(i)

Quefaire()      
