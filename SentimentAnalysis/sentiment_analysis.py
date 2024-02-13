"""
Author: Vishal Ashok Hegde
Function to perform Sentiment Analysis using Watson-nlp library
"""
import requests
import json 

def sentiment_analyzer(text_to_analyse: str):
    """
    Function to analyse the text input and predict the sentiment of the text
    Sentiment Categorized into :
    :1. Positive
    :2. Negetive
    :3. Neutral
    """

    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    headers = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    myobj =  {"raw_document": { "text": text_to_analyse }}
    response = requests.post(url, json=myobj, headers=headers)
    formatted_response = json.loads(response.text)
    
    if response.status_code == 200:
        """Status Code condition for 200"""
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    
    elif response.status_code == 500:
        """Error Code condition for 500"""
        label = None
        score = None
    
    return {"Label": label, "Score": score}
    