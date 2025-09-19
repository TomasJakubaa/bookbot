import sys
import stats

def main():

	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	path_to_file = sys.argv[1]
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
