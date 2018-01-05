import wikipedia
from difflib import SequenceMatcher


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


def read_and_clean_data():
    content = wikipedia.page("List_of_programming_languages")
    data = content.links

    list_of_languages = []

    for element in data:
        list_of_languages.append(element)

    to_be_cleaned = list(filter(lambda k: '(programming language)' in k, list_of_languages))
    list_one = list(filter(lambda k: '(programming language)' not in k, list_of_languages))
    list_two = list(map(lambda x: x.split(" (")[:-1][0], to_be_cleaned))

    return list_one + list_two

def tag_finder(lause):
    best_match = ""
    best_percentage = 0
    list_of_languages = read_and_clean_data()

    for language in list_of_languages:
        for word in lause.split(" "):
            percentage = round(similar(language.lower(), word.lower()) * 100, 2)
            if percentage == 100.00:
                return language

            if percentage > best_percentage:
                best_percentage = percentage
                best_match = language

    return best_match
