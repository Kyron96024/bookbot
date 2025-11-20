def get_word_count(text):
    text_list = text.split()
    counter = 0
    for word in text_list:
        counter += 1
    return counter

def get_each_char(text):
    char_dict = {}
    for char in text:
        if char.lower() in char_dict.keys():
            char_dict[char.lower()] += 1
        else:
            char_dict[char.lower()] = 1
    return char_dict