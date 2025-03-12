import unittest
import json  # Import the json module
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):

    def test_joy(self):
        result_str = emotion_detector("I am glad this happened")
        result = json.loads(result_str)  # Parse the JSON string
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_anger(self):
        result_str = emotion_detector("I am really mad about this")
        result = json.loads(result_str)  # Parse the JSON string
        self.assertEqual(result['dominant_emotion'], 'anger')

    #def test_disgust(self):
        #result_str = emotion_detector("I am disgusted.")
        #result = json.loads(result_str)  # Parse the JSON string
        #self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_sadness(self):
        result_str = emotion_detector("I am so sad about this")
        result = json.loads(result_str)  # Parse the JSON string
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_fear(self):
        result_str = emotion_detector("I am really afraid that this will happen")
        result = json.loads(result_str)  # Parse the JSON string
        self.assertEqual(result['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()