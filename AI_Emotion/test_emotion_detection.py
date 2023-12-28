from EmotionDetection.emotion_detection import emotion_detector
import unittest
import json

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        label = 'dominant_emotion'
        a1 = json.loads(emotion_detector('I am glad this happened'))
        self.assertEqual(a1.get(label), 'joy')
        a2 = json.loads(emotion_detector('I am really mad about this'))
        self.assertEqual(a2.get(label), 'anger')
        a3 = json.loads(emotion_detector('I feel disgusted just hearing about this'))
        self.assertEqual(a3.get(label), 'disgust')
        a4 = json.loads(emotion_detector('I am so sad about this'))
        self.assertEqual(a4.get(label), 'sadness')
        a5 = json.loads(emotion_detector('I am really afraid that this will happen'))
        self.assertEqual(a5.get(label), 'fear')

if __name__ == '__main__':
    unittest.main()