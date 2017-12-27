import gzip
import json
import urllib.request

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


def get_answer_from_api(question, tag):
    data = load_response(question, tag)

    keywords = question.split()

    # Take questions that have been answered and that are relevant to the language we are looking for
    filtered = filter(lambda data: data["is_answered"] and tag in data["tags"], data)

    contains_keywords = group_by_keywords(keywords, filtered)

    relevance = sorted(contains_keywords.keys(), reverse=True)[0]
    best_option = contains_keywords[relevance]

    return best_option, relevance


def load_response(question, tag):
    url = form_api_url(question, tag)
    file = urllib.request.urlopen(url)
    with gzip.open(file, "rb") as f:
        data = json.loads(f.read().decode())['items']
    return data


print(get_answer_from_api("add element to array", "python"))
