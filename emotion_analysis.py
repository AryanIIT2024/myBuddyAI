from transformers import pipeline

emotion_classifier = pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion")

def get_emotion(text):
    result = emotion_classifier(text)[0]
    return result['label'], result['score']