from transformers import pipeline
import json

def emotion_detector(text_to_analyze):
    """
    Detects all emotions in the given text using Hugging Face Transformers.

    Args:
        text_to_analyze (str): The text to analyze.

    Returns:
        str: A JSON-formatted string containing emotions with scores and the dominant emotion.
    """
    emotion_model = 'bhadresh-savani/distilbert-base-uncased-emotion'
    emotion_pipeline = pipeline("text-classification", model= emotion_model, return_all_scores=True)
  
    # Get all emotion scores (extracting first list from returned list of lists)
    result = emotion_pipeline(text_to_analyze)[0]
    emotions_dict = {emotion["label"]: emotion["score"] for emotion in result}

    # Find the dominant emotion (the one with the highest score)
    dominant_emotion = max(emotions_dict, key=emotions_dict.get)
    emotions_dict["dominant_emotion"] = dominant_emotion

    # Return formatted JSON output
    return json.dumps(emotions_dict, indent=4)  # Pretty print JSON output

if __name__ == "__main__":
    #Test Case
    test_text = "I am so happy and excited!"
    test_result = emotion_detector(test_text)
    print(test_result)
