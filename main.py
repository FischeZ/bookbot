import sys

from stats import word_count
from stats import char_count
from stats import sorted_list_of_dict

def get_book_text(filepath):
    book_text = ""
    with open(filepath) as file:
        book_text = file.read()

    return book_text

def sort_and_print_dict(dict_to_sort):
    sorted_items = sorted_list_of_dict(dict_to_sort)
    for item in sorted_items:
        if(item['char'].isalpha()):
            print(f"{item['char']}: {item['num']}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    text = get_book_text(file_path)
    num_words = word_count(text)
    ch_count = char_count(text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    sort_and_print_dict(ch_count)
    print("============= END ===============")
    
main()