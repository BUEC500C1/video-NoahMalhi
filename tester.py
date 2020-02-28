import json
import wget

tweet_texts = []
image_list = []

with open('tweetson.json') as json_file:
	data = json.load(json_file)
	for tweets in data['twittertest']:
	    tweet_texts.append(str(tweets['Tweet']))
        if (str(tweets['Image']) != 0):
            test = wget.download(str(tweet['Image']))
            image_list.append(test)
print(image_list)
print(tweet_texts)       