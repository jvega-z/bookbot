def count_words(text):
    return len(text.split())


def count_characters(text):
    char_count = {}
    for char in text:
        lower_char = char.lower()
        if lower_char in char_count:
            char_count[lower_char] += 1
        else:
            char_count[lower_char] = 1
    return char_count


def sort_on(items):
    return items["num"]


def sort_char_counts(char_count_dict):
    report = []
    for character, count in char_count_dict.items():
        report.append({"char": character, "num": count})
    report.sort(reverse=True, key=sort_on)
    return report




