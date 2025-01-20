def get_book_text(path): #function to obtain a string of text from a path file
    with open(path) as f:
        return f.read()

def word_counter(input_string): # function to count the words ommiting whitespace from an input string
    words = input_string.split()
    return len(words)

def char_counter(input_string): # function to create a dictionary of the occurance of all characters in an input string (standardised to lowercase)
    char_dict = {}
    for char in input_string:
        lowercase_char = char.lower()
        if lowercase_char not in char_dict:
            char_dict[lowercase_char] = 1
        else:
            char_dict[lowercase_char] += 1   
    return char_dict

def report(path, text): # function to generate a formatted report using previous functions

    print(f"--- Begin report of {path} ---")
    print(f"{word_counter(text)} words found in the document")
    print()


    base_char_dict = char_counter(text)
    char_dict_list = []

    for char_key in base_char_dict:
        dict_list_element = {"symbol":char_key,"number":base_char_dict[char_key]}
        char_dict_list.append(dict_list_element)

    def sort_on(dict):
        return dict["number"]
    
    char_dict_list.sort(reverse=True, key=sort_on)

    for element in char_dict_list:
        if element["symbol"].isalpha():
            print(f"The '{element["symbol"]}' character was found {element["number"]} times") 

    print("--- End report ---")
    return

def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    
    return report(path,text)

main()