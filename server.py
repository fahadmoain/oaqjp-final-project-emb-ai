from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector
import json  # Ensure we import json for processing JSON strings

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def detect_emotion():
    text_to_analyze = request.args.get('textToAnalyze')
    if not text_to_analyze:
        return "Error: No text provided for analysis."
    
    emotion_result = emotion_detector(text_to_analyze)  # Get emotion result as JSON string
    emotion_data = json.loads(emotion_result)  # Convert JSON string to dictionary
    dominant_emotion = emotion_data.pop("dominant_emotion")  # Extract dominant emotion
    
    # Format response string
    response_str = "For the given statement, the system response is "
    response_str += ", ".join([f"'{key}': {value}" for key, value in emotion_data.items()])
    response_str += f". The dominant emotion is {dominant_emotion}."
    
    return response_str

if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=5000)