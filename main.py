import sys
from stats import get_word_count, get_each_char, make_sorted_dict

def get_book_text():
    with open(sys.argv[1]) as f:
        file_contents = f.read()
    return file_contents



def main():
    if len(sys.argv) == 2:
        print("============ BOOKBOT ============")
        path = sys.argv[1]
        print(f"Analyzing book found at {path}...")
        print("----------- Word Count ----------")
        text = get_book_text()
        print(text.count("e")+text.count("E"))
        num_words = get_word_count(text)
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        dict_chars = get_each_char(text)
        sorted_dic = make_sorted_dict(dict_chars)
        for dic in sorted_dic:
            if dic["char"].isalpha():
                print(f"{dic["char"]}: {dic["num"]}")
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()