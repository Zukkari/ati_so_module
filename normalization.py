import json
import urllib.request

from configuration import get_node_value


def normalize_word(word):
    word = word.replace(get_node_value("normalize:replacements"), "")

    url = get_node_value("normalize:normalization_url")
    file = urllib.request.urlopen(url.format(urllib.parse.quote(word)))
    res = json.loads(file.read().decode())
    return res['root']


def normalize(text):
    if get_node_value("normalize:enabled"):
        sentence_words = text.split()
        normalized = []

        for word in sentence_words:
            normalized.append(normalize_word(word))

        return " ".join(normalized)
    else:
        return text
