def main():
    num_of_words(return_content())
    num_of_char_in_text(return_content())

    report(num_of_words(return_content()), num_of_char_in_text(return_content()))



def return_content():
    book = "books/frankenstein.txt"
    with open(book) as f:
        file_contents = f.read()
        return file_contents


def num_of_words(file_conts):
    words = file_conts.split()
    return len(words)


def num_of_char_in_text(file_conts):
    char_num_dict = {}
    file_conts = file_conts.lower()
    for char in file_conts:
        if char in char_num_dict:
            char_num_dict[char] += 1
        else:
            char_num_dict[char] = 1
    return char_num_dict

def report(words, chars):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document")
    keys = chars.keys()
    keys = list(keys)
    number_value = chars.values()
    number_value = list(number_value)
    for i in range(len(chars)):
        print(f"The '{keys[i]}' character was found {number_value[i]} times")
    
main()