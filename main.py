import twitter_fetch
import video_stream
import dev_image

def main():
    image_list = []

    (image_list, tweet_texts, success) = twitter_fetch.vision_feed(image_list)
    if(success == 0):
        print('Error retrieving tweets')
        return 1

    dev_image.convert_text(tweet_texts)
    
main()