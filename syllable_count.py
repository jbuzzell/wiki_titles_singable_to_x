import re
import json
import requests
import auth


def syllable_count(word):

    special_cases = check_special_pronunciation(word)
    count = special_cases[0]

    for w in special_cases[1]:
        count += get_syllables(w)

    return count


def check_special_pronunciation(title):
    words = title.split(' ')
    year = re.compile(r'^\d{4}$')
    abbr = re.compile(r'^[A-Z]{2,}$')
    count = 0

    for w in words:
        if year.match(w):
            count += parse_year(w)
        elif abbr.match(w):
            count += parse_abbr(w.lower())

    word_slice = [w for w in words if year.match(w) is None and abbr.match(w) is None]

    return count, word_slice


def parse_abbr(abbr):
    count = 0

    for i in abbr:
        if i == 'w':
            count += 3
        else:
            count += 1

    return count


def parse_year(year):
    with open("pronounciation_rules.json") as f:
        json_str = f.read()
        rules = json.loads(json_str)

    year_l = year[0:2]
    year_r = year[2:]
    count = 0

    for r in rules.items():
        test = re.compile(r[0])

        if test.match(year_l) or test.match(year_r):
            count += r[1]

    return count


# from Jeremy McGibbon @ https://stackoverflow.com/questions/46759492/syllable-count-in-python
    # THIS IS A FALLBACK IN CASE THE WORD IS NOT IN THE DICTIONARY
def parse_generic(word):

    word = word.lower()
    count = 0
    vowels = "aeiouy"

    if word[0] in vowels:
        count += 1

    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1

    if word.endswith("e"):
        count -= 1
    if count == 0:
        count += 1

    return count


def get_syllables(word):

    request = requests.get("https://www.dictionaryapi.com/api/v3/references/collegiate/json/" + word,
                           params={"key": auth.mw_key})

    if len(request.json()) != 0 and type(request.json()[0]) is not str:
        return len(request.json()[0]["hwi"]["hw"])
    else:
        return parse_generic(word)


if __name__ == "__main__":
    syllable_count("1977 Big Wow Convention")
