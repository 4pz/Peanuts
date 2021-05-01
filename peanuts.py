from datetime import date
import itertools
#from autocorrect import Speller

alphabet = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26
}

separator = ""


def get_key(val):
    for key, value in alphabet.items():
        if val == value:
            return key

    raise ValueError("Key Doesn't Exist")


def intersperse(lst, item):
    result = [item] * (len(lst) * 2 - 1)
    result[0::2] = lst
    return result


def reflect(text):
    split_text = [char for char in text]
    for letter in range(len(split_text)):
        try:
            if alphabet.get(split_text[letter]) < 14:
                corr_number = alphabet.get(split_text[letter]) + 13
                split_text[letter] = get_key(corr_number)
            elif alphabet.get(split_text[letter]) > 13:
                corr_number = alphabet.get(split_text[letter]) - 13
                split_text[letter] = get_key(corr_number)
        except:
            split_text[letter] = split_text[letter]

    return split_text


def date_shift(text):
    writing = reflect(text)
    shift = separator.join(str(date.today()).split("-"))
    split_shift = [i for i in shift]
    cycle = itertools.cycle(split_shift)

    for n in range(len(writing)):
        item = int(next(cycle))
        try:
            if alphabet.get(writing[n]) + item > 26:
                corr_number = alphabet.get(writing[n]) - item
                writing[n] = get_key(corr_number)
            else:
                corr_number = alphabet.get(writing[n]) + item
                writing[n] = get_key(corr_number)
        except:
            writing[n] = writing[n]

    return writing


def peanuts(text):
    dated = date_shift(text)
    for n in range(len(dated)):
        try:
            dated[n] = alphabet.get(dated[n]) * "#"
        except:
            if dated[n] == " ":
                dated[n] = "&"
            else:
                dated[n] = dated[n]

    return separator.join(intersperse(dated, "-"))

#print(peanuts("none"))


'''def undo_peanuts(text):
    new_text = text.split("-")
    for i in range(len(new_text)):
        if new_text[i] == "&":
            new_text[i] = " "
        elif "#" in new_text[i]:
            new_text[i] = get_key(len(new_text[i]))

    writing = new_text

    shift = separator.join(str(date.today()).split("-"))
    split_shift = [i for i in shift]
    cycle = itertools.cycle(split_shift)

    for n in range(len(writing)):
        item = int(next(cycle))
        try:
            if alphabet.get(writing[n]) + item > 26:
                corr_number = alphabet.get(writing[n]) + item
                writing[n] = get_key(corr_number)
            else:
                corr_number = alphabet.get(writing[n]) - item
                writing[n] = get_key(corr_number)
        except:
            writing[n] = writing[n]

    split_text = [char for char in writing]
    for letter in range(len(split_text)):
        try:
            if alphabet.get(split_text[letter]) > 14:
                corr_number = alphabet.get(split_text[letter]) - 13
                split_text[letter] = get_key(corr_number)
            elif alphabet.get(split_text[letter]) < 13:
                corr_number = alphabet.get(split_text[letter]) + 13
                split_text[letter] = get_key(corr_number)
        except:
            split_text[letter] = split_text[letter]

    spell = Speller()
    return spell(separator.join(split_text))


#print(undo_peanuts(peanuts("hello")))
'''