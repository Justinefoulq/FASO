import serial
import pickle

ser = serial.Serial('/dev/ttyACM0',9600)

def creerAdmin (admin):
  deja=False
  Codecarte=ser.readline()
  for i in range(len(admin)):
    if admin[i] == Codecarte:
      deja=True
  if not(deja):
    admin.append(Codecarte)
  else:
    print("Cette carte est deja admin")
  return admin
  
def supprAdmin (admin):
  Codecarte=ser.readline()
  i=0
  supp=True
  while i< len(admin):
    if admin[i] == Codecarte:
      del admin[i]
      supp=False
    i=i+1
  if supp:
    print("Cette carte n'est pas admin")
  return admin


def QueFaire():
  print("Voulez vous Ajouter('A') ou  Supprimer('S') un admin?")
  action=raw_input()
  print("Voici les admins existants")
  
  Fichier=open('ListeAdmin.txt','rb')
  admin=pickle.load(Fichier)
  Fichier.close
  print(admin)
  if action == 'A':
    admin=creerAdmin(admin)
  elif action == 'S':
    admin=supprAdmin(admin)
  else:
    print("La lettre n'est pas bonne")
  print("Voici la nouvelle liste des admins")
  print(admin)
  Fichier=open('ListeAdmin.txt','wb')
  pickle.dump(admin,Fichier)
  Fichier.close
   
QueFaire()  
