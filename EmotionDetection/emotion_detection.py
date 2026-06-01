import requests
import json
def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document":{"text":text_to_analyze}}


    response = requests.post(url, json = myobj, headers = header)
    formatted_response = json.loads(response.text)

    emotion_data = formatted_response["emotionPredictions"][0]["emotion"]
    
    anger_score = emotion_data['anger']
    disgust_score = emotion_data['disgust']
    fear_score = emotion_data['fear']
    joy_score = emotion_data['joy']
    sadness_score = emotion_data['sadness']

    emotions =['anger','disgust','fear','joy','sadness']
    scores =[anger_score,disgust_score,fear_score,joy_score,sadness_score]
    dominant_emotion = None
    max_score = float('-infinity')
    for i,score in enumerate(scores):
        if score > max_score:
            max_score = score
            dominant_emotion = emotions[i]


    result = {
        'anger' : anger_score,
        'disgust': disgust_score,
        'fear' : fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion,
    }

    return result
    



