def get_book(book):
    with open(book) as f:
         return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def get_letter_count(text):
    chars = {}
    for c in text:
        low_text = c.lower()
        if low_text in chars:
            chars[low_text] += 1
        else:
            chars[low_text] = 1
    return chars

def sort_on(dict):
    return dict["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def main():
    book_path = "books/frankenstein.txt"
    book = get_book(book_path)
    word_count = get_word_count(book)
    letter_count = get_letter_count(book)
    chars_sorted_list = chars_dict_to_sorted_list(letter_count)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
    print(f"--- End report ---")
    print(f"{letter_count}")

main()
