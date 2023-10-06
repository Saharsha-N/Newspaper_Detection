import modules
import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
# from textblob import TextBlob
# from textblob.sentiments import NaiveBayesAnalyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# TODO Finish HTML Parser and provide input command
new_article = modules.Analysis('https://en.wikipedia.org/wiki/World_War_I')
lemm_article = new_article.lemmat(500)

print(f"Article Summary: {new_article.article_summary()}\n \nArticle Text: {new_article.article_text(500)}")
# print(f"Lemmatized text: {str(new_article.lemmat(500))} \n")


sid_obj = SentimentIntensityAnalyzer()
print(sid_obj.polarity_scores(new_article.article_summary()))