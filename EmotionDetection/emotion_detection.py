""" URL: 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers: {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    Input json: { "raw_document": { "text": text_to_analyse } }"""
HEADER = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
import requests, json
def emotion_detector(text_to_analyze):
    in_Json = {"raw_document":{"text": text_to_analyze}}
    response = requests.post(URL,headers=HEADER,json=in_Json)
    if (response.status_code != 200):
        print("request unsucessful", response.status_code)
        return response.status_code
    out_Json = response.text
    out_Json = json.loads(out_Json)
    emotion = out_Json["emotionPredictions"][0]["emotion"]
    max = 0
    max_emotion = ""
    for key in emotion:
        if (emotion[key] > max):
            max = emotion[key]
            max_emotion = key
    emotion["dominant_emotion"] = max_emotion
    return emotion
emotion_detector("I am so happy I am doing this")