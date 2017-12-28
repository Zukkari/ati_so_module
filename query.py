import gzip
import json
import urllib.request
from html.parser import HTMLParser
from language import tag_finder

from configuration import get_node_value


def form_api_url(query, tag):
    return get_node_value("stack_app:url").format(
        get_node_value("stack_app:version"),
        get_node_value("stack_app:method"),
        get_node_value("stack_app:site"),
        urllib.parse.quote(query),
        urllib.parse.quote(tag)
    )


def group_by_keywords(keywords, items):
    dictionary = {}

    for item in items:
        matches = 0
        for keyword in keywords:
            if keyword in item['title']:
                matches += 1

        dictionary[matches / len(keywords)] = item

    return dictionary


def get_answer_ulr(id):
    return get_node_value('stack_app_answer:url').format(
        get_node_value('stack_app_answer:version'),
        get_node_value('stack_app_answer:method'),
        id,
        get_node_value('stack_app_answer:site')
    )


def load_answer(accepted_answer):
    url = get_answer_ulr(accepted_answer)
    file = urllib.request.urlopen(url)
    with gzip.open(file, "rb") as f:
        data = json.loads(f.read().decode())

    for person in data['items']:
        if person['is_accepted']:
            return person


class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.fed = []

    def handle_data(self, d):
        self.fed.append(d)

    def get_data(self):
        return ''.join(self.fed)


def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()


def parse_response(param):
    return strip_tags(param)


def form_nice_answer(best_option, answer, question):
    return get_node_value("answer:template").format(
        question,
        best_option['title'],
        best_option['link'],
        parse_response(answer['body'])
    )


def get_answer_from_api(question, tag):
    data = load_response(question, tag)

    keywords = question.split()

    # Take questions that have been answered and that are relevant to the language we are looking for
    filtered = list(filter(lambda data: data["is_answered"] and tag in data["tags"], data))

    if len(filtered) == 0:
        return get_node_value("answer:not_found"), 0.0

    contains_keywords = group_by_keywords(keywords, filtered)

    relevance = sorted(contains_keywords.keys(), reverse=True)[0]
    best_option = contains_keywords[relevance]

    accepted_answer = best_option['accepted_answer_id']
    answer = load_answer(accepted_answer)

    return form_nice_answer(best_option, answer, question), relevance


def load_response(question, tag):
    url = form_api_url(question, tag)
    file = urllib.request.urlopen(url)
    with gzip.open(file, "rb") as f:
        data = json.loads(f.read().decode())['items']
    return data


def preparing_question(question):
    tag = tag_finder(question).lower()

    print("Tag mida kasutame : " +str(tag))
    print("Küsimus : " +str(question))


    return get_answer_from_api(question, tag)



print(preparing_question("Java add element to array"))


