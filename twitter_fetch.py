import tweepy
import keys
import io
import os
import json
import wget

from google.cloud import vision
from google.cloud.vision import types

def vision_feed(image_list):

    data = {}
    data['tweets'] = []
    tweet_texts = []
    success = 0
    try:
        auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
        auth.set_access_token(keys.access_token, keys.access_token_secret)
        api = tweepy.API(auth)
        public_tweets = api.home_timeline()
        
        for tweet in public_tweets:
            tweet_texts.append(tweet.text)
            media_files = set()
            media = tweet.entities.get('media', [])
            if(len(media) > 0):
                media_files.add(media[0]['media_url'])           
            
            for media_file in media_files:
                test = wget.download(media_file)
                image_list.append(test)
                
        success = 1
        return (image_list, tweet_texts, success)

    except ValueError:
        success = ValueError
        return ([], success)

