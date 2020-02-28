import wget
import json
tweet_texts = []
image_list = []
success = 0
with open('tweetson.json') as json_file:
    data = json.load(json_file)
    for tweets in data['twittertest']:
        tweet_texts.append(str(tweets['Tweet']))
        #if (str(tweets['Image']) != 0):
            #test = wget.download(str(tweets['Image']))
            #image_list.append(test)
# print(image_list)
print(tweet_texts)
print(tweet_texts[1])