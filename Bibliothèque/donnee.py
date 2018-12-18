import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def stockDonneesDateIntrusion(date):
	#Ajoute dans le google form 
	#Dans la base de donnees pour permettre de faire des graphes (optimisation du dispositif)
	requests.post('https://docs.google.com/forms/d/e/1FAIpQLSc_v6OQrK_5Ft8TQxF6Wa_cb9TUv3DblCYvV95quh_PZp20cA/formResponse', data = {'entry.227361499':date} ,verify=False)
