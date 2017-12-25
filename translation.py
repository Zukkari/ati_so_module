from googletrans import Translator

from configuration import get_node_value


# Translation module: http://py-googletrans.readthedocs.io/en/latest/

def translate_sentence(sentence):
    return Translator().translate(text=sentence, src=get_node_value("languages:from"),
                                  dest=get_node_value("languages:to")).text
