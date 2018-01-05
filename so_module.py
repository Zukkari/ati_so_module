from language import tag_finder
from normalization import normalize
from translation import translate_sentence
from query import get_answer_from_api


def get_response(text, initiative, topic):
    normalized_text = normalize(text)
    translated_text = translate_sentence(normalized_text)
    language = tag_finder(normalized_text.lower())

    return get_answer_from_api(translated_text, language, text)