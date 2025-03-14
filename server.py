from flask import Flask, request, render_template, jsonify
from EmotionDetection.emotion_detection import emotion_detector
import json  # Ensure we import json for processing JSON strings

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def detect_emotion():
    text_to_analyze = request.args.get('textToAnalyze', '').strip()  # Ensure input is a string, handle None case

    # If the input is blank or missing, return None but with a 200 request, the reason for 200 request is that, the mywebscript JS file does not have a way to respond if it receives anything else except 200. Therefore returning 400 returns nothing and retains the previous request results on the front end.
    if not text_to_analyze:
        sample_text = ""
        blank_emotion_result = json.loads(emotion_detector(sample_text))  # Convert JSON string to dict
        return jsonify({key: None for key in blank_emotion_result}), 200 
  

    emotion_result = emotion_detector(text_to_analyze)  # Get emotion result as JSON string
    emotion_data = json.loads(emotion_result)  # Convert JSON string to dictionary

    # If the emotion detector fails (i.e., dominant_emotion is None), return 400
    if emotion_data.get("dominant_emotion") is None:
        return jsonify({"message": "Invalid text! Please try again!"}), 200

    # If everything is fine, process and return the response
    response_str = "For the given statement, the system response is "
    response_str += ", ".join([f"'{key}': {value}" for key, value in emotion_data.items() if key != "dominant_emotion"])
    response_str += f". The dominant emotion is {emotion_data['dominant_emotion']}."
    
    return jsonify({"response": response_str}), 200

if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=5000)