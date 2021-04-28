boardpasses = open('input.txt', 'r')

allIDs = []
for line in boardpasses:
	upperr = 0
	lowerr = 127
	rangerow = 128
	row = 0
	column = 0
	searchingcolumn = 0
	seatID = 0
	passline = line.strip('\n')
	print(passline)
	for i in passline:
		rangerow = rangerow / 2
		if (i == "B") or (i == "R"):
			upperr += rangerow
			print(f"Found letter {i}, range is {rangerow}")
			print(f"New Values: {upperr}, {lowerr}")
		if (i == "F") or (i == "L"):
			lowerr -= rangerow
			print(f"Found letter {i}, range is {rangerow}")
			print(f"New values: {upperr}, {lowerr}")
		if upperr == lowerr:
			if searchingcolumn == 0:
				searchingcolumn += 1
				row = upperr
				print(f"Row found: {row}. Searching for column.")
				upperr = 0
				lowerr = 7
				rangerow = 8
			else:
				column = upperr
				print(f"Column found: {column}.")
		
	seatID = row * 8 + column
	allIDs.append(seatID)
	print(f"SeatID is {seatID}")
	print(f"Final values for {passline}:{row}, {column}, {seatID}")
allIDs = sorted(allIDs)
print(f"Of all checked IDs, the highest value is {max(allIDs)}.")

listposition = 0
for a in allIDs:
	listposition += 1
	if listposition > len(allIDs):
		print("Reached end of list.")
		break
	if allIDs[listposition] - a == 2:
		print(f"Our SeatID: {a + 1}")
		break