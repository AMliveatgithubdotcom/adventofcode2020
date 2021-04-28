import re
data = open('input.txt', 'r')
orders = [line.strip().split('\n') for line in data]
orders = [orders[i][0].split(' ') for i in range(len(orders))]
currentline = 0
accumulator = 0
passedlines = []
savedline = 0
savedpassedlines = []
savedaccumulator = 0
mode = 1

#mode 0: switching operators next time
#mode 1: switches operators, remembers current line and passed lines, remembers accumulator
#mode 2: proceeding normally

def nop():
	global currentline
	currentline += 1

def acc(argument):
	global currentline
	global accumulator
	currentline += 1
	accumulator += argument

def jmp(argument):
	global currentline
	currentline += argument

while(True):

	if currentline in passedlines and mode == 2:
		print('Loop at', currentline)
		mode = 0
		print(savedpassedlines)
		print(savedline)
		passedlines = savedpassedlines
		currentline = savedline
		accumulator = savedaccumulator
	else:
		passedlines.append(currentline)
	print(currentline)
	print(passedlines)
	if currentline > len(orders) - 1:
		print('HEY MAN THIS IS GOINMG OUT OF BOUDNS')
		break

	operator = orders[currentline][0]
	argument = int((re.search('(\+?-?)(\d*)', orders[currentline][1]))[0])

	if operator == 'acc':
		print(operator, argument)
		acc(argument)

	if operator == 'nop':
		print(operator, argument)
		if mode == 0:
			print('mode 0')
			mode += 1
			nop()
		elif mode == 1:
			print('mode 1')
			mode += 1
			savedline = currentline
			savedpassedlines = passedlines
			savedaccumulator = accumulator
			jmp(argument)
		else:
			print('mode 2')
			nop()

	if operator == 'jmp':
		print(operator, argument)
		if mode == 0:
			print('mode 0')
			mode += 1
			jmp(argument)
		elif mode == 1:
			print('mode 1')
			mode += 1
			savedline = currentline
			savedpassedlines = passedlines
			savedaccumulator = accumulator
			nop()
		else:
			print('mode 2')
			jmp(argument)
print(accumulator)