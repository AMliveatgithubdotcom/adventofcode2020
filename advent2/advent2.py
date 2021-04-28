import re
f = open('input.txt', 'r')
counter1 = 0
counter2 = 0
for line in f:
	passwordraw = re.search('(\d?\d)-(\d?\d) (\w): (\w*)', line)
	ziffer = str(passwordraw[3])
	password = list(passwordraw[4])
	passnum1 = int(passwordraw[1])
	passnum2 = int(passwordraw[2])
	passstelle1 = password[passnum1 - 1]
	passstelle2 = password[passnum2 - 1]
	passchars = re.findall(ziffer, passwordraw[4])
	print("Pruefung des Passwortes nach Aufgabe 1 Bedingung:")
	if (passnum1 <= len(passchars) <= passnum2):
		print(f"{passchars} ist groesser als {passnum1} und kleiner als {passnum2}.")
		print("Passwort erfuellt Bedingung 1.")
		counter1 += 1
	else:
		print("Passwort erfuellt Bedingung 1 nicht.")
	print("Pruefung des Passwortes nach Aufgabe 2 Bedingung:")
	if (ziffer == passstelle1 or ziffer == passstelle2) and passstelle1 is not passstelle2:
		print("Es wurde gefunden:", ziffer, " in ", passstelle1, passstelle2, ". \nPasswort:", password)
		print(passstelle1, "ist nicht", passstelle2)
		print("Passwort erfuellt Bedingung 2.")
		counter2 += 1
	else:
		print("Passwort erfuellt Bedingung 2 nicht.")
print(counter1)
print(counter2)