import modules
import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('vader_lexicon')
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from colorama import Fore, Style
from gensim import corpora, models
import gensim
import unicodedata2

# TODO Finish HTML Parser and provide input command
new_article = modules.Analysis('https://en.wikipedia.org/wiki/World_War_I')
lemm_article = new_article.lemmat(500)

# print(f"Article Summary: {new_article.article_summary()}\n \nArticle Text: {new_article.article_text(500)}")
# print(f"Lemmatized text: {str(new_article.lemmat(500))} \n")
sid = SentimentIntensityAnalyzer()
# print(sid_obj.polarity_scores(new_article.article_summary()))

# using the score and summary, combin them and analyze hows its negative and what way its leaning towards. specific lines that have the most negative appeal (make a code or use a in-bulit function to find the number of characters, and use that to fund in the () for the number of charcters)
# len_article = len(new_article.article_text)
articleText = (new_article.extract_text())

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
    #print(highlighted_sentence)

# Preprocess your text data
texts = ["Your text goes here", "Another text here", ...]
tokenized_texts = [articleText]

for text in texts:
    try:
        # Use the unicodedata library to normalize the text and remove non-UTF-8 characters
        normalized_text = unicodedata.normalize('NFKD', text).encode('utf-8', 'ignore').decode('utf-8')
        tokenized_text = gensim.utils.simple_preprocess(normalized_text)
        tokenized_texts.append(tokenized_text)
    except Exception as e:
        print(f"Error preprocessing text: {e}")

# Create a dictionary and a document-term matrix
dictionary = corpora.Dictionary(tokenized_texts)
corpus = [dictionary.doc2bow(text) for text in tokenized_texts]

# Train the LDA model
lda_model = models.LdaModel(corpus, num_topics=5, id2word=dictionary, passes=15)

# Get the topics
topics = lda_model.print_topics(num_words=5)
for topic in topics:
    print(topic)