from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
import unittest

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        result_1 = sentiment_analyzer("I love working with Python")
        result_2 = sentiment_analyzer("I hate working with Pyhton")
        result_3 = sentiment_analyzer("I am neutral on Python")
        self.assertEqual(result_1['Label'], "SENT_POSITIVE")
        self.assertEqual(result_2['Label'], "SENT_NEGATIVE")
        self.assertEqual(result_3['Label'], "SENT_NEUTRAL")
        
if __name__ == "__main__":
    unittest.main()