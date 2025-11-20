def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    ch_dict = {}
    for ch in text:
        lower_ch = ch.lower()
        if lower_ch in ch_dict:
            ch_dict[lower_ch] += 1
        else:
            ch_dict[lower_ch] = 1
    return ch_dict

def sort_on(items):
    return items["num"]

def sorted_list_of_dict(input_dict):
    char_num_list = []
    for item in input_dict:
        char_num_list.append({"char": item, "num": input_dict[item]})

    char_num_list.sort(key=sort_on, reverse=True)
    return char_num_list