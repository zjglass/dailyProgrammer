def main():
	#open enable1.txt
	dictionary = open('enable1.txt','r')
	
	inputs = []
	
	#get paramaters
	i = int(input("How many keyboards?"))
	while i > 0:
		inputs.append(input("Enter a keyboard..."))
		i -= 1

	#for each keyboard, loop over dictionary and add longest typable word to outputs 
	for keyboard in inputs:
		longestWord = ""

		#loop over words
		for word in dictionary:
			word = word.strip()
			skip = False

			#loop over the letters in each word
			for letter in word:
				#if the word can't be typed, flag it for skipping
				if letter not in keyboard:
					
					skip = True
				
			#if the word was found to be untypable, skip it. Otherwise, if it
			#was longer than the current longestWord, set it as longestWord
			if skip == True:
				continue

			if len(word) > len(longestWord):
				longestWord = word
		
		#print result
		print(keyboard, " = ", longestWord)
			
	#pause at end for viewing
	input("Done!")

main()