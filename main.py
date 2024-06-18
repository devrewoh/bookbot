def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_wordcount(text)
    char_dict = get_charcount(text)
    converted_dictionary = convert_dict_to_list(char_dict)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    
    for item in converted_dictionary:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']} character was found {item['num']} times")
    print("--- End Report ---")

#returns book text from path
def get_book_text(path):
    with open(path) as f:
        return f.read()

#get word count
def get_wordcount(text):
    words = text.split()
    return len(words)

#get character count 
def get_charcount(text):
    char_count_dict = {}
    for char in text:
        lowered_char = char.lower()
        if char in char_count_dict:
            char_count_dict[lowered_char] += 1
        else:
            char_count_dict[lowered_char] = 1
    return char_count_dict

def convert_dict_to_list(char_dict):
    sorted_list = []
    for char in char_dict:
        sorted_list.append({"char": char, "num": char_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

#sort function
def sort_on(dict):
    return dict["num"]


main()