# Sentiment Analysis For a Given Text 
This repo is for a reflection on my attempt to learn and implement my gained knowledge in the area of Flask Web Application framework, Python programming (Unit Testing, Packaging Modules, Error handling & PEP8 guidelines) and RESTful Api. 

This is a practice project where in I have demonstrated my programming skills in developing an AI based Application using Python and Flask. I have integrated the Web app with Watson-NLP AI library <b>(BERT based Sentiment Analysis Function of the Watson NLP Library)</b> which is used to perfome <b>"Sentiment Analysis"</b> for a given text. In other words, this AI application will detect the sentiment with which a given text was written.

## A sample code for such an application could be
```python
import requests
def <function_name>(<input_args>):
    url = '<relevant_url>'
    headers = {<header_dictionary>}
    myobj = {<input_dictionary_to_the_function>}
    response = requests.post(url, json = myobj, headers=header)
    return response.text
``` 

Since I made use of the IBM Watson AI Library services, to access this function, the UTL, headers and input json format is as follows
```python 
URL: 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
Headers: {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
Input json: { "raw_document": { "text": text_to_analyse } }
````

A sample application response for a given etxt input <i>"I love this new technology"</i> is something like this 
```json
{"documentSentiment":{"score":0.995756, "label":"SENT_POSITIVE", "mixed":false, "sentimentMentions":[{"span":{"begin":0, "end":22, "text":"I love this technology"}, "sentimentprob":{"positive":0.99183923, "neutral":0.0041469256, "negative":0.004013916}}]}, "targetedSentiments":{"targetedSentiments":{}, "producerId":{"name":"Aggregated Sentiment Workflow", "version":"0.0.1"}}, "producerId":{"name":"Aggregated Sentiment Workflow", "version":"0.0.1"}}
````
Information relevant to us is only the <b><i>label</i></b> and the <b><i>score</i></b>.

## Summary
With this project, I have successfully

* Created an AI based sentiment analysis application using Watson NLP embedded libraries.

* Formatted the output received from the Watson NLP library function to extract relevant information from it.

* Packaged the application and made it importable to any python code for usage.

* Ran unit tests on the application and checked the validity of its outputs for different inputs.

* Deployed the application using Flask framework.

* Incorporated error handling capability in the application, such that a response code of 500 receives an appropriate response from the application.

* Ran static code analysis on the code files to confirm their adherence to the PEP8 guidelines.


© IBM Corporation 2023. All rights reserved.