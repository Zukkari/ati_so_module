from normalization import normalize
from translation import translate_sentence


def get_response(text):
    # TODO
    # Steps to follow:
    # 1. Normalize message if normalization is enabled
    normalized_text = normalize(text)
    # 2. Translate message using translation url from conf
    translated_text = translate_sentence(normalized_text)
    # 3. Query stack overflow API for result using translated message
    print(translated_text)
    # 4. Parse response for result
    # 5. Rate response relevance

    return "response", 1.0
