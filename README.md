# University of Tartu StackOverflow chatbot module

## About the project:
Chat bot module for bigger chat bot made in AI course in University of Tartu.

Purpose of this module is to take input as sentence as text, process it and output a response with a rate how good the reponse is for the given sentence.

## Functionality:
Our module does the following things:

* Normalizes the message (if this is enabled the configuration)
* Translates the message into the language defined in the configuration
* Queries stackoverflow for the question
* Parses the response and rates how good the response is for the asked question.

## Dependecies:
Our module uses the following dependencies:

For translations we use module found [here](http://py-googletrans.readthedocs.io/en/latest/):

```pip install googletrans```

Also we use the [following](http://prog.keeleressursid.ee/ws_etmrf/lemma.php) service for message normalization.
