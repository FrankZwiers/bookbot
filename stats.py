def count_words(text):
    return len(text.split())

def count_characters(text):
    dict = {}
    for char in text:
        lchar = char.lower()
        if not lchar in dict:
            dict[lchar] = 0

        dict[lchar] += 1

    return dict

def sort_on(dict):
    return dict["amount"]

def sort_dict(dict):
    list = []
    for char in dict.keys():
        if (char.isalpha()):
            list.append({"character": char, "amount": dict[char]})

    list.sort(reverse=True, key=sort_on)
    return list