from stats import get_num_words
from stats import get_num_letter
from stats import get_final_result
import sys

def main():
    if len(sys.argv) != 2:
      print("Usage: python3 main.py <path_to_book>")
      sys.exit(1)
      
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    dict = get_num_letter(text)
    dict2 = get_final_result(dict)
    
    
    # FINAL PRINTING
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in dict2:
      if item["name"].isalpha() == True:
        letter = item["name"]
        count = item["num"]
        print(f"{letter}: {count}")
    print("============= END ===============")


    

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()



