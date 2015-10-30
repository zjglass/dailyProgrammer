import copy

# checks to see if the top board in the boardStack is full. If it isn't, it calls move(), 
# then calls itself
def solve(boardStack):
	if isComplete(boardStack[-1]):
		print("Done!")
		return True
	else:
		makeMoves(boardStack)
		solve(boardStack)
		

# checks to see if the board if full. Returns True if it is, and False if it isn't
def isComplete(config):
	for row in range(len(config)):
		for col in range(len(config[row])):
			if config[row][col] == ".":
				return False	
	return True

def makeMoves(boardStack):
	curBoard = boardStack.pop()
	movesMade = 0

	queuedMoves = checkDoubles(curBoard)
	for move in queuedMoves:
		curBoard[move[1]][move[2]] = move[0]
		movesMade += 1
		prettyPrint(curBoard)
		print("____________")

	for move in checkSandwiches(curBoard):
		curBoard[move[1]][move[2]] = move[0]
		prettyPrint(curBoard)
		print("____________")
	for move in checkNumComplete(curBoard):
		curBoard[move[1]][move[2]] = move[0]
		prettyPrint(curBoard)
		print("____________")
	for move in complementSimilarRow(curBoard):
		curBoard[move[1]][move[2]] = move[0]
		prettyPrint(curBoard)
		print("____________")
	for move in complementSimilarCol(curBoard):
		curBoard[move[1]][move[2]] = move[0]
		prettyPrint(curBoard)
		print("____________")
	boardStack.append(curBoard)
	

	#eventually, once logic inplementation is finished, this will make all possible valid moves
	#on the mostly filled in board, backtracking when no more valid moves can be made and the board
	#is not complete. this will eventually result in a valid, complete, board. this will only come
	#into play when all logic has failed.
	#
	#for row in range(len(curBoard)):
	#	for col in range(len(curBoard[row])):
	#		moveMade = False
	#		if config[row][col] == ".":
	#			newBoard0 = copy.deepcopy(curBoard)
	#			newBoard1 = copy.deepcopy(curBoard)
	#			newBoard0[row][col], newBoard1[row][col] = "0", "1"
	#			if isValid(newBoard0):
	#				boardStack.append(newBoard0)
	#				moveMade = True
	#			if isValid(newBoard1):
	#				boardStack.append(newBoard1)
	#				moveMade = True
	#		if moveMade:
	#			return 

#returns either a list of 3-tuples [(<0 or 1>, <row>, <col>), ...]
# or an empty list
def checkDoubles(config):
	print("doubles sweep!")
	moveList = []
	for row in range(len(config)):
		for col in range(len(config)):
			
			#if we're not at the last row, where this is irrelevant
			if row+1 <= len(config)-1 :
				#if there is a vertical double number?
				if (config[row][col] != ".") and (config[row][col] == config[row+1][col]):
					#if we're not on the first row and about to negative index
					if (row-1 >= 0):
						#if the spot above us is unpopulated
						if config[row-1][col] == ".":
							#add moves to moveList!
							if config[row][col] == "1":
								moveList.append(("0", (row-1), col))
							else:
								moveList.append(("1", (row-1), col))
					#if we're not on the second to last row and about to index out of range
					if (row+2 < len(config)):
						#if the spot below the double is unpopulated
						if config[row+2][col] == ".":
							#add moves to moveList
							if config[row][col] == "1":
								moveList.append(("0", (row+2), col))
							else:
								moveList.append(("1", (row+2), col))

			#if we're not at the last col, where this is irrelevant
			if col+1 <= len(config)-1 :
				#if there is a horizontal double number?
				if (config[row][col] != ".") and (config[row][col] == config[row][col+1]):
					#if we're not on the first col and about to negative index
					if (col-1 >= 0):
						#if the spot left of us is unpopulated
						if config[row][col-1] == ".":
							#add moves to moveList!
							if config[row][col] == "1":
								moveList.append(("0", row, (col-1)))
							else:
								moveList.append(("1", row, (col-1)))
					#if we're not on the second to last col and about to index out of range
					if (col+2 < len(config)):
						#if the spot right of the double is unpopulated
						if config[row][col+2] == ".":
							#add moves to moveList
							if config[row][col] == "1":
								moveList.append(("0", row, (col+2)))
							else:
								moveList.append(("1", row, (col+2)))
	return moveList						

# returns moves in the fashion of checkDoubles(), but these moves will fill in
# meatless number sandwiches!
def checkSandwiches(config):
	print("sandwich sweep!")
	moveList = []
	for row in range(len(config)):
		for col in range(len(config)):
			
			#if we're not at or near the last row, where this is irrelevant
			if row+2 <= len(config)-1 :
				#if there is a vertical number sandwich without number meat?
				if (config[row][col] != ".") and (config[row][col] == config[row+2][col]) and (config[row+1][col] == "."):
					#add moves to moveList!
						if config[row][col] == "1":
							moveList.append(("0", (row+1), col))
						else:
							moveList.append(("1", (row+1), col))
			#if we're not at or near the last col, where this is irrelevant
			if col+2 <= len(config)-1 :
				#if there is a horizontal number sandwich without number meat?
				if (config[row][col] != ".") and (config[row][col] == config[row][col+2]) and (config[row][col+1] == "."):
					#add moves to moveList!
						if config[row][col] == "1":
							moveList.append(("0", row, (col+1)))
						else:
							moveList.append(("1", row, (col+1)))

	return moveList						


def checkNumComplete(config):
	print("number complete sweep!")
	moveList = []
	for i in range(len(config)):
		if isFullLine(getRowData(config, i)) == False:
			if onesOrZerosInRow(config, 0, i) == .5*len(config):
				for col in range(len(config)):
					if config[i][col] == ".":
						moveList.append(("1", i, col))
			if onesOrZerosInRow(config, 1, i) == .5*len(config):
				for col in range(len(config)):
					if config[i][col] == ".":
						moveList.append(("0", i, col))
		if isFullLine(getColData(config, i)) == False:
			if onesOrZerosInCol(config, 0, i) == .5*len(config):
				for row in range(len(config)):
					if config[row][i] == ".":
						moveList.append(("1", row, i))
			if onesOrZerosInCol(config, 1, i) == .5*len(config):
				for row in range(len(config)):
					if config[row][i] == ".":
						moveList.append(("0", row, i))
	return moveList

def complementSimilarRow(config):
	print("complement similar rows!")
	moveList = []
	indicesList = []
	for num in range(len(config)):
		indicesList.append(num)

	for i in range(len(config)):
		curRow = getRowData(config, i)
		
		blanksInRow = 0
		 
		for col in range(len(curRow)):
			if curRow[col] == ".":
				blanksInRow += 1
				if blanksInRow > 2:
					break
		if blanksInRow == 2:
			for row in indicesList[i+1:]:
				testRow = getRowData(config, row)
				if isFullLine(testRow):
					differences = differencesInLine(curRow, testRow)
					if len(differences) == 2:
						moveList.append((differences[0][0], i, differences[0][1]))
						moveList.append((differences[1][0], i, differences[1][1]))

		
	return moveList

#
#
#
def complementSimilarCol(config):
	print("complement similar cols!")
	moveList = []
	indicesList = []
	for num in range(len(config)):
		indicesList.append(num)

	for i in range(len(config)):
		blanksInCol = 0
		curCol = getColData(config, i)
		for row in range(len(curCol)):
			if curCol[row] == ".":
				blanksInCol += 1
				if blanksInCol > 2:
					break
		if blanksInCol == 2:
			for col in indicesList[i+1:]:
				testCol = getColData(config, col)
				if isFullLine(testCol):
					differences = differencesInLine(curCol, testCol)
					if len(differences) == 2:
						moveList.append((differences[0][0], differences[0][1], i))
						moveList.append((differences[1][0], differences[1][1], i))

	return moveList

# check to see if the config passed in follows the rules of the game
#def isValid(config):
#	print("nope")


#returns False if the passed in lineData has blanks; else, returns True
def isFullLine(lineData):
	for spot in lineData:
		if spot == ".":
			return False
	return True

#takes in two sets of lineData
#	lineData1 = lineData to be tested
#	lineData2 = data to be tested against. MUST BE A FULL LINE.
#returns:
#	differences = a list of 2-tuples, in the format 
#		[(<the opposite of lineData2's value where a difference exists>,
#		<index of difference in lineData>), ...]
def differencesInLine(lineData1, lineData2):
	differences = []
	opposite = {"0":"1", "1":"0"}
	for spot in range(len(lineData1)):
		if lineData1[spot] != lineData2[spot]:
			differences.append((opposite[lineData2[spot]], spot))
	return differences
	

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


# returns True if rowData is full, and a duplicate of another full row in config
def isDuplicateRow(config, rowData):
	if isFullLine(rowData) != True:
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
	if isFullLine(colData) != True:
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
	config = []

	config.append([".",".",".","1",".","1",".",".",".",".","1","."])
	config.append(["0",".",".",".",".",".",".","0",".",".",".","0"])
	config.append([".",".","0","0",".",".",".",".",".",".","1","."])
	config.append([".","1",".",".",".",".",".",".",".",".",".","1"])
	config.append([".",".",".","1",".",".","0","0","1",".",".","."])
	config.append(["1",".","1","1",".","1",".","0",".",".","1","."])
	config.append([".",".",".",".",".",".","1",".",".",".","1","."])
	config.append(["0",".","0",".","1",".",".",".",".",".",".","."])
	config.append([".",".",".",".",".",".","0","1","0",".","1","."])
	config.append([".","0",".",".","1",".",".",".",".","1","1","."])
	config.append([".",".",".","0",".",".",".","1",".",".",".","."])
	config.append([".",".",".",".",".","0","0",".",".","0",".","."])

	boardStack = []
	boardStack.append(config)

	prettyPrint(config)
	print("____________")

	solve(boardStack)
	prettyPrint(boardStack[-1])
		

main()