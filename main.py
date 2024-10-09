def main():
    book_path = "./books/frankenstein.txt"
    text = print_book(book_path)
    word_count = count_words(text)
    return print(word_count)


def print_book(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def count_words(text):
    words = text.split()
    return len(words)

main()
 

# boot-dev solution:
# def main():
#     book_path = "books/frankenstein.txt"
#     text = get_book_text(book_path)
#     print(text)


# def get_book_text(path):
#     with open(path) as f:
#         return f.read()


# main()