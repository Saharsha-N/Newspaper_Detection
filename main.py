import modules
import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from colorama import Fore, Style

# TODO Finish HTML Parser and provide input command
new_article = modules.Analysis('https://en.wikipedia.org/wiki/World_War_I')
lemm_article = new_article.lemmat(500)

# print(f"Article Summary: {new_article.article_summary()}\n \nArticle Text: {new_article.article_text(500)}")
# print(f"Lemmatized text: {str(new_article.lemmat(500))} \n")

sid_obj = SentimentIntensityAnalyzer()
# print(sid_obj.polarity_scores(new_article.article_summary()))

# using the score and summary, combin them and analyze hows its negative and what way its leaning towards. specific lines that have the most negative appeal (make a code or use a in-bulit function to find the number of characters, and use that to fund in the () for the number of charcters)
# len_article = len(new_article.article_text)
articleText = (new_article.article_text(999999999999999**999))

nltk.download('vader_lexicon')
sid = SentimentIntensityAnalyzer()

sentences = nltk.sent_tokenize(articleText)
threshold = 0.6

for sentence in sentences:
    sentiment_scores = sid.polarity_scores(sentence)
    compound_score = sentiment_scores['compound']
    # do you want to highlight the postively skewed ones as well? We can make a threshold for that.
    if abs(compound_score) >= threshold:
        if compound_score > 0:
            highlighted_sentence = Fore.GREEN + sentence + Style.RESET_ALL
        else:
            highlighted_sentence = Fore.RED + sentence + Style.RESET_ALL
    else:
        highlighted_sentence = sentence
    print(highlighted_sentence)