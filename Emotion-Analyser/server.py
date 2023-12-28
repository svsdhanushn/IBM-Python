import json
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detector", template_folder='templates')


@app.route("/emotionDetector")
def sent_detector():
    text_to_analyze = request.args.get('textToAnalyze')

    response = json.loads(emotion_detector(text_to_analyze))

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if anger is None:
        return "Invalid text! Please try again!"
    else:
        return ("""
        For the given statement, the system response is 'anger': {}, 'disgust': {}, 'fear': {}, 
        'joy': {} and 'sadness': {}. The dominant emotion is {}.
        """).format(anger, disgust, fear, joy, sadness, dominant_emotion)


@app.route("/")
def render_index_page():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
