from configuration import get_node_value
import urllib.request


def form_api_url(query):
    return get_node_value("stack_app:url").format(
        get_node_value("stack_app:version"),
        get_node_value("stack_app:method"),
        get_node_value("stack_app:site"),
        urllib.parse.quote(query)
    )

def get_answer_from_api(question, tag):
    pass