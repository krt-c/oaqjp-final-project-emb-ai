"""
This module provides a Flask server for the emotion detection application.
It handles routes for processing text and returning emotion scores.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def post_emotion_detector():
    """
    This functions accepts the text to analyze 
    Returns the level of emotion for the given text
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']

    return (
        f"For the given statement, the system response is 'anger': {anger_score}, "
        f"'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score} "
        f"and 'sadness': {sadness_score}. The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    Index route function
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
