import re
data = open('input.txt', 'r')

answersraw = (data.read()).split('\n\n')
answers = [answer.split("\n") for answer in answersraw]
answerstotal = 0
sameanswers = 0
print(answers)
for group in answers:
	answerpool = " "
	samepool = "\w*"
	for member in group:
			if len(member) != 0:
				print("Next answers:", member)
				if len(samepool) != 0:
					answerssame = re.findall(f'[{samepool}]', member)
					print("Current Pool:",samepool)
					print("Same answers compared to the pool:",answerssame)
					samepool = re.sub(f'.', '', samepool)
					samepool = samepool.join(answerssame)
				else:
					print("No more same answers in group.")
				print("Pool now:",samepool)
			else:
				print("End of data.")
			for answer in member:
				answerfiltered = re.sub(f'[{answerpool}]', '', answer)
				answerpool += answerfiltered
				answerstotal += len(answerfiltered)
	sameanswers += len(samepool)
	print(f"In this group we found {len(answerssame)} same answer(s).")
	print("Switching group...")
print(sameanswers)
print(answerstotal)