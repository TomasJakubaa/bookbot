from stats import count_characters
from stats import count_words

def main():

	def get_book_text(file_path):
		with open(file_path) as file:
			return file.read()

	path_to_file = "books/frankenstein.txt"
	words_counted = count_words(get_book_text(path_to_file))
	characters_counted = count_characters(get_book_text(path_to_file))

	print(f"{words_counted} words found in the document")
	print(characters_counted)

main()
