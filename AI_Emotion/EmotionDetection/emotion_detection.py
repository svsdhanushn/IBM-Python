import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=myobj, headers=header)

    formatted_response = json.loads(response.text)

    score = formatted_response["emotionPredictions"][0]["emotion"]
    anger = score["anger"]
    disgust = score["disgust"]
    fear = score["fear"]
    joy = score["joy"]
    sadness = score["sadness"]
    dominant_emotion = max(score, key=score.get)

    result = {'anger': anger, 'disgust': disgust, 'fear': fear, 'joy': joy,
              'sadness': sadness, 'dominant_emotion': dominant_emotion }

    return(json.dumps(result, indent=0))

# from emotion_detection import emotion_detector
# emotion_detector('I love this new technology')