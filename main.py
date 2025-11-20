from stats import get_word_count, get_each_char

def get_book_text():
    with open("/home/gergo/workspace/github.com/BOOTDOTDEV/bookbot/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents



def main():
    text = get_book_text()
    num_words = get_word_count(text)
    print(f"Found {num_words} total words")
    dict_chars = get_each_char(text)
    print(dict_chars)

main()