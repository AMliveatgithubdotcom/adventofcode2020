import re
passportinput = open('input.txt', 'r')
passporttemp = []
counter = 0
passcounter = 0

def controlbyr(x):
	byrc = int(x.split(':')[1])
	if 1920 <= byrc <= 2002:
		print(f"byr {byrc} pass")
		global passcounter
		passcounter += 1
	else:
		print("byr falsch", byrc)

def controlecl(x):
	eclc = x.split(':')[1]
	eclvalid = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
	if eclc in eclvalid:
		print(f"ecl {eclc} pass")
		global passcounter
		passcounter += 1
	else:
		print("ecl falsch", eclc)

def controleyr(x):
	eyrc = int(x.split(':')[1])
	if 2020 <= eyrc <= 2030:
		print(f"eyr {eyrc} pass")
		global passcounter
		passcounter += 1
	else:
		print("eyr falsch", eyrc)

def controlhcl(x):
	hclc = x.split(':')[1]
	if re.search('#[a-f 0-9]{6}', hclc):
		print(f"hcl {hclc} pass")
		global passcounter
		passcounter += 1
	else:
		print("hcl falsch", hclc)

def controlhgt(x):
	hgtc = x.split(':')[1]
	hgtnumber = int(' '.join(re.findall('[\d]{2,3}', hgtc)))
	if (re.search('[\d]{2,3}cm', hgtc) and 150 <= hgtnumber <= 193) or (re.search('[\d]{2,3}in', hgtc) and 59 <= hgtnumber <= 76):
		print(f"hgt {hgtc} pass")
		global passcounter
		passcounter += 1
	else:
		print("hgt falsch", hgtc)

def controliyr(x):
	iyrc = int(x.split(':')[1])
	if 2010 <= iyrc <= 2020:
		print(f"iyr {iyrc} pass")
		global passcounter
		passcounter += 1
	else:
		print("iyr falsch", iyrc)

def controlpid(x):
	pidc = x.split(':')[1]
	if re.search('[0-9]{9}', pidc):
		print(f"pid {pidc} pass")
		global passcounter
		passcounter += 1
	else:
		print("pid falsch", pidc)

for line in passportinput:
	if line == '\n':
		print("line was n")
		print(passporttemp)
		print(len(passporttemp))
		if len(passporttemp) >= 7:
			if re.findall('byr[^ ]+', ' '.join(passporttemp)):
				byr = re.findall('byr[^ ]+', ' '.join(passporttemp))[0]
				controlbyr(byr)
			if re.findall('ecl[^ ]+', ' '.join(passporttemp)):
				ecl = re.findall('ecl[^ ]+', ' '.join(passporttemp))[0]
				controlecl(ecl)
			if re.findall('eyr[^ ]+', ' '.join(passporttemp)):
				eyr = re.findall('eyr[^ ]+', ' '.join(passporttemp))[0]
				controleyr(eyr)
			if re.findall('hcl[^ ]+', ' '.join(passporttemp)):
				hcl = re.findall('hcl[^ ]+', ' '.join(passporttemp))[0]
				controlhcl(hcl)
			if re.findall('hgt[^ ]+', ' '.join(passporttemp)):
				hgt = re.findall('hgt[^ ]+', ' '.join(passporttemp))[0]
				controlhgt(hgt)
			if re.findall('iyr[^ ]+', ' '.join(passporttemp)):
				iyr = re.findall('iyr[^ ]+', ' '.join(passporttemp))[0]
				controliyr(iyr)
			if re.findall('pid[^ ]+', ' '.join(passporttemp)):
				pid = re.findall('pid[^ ]+', ' '.join(passporttemp))[0]
				controlpid(pid)
			print("passed checks:", passcounter)
			if passcounter == 7:
				print("passport valid")
				counter += 1
			else:
				print("passport not valid")
		passcounter = 0
		passporttemp = []
	else:
		passporttemp += re.findall('(\w{3}[^ ]+)', line.strip('\n'))


		
print("Valid:", counter)