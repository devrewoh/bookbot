def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)
    print(f"Number of words counted in document: {get_wordcount(text)}")
    print(f"Number of character instances counted in document: {get_charcount(text)}")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_wordcount(text):
    words = text.split()
    return len(words)

def get_charcount(text):
    lowered_string = text.lower()
    char_count_dict = {}
    for char in lowered_string:
        if char in char_count_dict:
            char_count_dict[char] += 1
        else:
            char_count_dict[char] = 1
    return char_count_dict



main()