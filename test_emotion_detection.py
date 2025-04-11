
from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        cases = [
            {'statement': 'I am glad this happened', 'dominant_emotion': 'joy'},
            {'statement': 'I am really mad about this', 'dominant_emotion': 'anger'},
            {'statement': 'I feel disgusted just hearing about this', 'dominant_emotion': 'disgust'},
            {'statement': 'I am so sad about this', 'dominant_emotion': 'sadness'},
            {'statement': 'I am really afraid that this will happen', 'dominant_emotion': 'fear'},
        ]
        for case in cases:
            result = emotion_detector(case['statement'])
            self.assertEqual(result['dominant_emotion'], case['dominant_emotion'])

unittest.main()
