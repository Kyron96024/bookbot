from stats import get_word_count, get_each_char, make_sorted_dict

def get_book_text():
    with open("/home/gergo/workspace/github.com/BOOTDOTDEV/bookbot/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents



def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    text = get_book_text()
    num_words = get_word_count(text)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    dict_chars = get_each_char(text)
    sorted_dic = make_sorted_dict(dict_chars)
    for dic in sorted_dic:
        if dic["char"].isalpha():
            print(f"{dic["char"]}: {dic["num"]}")
    print("============= END ===============")

main()