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

We also use the wikipedia module found [here](https://pypi.python.org/pypi/wikipedia/):

```pip install wikipedia```

Also we use the [following](http://prog.keeleressursid.ee/ws_etmrf/lemma.php) service for message normalization.

## Configuration:
Module can be configured using the ```config.json``` file in the root directory.

Currently those options can be configured:

* Text normalization:
  * can be enabled/disabled: ```"normalize": { "enabled": true/dalse }```
  * punctuation signs that will be stripped from the input text can be configured with ``` "normalize" : { "replacements": ";.,?!" }```
* Languages which will be used for translation:
  * translation can be enabled/disabled: ``` "translation" : { "enabled" : true/false }```
  * 'to' language can be configured with ``` "translation": { "languages": { "to" : "your_lang_here" }}```
  * 'from' language can be configured with ``` "translation" : { "languages": { "from": "your_lang_here"}}```

* Stack apps querying:
  * url which will be queried is in the node: ```url```
  * querying method can be found in the node (we found that similar produces best results in our case): ```method```
  * api version is found in the node ```version```
  * site which will be queried is in the node (we use stackoverflow site, but other sites like math exchange can be used too) ```site```
 
 * Stacks apps answer:
   * same rules as for querying
  
* Answer:
  * successful answer template is defined in node ```template```
  * answer if no response is found is defined in ```not_found``` node
