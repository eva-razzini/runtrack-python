def cesar(msg="", clef=0): 
	alphabet="abcdefghijklmnopqrstuvwxyz" 
	chiffre="" 

	for l in msg.lower(): 
		pos=alphabet.find(l) 
		if pos != -1: 
			chiffre+=alphabet[(pos+clef) % len(alphabet)] 
		else: 
			chiffre+=l 
	return chiffre 
message="Bonjour Cesar!" 
chiffre=cesar(message, 5) 
print(message, "=>", chiffre)