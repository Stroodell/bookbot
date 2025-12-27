def get_word_count(path_to_file):
    with open(path_to_file) as f:
        content = f.read()
    words = content.split()
    return len(words)

def get_character_count(path_to_file):
    with open(path_to_file) as f:
        content = f.read()
    no_dublicates = content.lower()

    count = {}
    for character in no_dublicates:
        if character not in count:
            count[character] = 1
        else:
            count[character] += 1
    return count

def sort_on(items):
    return items["num"]

def get_sorted_list(characters):
    char_sort = []
    for key in characters:
        char_dic = {"char": key, "num": characters[key]}
        char_sort.append(char_dic)

    char_sort.sort(reverse=True, key=sort_on)
    return char_sort


