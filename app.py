from flask import Flask, render_template, request 
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
nltk.download('vader_lexicon')
nltk.download('punkt')

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/result', methods = ['POST', 'GET']) 
def result(): 
   if request.method == 'POST': 
      result = request.form.to_dict() 
      global link
      link = result.get('Link')

      new_article = modules.Analysis(f'{link}')
      articleText = (new_article.extract_text())
      sentences = nltk.sent_tokenize(articleText)
      threshold = 0.6
      sid = SentimentIntensityAnalyzer()
      n_res = []
      p_res = []

      for sentence in sentences:
        sentiment_scores = sid.polarity_scores(sentence)
        compound_score = sentiment_scores['compound']
        # do you want to highlight the postively skewed ones as well? We can make a threshold for that.
        if abs(compound_score) >= threshold:
            if compound_score > 0:
                highlighted_sentence = Fore.GREEN + sentence + Style.RESET_ALL
                p_res.append(highlighted_sentence)
            else:
                highlighted_sentence = Fore.RED + sentence + Style.RESET_ALL
                n_res.append(highlighted_sentence)
        else:
            highlighted_sentence = sentence
        
      scores = sid.polarity_scores(new_article.article_summary())
      
      def summarize_neutral_text(input_text):
          # Tokenize the input text into sentences
          sentences = nltk.sent_tokenize(input_text)

          # Initialize the VADER SentimentIntensityAnalyzer
          sid = SentimentIntensityAnalyzer()

          neutral_sentences = []

          # Identify and collect neutral sentences
          for sentence in sentences:
            sentiment_scores = sid.polarity_scores(sentence)
            compound_score = sentiment_scores['compound']
            if -0.1 <= compound_score <= 0.1:
                neutral_sentences.append(sentence)

          # Generate the summary from neutral sentences
          summary = ' '.join(neutral_sentences)
          return summary

      neutral_summary = new_article.article_summary()
      output = [link, neutral_summary, articleText, threshold, SentimentIntensityAnalyzer(), sentences,  p_res, n_res, scores]
      return render_template("result.html", result = output)

# # print(f"Article Summary: {new_article.article_summary()}\n \nArticle Text: {new_article.article_text(500)}")
# # print(f"Lemmatized text: {str(new_article.lemmat(500))} \n")
# sid = SentimentIntensityAnalyzer()
# #print(sid.polarity_scores(new_article.article_summary()))

# # using the score and summary, combin them and analyze hows its negative and what way its leaning towards. specific lines that have the most negative appeal (make a code or use a in-bulit function to find the number of characters, and use that to fund in the () for the number of charcters)
# # len_article = len(new_article.article_text)
# articleText = (new_article.extract_text())

# sentences = nltk.sent_tokenize(articleText)
# threshold = 0.6

# for sentence in sentences:
#     sentiment_scores = sid.polarity_scores(sentence)
#     compound_score = sentiment_scores['compound']
#     # do you want to highlight the postively skewed ones as well? We can make a threshold for that.
#     if abs(compound_score) >= threshold:
#         if compound_score > 0:
#             highlighted_sentence = Fore.GREEN + sentence + Style.RESET_ALL
#         else:
#             highlighted_sentence = Fore.RED + sentence + Style.RESET_ALL
#     else:
#         highlighted_sentence = sentence
#     #print(highlighted_sentence)

# print("Summary of Neutral Text:")
# print(neutral_summary)