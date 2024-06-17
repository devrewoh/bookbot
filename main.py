def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)
    print(f"Number of words counted in document: {get_wordcount(text)}")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_wordcount(text):
    words = text.split()
    return len(words)


main()