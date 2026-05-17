import requests
import json

def emotion_detector(text_to_analyze):
    
    # URL for Watson NLP Emotion Predict function
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Headers required by Watson NLP
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    
    # Input JSON format
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    # Send POST request to Watson NLP
    response = requests.post(url, headers=headers, json=input_json)
    
    # Step 1 — Convert response text to dictionary
    response_dict = json.loads(response.text)
    
    # Step 2 — Extract emotions from dictionary
    emotions = response_dict['emotionPredictions'][0]['emotion']
    
    anger_score   = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score    = emotions['fear']
    joy_score     = emotions['joy']
    sadness_score = emotions['sadness']
    
    # Step 3 — Find dominant emotion (highest score)
    emotion_scores = {
        'anger':   anger_score,
        'disgust': disgust_score,
        'fear':    fear_score,
        'joy':     joy_score,
        'sadness': sadness_score
    }
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    
    # Step 4 — Return formatted output
    return {
        'anger':            anger_score,
        'disgust':          disgust_score,
        'fear':             fear_score,
        'joy':              joy_score,
        'sadness':          sadness_score,
        'dominant_emotion': dominant_emotion
    }