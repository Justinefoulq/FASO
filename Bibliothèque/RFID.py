import signal
from contextlib import contextmanager
import serial
import pickle
import time

@contextmanager
def timeout(time):
    # Register a function to raise a TimeoutError on the signal.
    signal.signal(signal.SIGALRM, raise_timeout)
    # Schedule the signal to be sent after ``time``.
    signal.alarm(time)

    try:
        yield
    except Exception:
        pass
    finally:
        # Unregister the signal so it won't be triggered
        # if the timeout is not reached.
        signal.signal(signal.SIGALRM, signal.SIG_IGN)

def raise_timeout(signum, frame):  
    raise Exception


ser = serial.Serial('/dev/ttyACM0',9600)

def BadgeDetecte():

  res=True
  with timeout(1):
    CodeCarte = ser.readline()
    Fichier=open('../ListeAdmin.txt','rb')
    admin=pickle.load(Fichier)
    Fichier.close
    i=0
    while i< len(admin) and res:
      if admin[i] == CodeCarte:
        res = False
      i=i+1
  return not(res)


#while True:
#  BadgeDetecte()  

#print(BadgeDetecte())

