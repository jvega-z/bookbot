import sys
from stats import count_words, count_characters, sort_char_counts


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    if (len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        # print(get_book_text("./books/frankenstein.txt"))
        book = get_book_text(sys.argv[1])
        total_words = count_words(book)
        char_counts = count_characters(book)
        sorted_char_report = sort_char_counts(char_counts)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}")

        print("----------- Word Count ----------")
        print(f"Found {total_words} total words")

        print("--------- Character Count -------")
        for item in sorted_char_report:
            if item['char'].isalpha():
                print(f"{item['char']}: {item['num']}")

        print("============= END ===============")
    


main()