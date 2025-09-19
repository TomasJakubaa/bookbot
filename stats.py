def get_book_text(file_path):
	with open(file_path) as file:
		return file.read()

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

def sorted_list_dictionaries(dictionary):
	def sort_on(item):
		return item["num"]
	list_dictionaries = []
	for char, count in dictionary.items():
		list_dictionaries.append({"char": char, "num": count})
	list_dictionaries.sort(reverse=True, key=sort_on)
	return list_dictionaries
