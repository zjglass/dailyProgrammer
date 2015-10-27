import copy

# checks to see if the top board in the boardStack is full. If it isn't, it calls move(), 
# then calls itself
def solve(boardStack):
	if isComplete(boardStack[-1]):
		print("Done!")
		return True
	else:
		move(boardStack)
		solve(boardStack)
		

# checks to see if the board if full. Returns True if it is, and False if it isn't
def isComplete(config):
	for row in range(len(config)):
		for col in range(len(config[row])):
			if config[row][col] == ".":
				return False	
	return True

def move(boardStack):
	curBoard = boardStack.pop()
	for row in range(len(curBoard)):
		for col in range(len(curBoard[row])):
			moveMade = False
			if config[row][col] == ".":
				newBoard0 = copy.deepcopy(curBoard)
				newBoard1 = copy.deepcopy(curBoard)
				newBoard0[row][col], newBoard1[row][col] = 0, 1
				if isValid(newBoard0):
					boardStack.append(newBoard0)
					moveMade = True
				if isValid(newBoard1):
					boardStack.append(newBoard1)
					moveMade = True
			if moveMade:
				return 


# check to see if the config passed in follows the rules of the game
def isValid(config):
	print("nope")

# returns the data at a given row.
# the data returned is not the real row, but a mirror of it
# modifying it will do nothing to the config
def getRowData(config, row):
	data = []
	for space in config[row]:
		data.append(space)
	return data

# returns the data at a given col
# the data returned is not the real col, but a mirror of it
# modifying it will do nothing to the config
def getColData(config, col):
	data = []
	for row in config:
		data.append(row[col])
	return data

# returns the number of ones or zeroes in a row
def onesOrZerosInRow(config, switch, row):
	count = 0
	for spot in getRowData(config, row):
		if switch == 1:
			if spot == "1":
				count += 1
		if switch == 0:
			if spot == "0":
				count += 1
	return count

# returns the number of ones or zeroes in a row
def onesOrZerosInCol(config, switch, col):
	count = 0
	for spot in getColData(config, col):
		if switch == 1:
			if spot == "1":
				count += 1
		if switch == 0:
			if spot == "0":
				count += 1
	return count 


def isFullRowOrCol(line):
	for spot in line:
		if spot == ".":
			return False
	return True

# returns True if rowData is full, and a duplicate of another full row in config
def isDuplicateRow(config, rowData):
	if isFullRowOrCol(rowData) != True:
		return False

	count = 0
	for row in config:
		if row == rowData:
			count += 1
		if count > 1:
			return True
	return False


# returns True if colData is full, and a duplicate of another full col in config
def isDuplicateCol(config, colData):
	if isFullRowOrCol(colData) != True:
		return False

	count = 0
	for i in range(len(config)):
		if getColData(config, i) == colData:
			count += 1
		if count > 1:
			return True
	return False

# prints out the config all nice and purdy-like
def prettyPrint(config):
	output = ""
	for row in config:
		output = ""
		for spot in row:
			output += spot
		print(output)

# Modify config to change input board before run
# solves, then prettyPrints config
def main():
	print("Lets do this!")
	config = [[".", ".", ".", "."],["0",".","0","."],[".",".","0","."],[".",".",".","1"]]
	boardStack = []
	boardStack.append(config)

	solve(boardStack)
	prettyPrint(boardStack[-1])
		

main()