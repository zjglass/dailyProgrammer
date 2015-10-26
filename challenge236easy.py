import random

def main():
	#assign tetriminos, cache, and output list
	tetriminos = ["O", "I", "S", "Z", "L", "J", "T"]
	cache = [0,1,2,3,4,5,6]
	output = []

	#i iterations 
	i = 50

	while (i>0):
		#append, to output, the tetrimino at index (randomly popped value from cache).	
		output.append(tetriminos[cache.pop(random.randint(0, (len(cache)-1)))])
		i -= 1

		if cache == []:
			cache = [0,1,2,3,4,5,6]

	print(output)

main()