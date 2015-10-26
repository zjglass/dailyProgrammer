def solve(config):
	if isComplete(config):
		print("Done!")
	else:
		solve(makeValidMove(config))

def isComplete(config):
	for row in range(len(config)):
		for col in range(len(config[row])):
			if config[row][col] == ".":
				return False	
	return True


def makeValidMove(config):
	for row in range(len(config)):
		for col in range(len(config[row])):
			

def getRowData(config, row):
	data = []
	for space in config[row]:
		data.append(space)
	return data

def onesOrZerosInRow(config, row):
	count = 0
	for spot in getRowData(config, row):
		if spot = "1":
			count += 1
	return count



def getColData(config, col):
	data = []
	for row in config:
		data.append(row[col])
	return data

def main():
	print("Lets do this!")
	config = [[".", ".", ".", "."],["0",".","0","."],[".",".","0","."],[".",".",".","1"]]
	
	
	for row in config:
		print(row)


main()