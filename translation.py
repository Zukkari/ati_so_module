from googletrans import Translator

from configuration import get_node_value


# Translation module: http://py-googletrans.readthedocs.io/en/latest/

def translate_sentence(sentence):
    if get_node_value("translation:enabled"):
        return Translator().translate(text=sentence, src=get_node_value("translation:languages:from"),
                                      dest=get_node_value("translation:languages:to")).text
    else:
        return sentence
