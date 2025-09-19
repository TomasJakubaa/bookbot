import stats

def main():

	path_to_file = "books/frankenstein.txt"
	book_text = stats.get_book_text(path_to_file)
	words_counted = stats.count_words(book_text)
	characters_counted = stats.count_characters(book_text)
		# python
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {path_to_file}...")
	print("----------- Word Count ----------")
	print(f"Found {words_counted} total words")
	print("--------- Character Count -------")

	sorted_chars = stats.sorted_list_dictionaries(characters_counted)
	for entry in sorted_chars:
		ch = entry["char"]
		if ch.isalpha():
			print(f"{ch}: {entry['num']}")

	print("============= END ===============")


main()
