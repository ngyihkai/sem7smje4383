def make_word_list (a_file) :
	"""Create a list of words from the file."""
	word_list = [] # list of speech words: initialized to be empty
	for line_str in a_file:
		line_list = line_str.split()
		for word in line_list:
			if word != "--": #split each line into a list of words #get words one at a time from list #if the word is not
				word_list.append(word)
	return word_list

