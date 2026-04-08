def sentiment(text):
    positive = ['good','happy','great','love']
    negative = ['bad','sad','angry','hate']

    if any(word in text.lower() for word in positive):
        return "Positive"
    elif any(word in text.lower() for word in negative):
        return "Negative"
    else:
        return "Neutral"
    
print(sentiment("I Love AI"))
print(sentiment("I hate this product"))