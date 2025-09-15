from stats import sorted_list_dictionaries
from stats import count_characters
from stats import count_words

def main():

	def get_book_text(file_path):
		with open(file_path) as file:
			return file.read()

	path_to_file = "books/frankenstein.txt"
	book_text = get_book_text(path_to_file)
	words_counted = count_words(book_text)
	characters_counted = count_characters(book_text)
		# python
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {path_to_file}...")
	print("----------- Word Count ----------")
	print(f"Found {words_counted} total words")
	print("--------- Character Count -------")

	sorted_chars = sorted_list_dictionaries(characters_counted)
	for entry in sorted_chars:
   		ch = entry["char"]
    	if ch.isalpha():
        	print(f"{ch}: {entry['num']}")

	print("============= END ===============")
	

main()
