import sys

from stats import count_words
from stats import count_characters
from stats import sort_dict

def get_book_text(path):
    with open(path) as file:
        return file.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = sys.argv[1]
    text = get_book_text(book)

    num_words = count_words(text)
    character_count = count_characters(text)

    sorted_list = sort_dict(character_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in sorted_list:
        print(f"{dict["character"]}: {dict["amount"]}")
    print("============= END ===============")

main()