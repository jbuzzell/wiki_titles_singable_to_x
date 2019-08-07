import auth
import wikipedia
import os
import random
import syllable_count

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

        if syllable_count.syllable_count(tmp) == syllable_constraint\
                and not forbidden_phrases_in_result(tmp):

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


if __name__ == "__main__":   
    print(find_wiki_page(6))
