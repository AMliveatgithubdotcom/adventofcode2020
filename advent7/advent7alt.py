import re
rulesdata = open('input.txt', 'r')

rules = rulesdata.read().split('.\n')
rules = [bag.split(' contain ') for bag in rules]
bagstotal = []
counter = 0
allbags = dict([])
searchedbag = 'shinygold'
untilyoulikeit = None

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
			else:
				allowedbags += ['no bags allowed']
	allbags[bagname] = allowedbags

def bagcheck(searchedbag, wantedbag):
	#	print(f'Searching {searchedbag} in {wantedbag}')
		if searchedbag in wantedbag:
			print(f'Gold bag found in {wantedbag}.')
			return True
		else:
			return False

for bag in allbags:
#	print(f'checking bag {bag}')
	if bagcheck(searchedbag, allbags[bag]) == True:
		counter += 1
	else:
		for allowedbag in allbags[bag]:
				if allowedbag == 'no bags allowed':
					print('This bag allows no other bags.')
				else:
					if bagcheck(searchedbag, allbags[allowedbag]) == True:
						counter += 1
					else:
						untilyoulikeit = allowedbag
						wewilldothis = 0
						while(wewilldothis != 1):
							for againandagain in allbags[untilyoulikeit]:
								if againandagain != 'no bags allowed':
									if bagcheck(searchedbag, allbags[againandagain]) == True:
										counter += 1
										wewilldothis = 1
										break
									else:
										untilyoulikeit = againandagain
								else:
									print('This bag allows no other bags.')
							break

print(counter)