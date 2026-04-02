import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json = myobj, headers=headers)
    formatted_response = json.loads(response.text)
    emotion_predictions = formatted_response['emotionPredictions'][0]
    emotion_predictions_emotions = emotion_predictions['emotion']

    anger_score = emotion_predictions_emotions['anger']
    disgust_score = emotion_predictions_emotions['disgust']
    fear_score = emotion_predictions_emotions['fear']
    joy_score = emotion_predictions_emotions['joy']
    sadness_score = emotion_predictions_emotions['sadness']

    dominant_emotion = max(emotion_predictions_emotions, key=emotion_predictions_emotions.get)
    
    return {'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion}