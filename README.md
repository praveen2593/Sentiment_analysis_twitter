# Sentiment_analysis_twitter
## Perform Sentiment Analysis on Twitter Stream Data
Analyzed effect of Emoji's in improving Sentiment Analysis results. Collected twitter data using Twitter StreamAPI and used TF-IDF to vectorize the tweets. Created a positive and negative vector using the matrix, and used cosine similarity to identify the extent to which a given tweet is positive or negative. Incorporated Emoji's to the tweets by converting unicode, and repeated the process. Improved classification of the process by 15%. 

## Files in src and it's use

* settings.py - Input security credentials for the Twitter StreamAPI
* senti_analysis.py - Performs the Sentiment Analysis through cosine similarity
* scraper.py - Scraping from Twitter StreamAPI using tweepy

## Rough timeline 

* Week 1: Scraping data from Twitter Stream and storing it in MongoDB
* Week 2: Vectorized the tweets and calculated similarity, followed the CRISP - DM methodology
