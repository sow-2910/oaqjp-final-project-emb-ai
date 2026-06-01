from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask("emotion_detector")

@app.route("/emotionDetector")
def sent_analyzer():
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    dominant_emotion = response['dominant_emotion']

    return f"For the given statement, the system response is {response}. The dominant emotion is {dominant_emotion}"

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 5000)
