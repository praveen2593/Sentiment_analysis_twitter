'''
I am interested in performing a sentiment analysis on twitter stream data. I used an event recently, which covers a historic transfer of a soccer player for the highest amount of money (grossing over $450 million) and I am interested in understanding the public reaction on the same.
Also, continuing with the data set, I am interested in identifying the power of emoji's in a tweet. I want to incorporate the emoji's while computing the sentiment orientation of a tweet. And in order to do this, I converted all unicode tweet into their names using unicodedata library.

I have two questions:
1. For the first part of the problem, I created a tfidf Vectorizer, and converted the tweet data. For some reason, when I try to run the code, it takes a lot of time and my kernel restarts. I am not able to identify why.

2. For the second part of my problem, I built a separate tokenizer. I am not sure how to convert the list to a sparse matrix. And beyond that problem, I am not able to understand how I can convert my positive and negative words list as vectors with same number of features as the sparse matrix. Or is there some other way in which I can perform this operation?
'''


import pandas as pd
import numpy as np
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
import string
import unicodedata as uni
from sklearn.metrics.pairwise import cosine_similarity
import unicodedata as uni
import matplotlib.pyplot as plt
# %matplotlib inline
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

def cleaning_tweets(tweet):
    ''' Cleaning Tweets by tokenizing, converting to lowercase, removing stop words and converting EMOJI's to their string names
    input: tweet: a single Tweet
    Output: words: Words in the tweet
            emoji_count: Number of Emoji's in the tweet
    '''
    words = [x for x in TweetTokenizer(strip_handles= True, preserve_case=False, reduce_len=True).tokenize(tweet) if x not in stopwords.words('english')]
    words = [x for x in words if x not in string.punctuation]
    emoji_count = 0
    for idx, word in enumerate(words):
        try:
            words[idx] = uni.name(word).lower()
            emoji_count += 1
        except:
            pass
    return words, emoji_count

def tweet_prep(tweets):
    '''
    Gets all tweets and cleans the tweets using cleaning_tweets. Returns a list of list of words in a tweet and a list of the number of emoji's in that tweet.
    Input: tweets: All tweets
    Output: tweets_list: list of list of words in each tweet
            emo_count: list of count of emoji's in each tweet
    '''
    tweets_list = []
    emo_count = []
    for tweet in tweets:
        words, count = cleaning_tweets(tweet)
        tweets_list.append(words)
        emo_count.append(count)
    return tweets_list, emo_count

def senti_data(filename_pos, filename_neg):
    '''
    Converts a list of positive and negative words into a lists.
    Output: pos: List of all positive words
            neg: List of all negative words
    '''
    positive_vocab = ''
    negative_vocab = ''

    with open('filename_pos', 'r') as f:
        for line in f:
            positive_vocab += line.strip() + ' '

    with open('filename_neg', 'r') as f:
        for line in f:
            negative_vocab += line.strip() + ' '
    pos = []
    neg = []
    pos.append(positive_vocab)
    neg.append(negative_vocab)
    return pos, neg

if __name__ == '__main__':
    # Reading Tweets from the Scraped data
    df = pd.read_json('tweets.json', lines=True)

    #Removing rows of tweets which does not have any text
    df.dropna(axis=0, subset = ['text'], inplace=True)

    #Calling tweet_prep to convert tweets to word counts
    tweet_list, emo_count = tweet_prep(df.text)
    # cv = CountVectorizer()

    #Creating Vectorizer and transforming data
    cv = TfidfVectorizer(ngram_range=(1,3), stop_words='english', strip_accents='unicode')
    tf = cv.fit_transform(df.text)

    #Getting positive and negative words list
    pos, neg = senti_data('data/pos','data/neg')

    #Converting the words list to vectors
    pos_vec = cv.transform(pos)
    neg_vec = cv.transform(neg)

    #Calculating similarity between each tweet and the positive vector
    pos_score = np.asanyarray(cosine_similarity(tf.toarray(),pos_vec))
    neg_score = np.asanyarray(cosine_similarity(tf.toarray(),neg_vec))

    #Calculating net score, assuming that each tweet would have a positive and negative score associated with it. And the net difference would give me the net orientation of the tweet.
    score = pos_score - neg_score

    #Getting the top 20 tweets with a positive sentiment
    np.argsort(score.ravel())[-20:][::-1]
