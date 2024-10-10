def main():
    book_path = "./books/frankenstein.txt"
    text = print_book(book_path)
    word_count = count_words(text)
    char_dict = count_characters(text)
    sort_on(char_dict)
    char_list = book_report(char_dict)
    print("--- Begin report of books/frankenstien.txt ---")
    print(f'{word_count} words found in this book.')
    print()
    print_char_count(char_list)
    print("--- End Report ---")

def print_book(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    chars = {}
    lower_text = text.lower()
    for letter in lower_text:
        if letter in chars:
            chars[letter] += 1
        else:
            chars[letter] = 1
    return chars

def sort_on(dict):
    for c in dict:
        return dict[c]
    
def book_report(dict):
    report = []
    for c in dict:
        if c.isalpha():
            report.append({c: dict[c]})
    report.sort(reverse=True, key=sort_on)
    return report

def print_char_count(list):
    for dict in list:
        for key, value in dict.items():
            print(f"The '{key}' character was found {value} times")

main()


 