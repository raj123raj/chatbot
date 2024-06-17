import bs4 as bs
import urllib.request as url
import re
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import heapq
from string import punctuation
scraped_data = url.urlopen('https://en.wikipedia.org/wiki/Ilaiyaraaja')
article = scraped_data.read()
parsed_article = bs.BeautifulSoup(article,'lxml')   
paragraphs = parsed_article.find_all('p')

article_text = ""

for p in paragraphs:
    article_text += p.text
     

print(article_text)

# remove square brackets and extra spaces
article_text = re.sub(r'', ' ', article_text)
article_text = re.sub(r'\s+', ' ', article_text)
     

# remove special characters and digits
formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text )
formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)

#print(formatted_article_text)

#Tokenize Sentences
sentence_list = nltk.sent_tokenize(article_text)



stopwords = nltk.corpus.stopwords.words('english')
#print(stopwords)     

word_frequencies = {}

for word in nltk.word_tokenize(formatted_article_text):
    if word not in stopwords and word not in punctuation:
        if word not in word_frequencies.keys():
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1
     

#print(word_frequencies)

#Maximum frequencies

maximum_frequncy = max(word_frequencies.values())

for word in word_frequencies.keys():
    word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)
     

#print(word_frequencies)

#Frequency distribution
#frequency_dist = nltk.FreqDist(word_frequencies)
#frequency_dist.plot(30)

#Sentence scores


sentence_scores = {}

for sent in sentence_list:
    for word in nltk.word_tokenize(sent.lower()):
        if word in word_frequencies.keys():
            if len(sent.split(' ')) < 30:
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word]
                else:
                    sentence_scores[sent] += word_frequencies[word]
     

#print(sentence_scores)



summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)
summary = ' '.join(summary_sentences)
     

print(summary)
     

#summary
     

     

     

     

     

     
