def count_words(string_file):
	count = 0
	words = string_file.split()
	for word in words:
		count += 1
	return count

def count_characters(string_file):
	dictionary = {}
	lower_string_file = string_file.lower()
	for character in lower_string_file:
		if character in dictionary:
			dictionary[character] += 1
		else:
			dictionary[character] = 1
	return dictionary
