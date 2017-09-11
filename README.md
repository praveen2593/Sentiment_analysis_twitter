# Sentiment_analysis_twitter

## Overview
Analyzed effect of Emoji's in improving Sentiment Analysis results. Collected twitter data using Twitter StreamAPI and used TF-IDF to vectorize the tweets. Created a positive and negative vector using the matrix, and used cosine similarity to identify the extent to which a given tweet is positive or negative. Incorporated Emoji's to the tweets by converting unicode, and repeated the process. Improved classification of the process by 15%. 

## Motivation
Understanding human emotion and rationale has always been a fascination of mine. With my data science skillset, I wanted to understand how people express their emotion on social networks, aka Sentiment Analysis. Being an avid twitter user, I knew how restricting to less than 140 characters forced people to innovate, and how emoji's became one of the important methods to deliver meaning in tweets. I wanted to understand how people relied on Emoji's to convey their emotion, hence designed this simple experiment to capture that feeling. 

## Data Collection
Twitter's Stream API lets you collect data in real-time. Using [tweepy](https://github.com/tweepy/tweepy), I created a Stream Listener object which allowed me to collect real time data. For this experiment, I wanted to understand how football fans percieved the biggest football transfer till date, [sale of Neymar Jr from Barcelona to Paris St. Germain for $263 million](https://www.cnbc.com/amp/2017/08/17/what-neymars-263-million-transfer-fee-means-for-the-future-of-soccer.html). 
I eventually ended up with around 50,000 tweets collecting for a four hour time period.

## Feature Engineering
Similar to NLP, I stripped whitespaces and converted to lowercase. Since tweets have other unnecessary information like the twitter handles, links, I removed those information. For the first part of the project, I removed all emoji's and stored them separately. 

For the second part of the problem, I used the unicode library to convert all unicode emoji's to their names, using a unicode to name table.

## Model Development
Using the above data, I used Count Vectorizer to create a matrix with the vocabulary as features and the different tweets as rows. To associate each tweet with a sentiment, I compiled a list of positive words and list of negative words, and using the matrix, created a positive and negative vector. I then calculated the amount of positivity and negativity associated with each tweet by calculating the cosine similarity between the vector and the tweet. The difference between the positive and the negative score would show the overall score of the tweet. 
Repeated the process again while including the emoji's in the dataset.

## Result, Inference and Future Work
The model showed a 5% increase in the number of positive tweets when Emoji's were added. Since the event was an international event, I could not perform the analysis on tweets which were not in english. That and given that a significant portion of the tweet consisted of hyperlinks to news articles, I felt my model did not perform as well as expected. In the future, I want to choose a more general topic and perform the same experiment, to see how generalized the experiement results are. 

## Files in src and it's use

* settings.py - Input security credentials for the Twitter StreamAPI
* senti_analysis.py - Performs the Sentiment Analysis through cosine similarity
* scraper.py - Scraping from Twitter StreamAPI using tweepy

## Rough timeline 

* Week 1: Scraping data from Twitter Stream and storing it in MongoDB
* Week 2: Vectorized the tweets and calculated similarity, followed the CRISP - DM methodology
