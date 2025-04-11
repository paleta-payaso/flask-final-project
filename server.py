
'''
Initialize flask app.
'''

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detector')

@app.route("/emotionDetector")
def serve_detector():
    '''
    This route gets called by the javascript code to use the emotion detector 'api'.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    return f"""
        For the given statement, the system response is
        \'anger\': {response['anger']},
        \'disgust\': {response['disgust']}, 
        \'fear\': {response['fear']},
        \'joy\': {response['joy']},
        \'sadness\': {response['sadness']}.
        The dominant emotion is {response['dominant_emotion']}.
    """

@app.route("/")
def render_index():
    '''
    This route renders the main app.
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
