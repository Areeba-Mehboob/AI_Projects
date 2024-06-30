!pip install textblob
from textblob import TextBlob

def sentiment_analysis(text):
    # Directly calculate sentiment on the input text
    subjectivity = TextBlob(text).sentiment.subjectivity
    polarity = TextBlob(text).sentiment.polarity

    if polarity < 0:
        analysis = 'Negative'
    elif polarity == 0:
        analysis = 'Neutral'
    else:
        analysis = 'Positive'

    print('Subjectivity:', subjectivity, end="")
    print(', Polarity:', polarity, end="")
    print(', Analysis:', analysis)

sentiment_analysis("The movie was so awesome.")

sentiment_analysis("The food here tastes terrible.")

sentiment_analysis("The book was a perfect balance between wrtiting style and plot.")

sentiment_analysis("The pizza tastes terrible.")

sentiment_analysis("Python is a high-level, general-purpose programming language.")
