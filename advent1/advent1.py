data = []
f = open('input.txt', 'rb')
for line in f:
	data += ([int(line)])
try:
	for a in data:
			for b in data:
				for c in data:
					#print("calculating %s, %s, %s" % (a, b, c))
					result = int(a + b + c)
					#print(result)
					if result == 2020:
						print("%s RICHTIG" % result)
						ergebnis = (a * b * c)
						raise
except:
	pass
print("Ergebnis: %s" % ergebnis)