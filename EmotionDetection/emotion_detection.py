
import requests
import json

def emotion_detector(text_to_analyze):
    # api url
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # request headers
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # body
    body = {"raw_document": {"text": text_to_analyze}}

    # make request
    response = requests.post(url, json=body, headers=headers)

    # grab json
    formatted_response = json.loads(response.text)

    # grab emotions score dictionary
    emotion_scores = formatted_response['emotionPredictions'][0]['emotion']
    
    # dominant emotion
    major_score = max(emotion_scores.values())
    emotion_scores['dominant_emotion'] = None
    for k, v in emotion_scores.items():
        if v == major_score:
            emotion_scores['dominant_emotion'] = k
    
    return emotion_scores

if __name__ == "__main__":
    print(emotion_detector("i love this new technology"))
