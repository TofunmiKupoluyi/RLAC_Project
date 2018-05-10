from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

# Instantiates a client
client = language.LanguageServiceClient()
def analyze(text):
    # The text to analyze
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(document=document)
    entitySentiment = client.analyze_entities(document).entities
    # print('Text: {}'.format(text))
    # print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))
    print(sentiment)

    return(sentiment, entitySentiment)


