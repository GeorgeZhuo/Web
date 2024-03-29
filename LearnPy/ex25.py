def break_words(stuff):
    """This function will break sentence into words"""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sort the words"""
    return sorted(words)

def print_first_word(words):
    """Print the first word in the sentence"""
    word = words.pop(0)
    print word

def print_last_word(words):
    """Print the last word in the sentence"""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and return the sort words"""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

