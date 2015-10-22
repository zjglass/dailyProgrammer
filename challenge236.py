import random

def resetBag(bag):
	bag = {1:["O",True], 2:["I",True], 3:["S",True], 4:["Z",True], 5:["L",True], 6:["J",True], 7:["T",True]}

def getPiece(bag):
	switch = True
	while switch:
		index = random.randint(1,7)
		
		if bag[index][1] == True:
			bag[index][1] = False
			switch = False
			return bag[index][0]

def main():
	#initialize bag and output string
	bag = {}
	resetBag(bag)
	output = ""

	#50 iterations
	i = 50
	while i > 0:
		
		if ((i+6)%7) == 0: 
			resetBag(bag)
		
		output += getPiece(bag)

	print(output)
	input("Done!")

main()