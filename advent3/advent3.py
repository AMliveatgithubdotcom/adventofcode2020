map = open('input.txt', 'r')

inputx = int(input("Wert X / Nach Rechts? \n"))
print(f"Wert X = {inputx}")
inputy = int(input("Wert Y / Nach Unten? \n"))
print(f"Wert Y = {inputy}")

globaly = 0
ycoord = 0
xcoord = 0
baumcounter = 0
for line in map:
	currentline = line.rstrip()
	maxlenght = len(currentline)
	if ycoord < inputy:
		print("Es wird zur naechsten Y gegangen... (Y: ", ycoord," Gewuenscht: ", inputy, ")")
		ycoord += 1
	else:
		xcoord += inputx
		if xcoord >= maxlenght:
			print("X out of bounds. (Line Size: ", maxlenght,")")
			xcoord = xcoord - maxlenght
			print("New X: ", xcoord)
		currentlocation = currentline[xcoord]
		print("Terrain:", currentlocation, "X: ", xcoord, "Y: ", globaly)
		if currentlocation == "#":
			print("Baum gefunden.")
			baumcounter += 1
		ycoord = 1
	globaly += 1
print("Ende Erreicht. \nBaumcounter: ", baumcounter)