from stats import count_words, count_characters, sort_char_counts


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    # print(get_book_text("./books/frankenstein.txt"))
    book = get_book_text("./books/frankenstein.txt")
    total_words = count_words(book)
    char_counts = count_characters(book)
    sorted_char_report = sort_char_counts(char_counts)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")

    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")

    print("--------- Character Count -------")
    for item in sorted_char_report:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


main()