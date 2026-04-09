from transformers import pipeline
import torch

sentiment_analyzer = pipeline("sentiment-analysis")

texts = [
    'I absolutely love this product! Its amazing.',
    'The service was terrible and I want my money back.',
    'Its okay, nothing special.'
]

for text in texts:
    result = sentiment_analyzer(text)[0]

    print(f'Text: {text}')
    print(f'Sentiment: {result['label']}, Confidence: {result['score']}\n')