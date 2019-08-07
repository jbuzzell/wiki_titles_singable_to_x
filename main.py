import auth
import wikipedia
import re
import os
import random

api = auth.auth()
random.seed()


def post():

    title = find_wiki_page(6)
    title_url = 'https://en.wikipedia.com/wiki/' + title.replace(" ", "_")

    status = api.update_with_media("img/" + get_random_image(), status=title)
    api.update_status(title_url, in_reply_to_status_id=status._json["id"])


def find_wiki_page(syllable_constraint=5):

    while True:

        tmp = wikipedia.random()

        if syllable_count(tmp) == syllable_constraint\
                and not forbidden_phrases_in_result(tmp)\
                and re.search(r'\d{4}', tmp) is None\
                and re.search(r' [A-Z]{2,} ', tmp) is None:

            return tmp


def get_random_image():
    return os.listdir("img/")[random.randint(0, len(os.listdir("img/")) - 1)]


def forbidden_phrases_in_result(result):

    with open("forbidden_phrases.txt") as f:
        content = f.readlines()

    content = [line.rstrip('\n') for line in content]

    for phrase in content:
        if phrase in result:
            return True

    return False


# from Jeremy McGibbon @ https://stackoverflow.com/questions/46759492/syllable-count-in-python
def syllable_count(word):

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


if __name__ == "__main__":   
    post()
