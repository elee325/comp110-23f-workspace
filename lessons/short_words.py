def short_words(list1: list[str]) -> list[str]:
    """Returns list of words that are shorter than 5 characters."""
    list2: list[str] = []
    for word in list1:
        if len(word) < 5:
            list2.append(word)
        else:
            print(f"{word} is too long!")
    return list2

my_list : list [str ] = ["sun", "cloud", "sky"]
print(short_words(my_list))