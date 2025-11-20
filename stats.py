def get_word_count(text):
    text_list = text.split()
    counter = 0
    for word in text_list:
        counter += 1
    return counter

def get_each_char(text):
    list_dict = []
    char_dict = {}
    for char in text:
        if char.lower() in char_dict.keys():
            char_dict[char.lower()] += 1
        else:
            char_dict[char.lower()] = 1
    for char in char_dict:
        one_dict = {}
        one_dict["char"] = char
        one_dict["num"] = char_dict[char]
        list_dict.append(one_dict)
    return list_dict

def sort_on(item):
    return item["num"]

def make_sorted_dict(dict_char_count):
    dict_char_count.sort(reverse=True, key=sort_on)
    return dict_char_count