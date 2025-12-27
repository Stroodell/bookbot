import sys

from stats import get_word_count, get_character_count, get_sorted_list

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        content = f.read()
    return content

def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    
    #file_path = "books/frankenstein.txt"
    #print(get_book_text(file_path))
    #print(f"Found {get_word_count(file_path)} total words")
    

    """
    word_count = get_character_count(file_path)
    for key in word_count:
        count = word_count[key]
        print(f"'{key}': {count}")
    """
    word_count = get_character_count(file_path)
    sort_character = get_sorted_list(word_count)
    #print(sort_character)

    #Print Report

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(file_path)} total words")
    print("--------- Character Count -------")


    for entry in sort_character:
        if entry.get("char").isalpha():
            print(f"{entry.get("char")}: {entry.get("num")}")
  
main()
    
