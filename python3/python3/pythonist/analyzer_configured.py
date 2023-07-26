# Программа “Анализатор настроений”



import nltk
from nltk.sentiment import SentimentIntensityAnalyzer


def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = sia.polarity_scores(text)
    if sentiment_scores['compound'] >= 0.05:
        return "Положительный"
    elif sentiment_scores['compound'] <= -0.05:
        return "негативный"
    else:
        return "нейтральный"

def analyze_sentiment_batch(texts):
    sia = SentimentIntensityAnalyzer()
    sentiments = []
    for text in texts:
        sentiment_scores = sia.polarity_scores(text)
        if sentiment_scores['compound'] >= 0.05:
            sentiments.append("Положительный")
        elif sentiment_scores['compound'] <= -0.05:
            sentiments.append("негативный")
        else:
            sentiments.append("нейтральный")
    return sentiments

def get_sentiment_score(text):
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = sia.polarity_scores(text)
    return sentiment_scores['compound']

text = "Мне очень понравился фильм. Там был отличный сюжет и потрясающая актерская игра!"
sentiment = analyze_sentiment(text)
print("настроение:", sentiment)

texts = ["Мне нравится этот продукт!», «Обслуживание было ужасным», «Обычное впечатление."]
sentiments_batch = analyze_sentiment_batch(texts)
print("Настроения(партия):", sentiments_batch)

score = get_sentiment_score(text)
print("Оценка настроения:", score)


# В этой программе у нас есть следующие функции: analyze_sentiment_batch(texts): эта функция принимает список текстов и анализирует тональность каждого текста с помощью Анализатора интенсивности тональности. Он возвращает список настроений, соответствующих каждому входному тексту. get_sentiment_score(text): эта функция вычисляет оценку тональности (составную оценку) заданного текста с помощью Анализатора интенсивности тональности и возвращает оценку Теперь вы можете анализировать тональность отдельных текстов, обрабатывать пакет текстов или получать оценки тональности. Не стесняйтесь адаптировать и использовать эти функции в соответствии с вашими конкретными требованиями.

