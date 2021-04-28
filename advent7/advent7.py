import re
rulesdata = open('input.txt', 'r')

rules = rulesdata.read().split('.\n')
rules = [bag.split(' contain ') for bag in rules]
bagstotal = []
counter = 0
allbags = dict([])
goldbagallowed = []
condition = 0
for bag in rules:
	bagname = bag[0].replace(' ', '')
	bagname = re.sub('bags?', '', bagname)
	allowedbags = []
	for conditions in bag[1:]:
		allowedbagsraw = conditions.split(', ')
		for singlebag in allowedbagsraw:
			formattedcondition = re.findall('(\d+) (.+)bags?', singlebag)
			if len(formattedcondition) != 0:
				formattedcondition = list(formattedcondition[0])
				allowedbags += [formattedcondition[1].replace(' ', '')]
				if 'shinygold' in allowedbags:
					goldbagallowed.append(bagname)
				allbags[bagname] = allowedbags
			else:
				allowedbags = ['shinygold']
	allbags[bagname] = allowedbags
goldbagallowed = set((goldbagallowed))
def checkbag(bagtocheck):
	if bagtocheck in goldbagallowed:
		return True

for bags in allbags:
	if checkbag(bags) == True:
		counter += 1
	else:
		innerbags = []
		[innerbags.append(appendbags) for appendbags in allbags[bags]]
		for otherbags in innerbags:
			if checkbag(otherbags) == True:
				counter += 1
				condition = 1
				break
		
print(counter)