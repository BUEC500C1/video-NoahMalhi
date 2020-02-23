import twitter_fetch
import video_stream
import dev_image
import os

def main():
    image_list = []
    (image_list, tweet_texts, success) = twitter_fetch.vision_feed(image_list)
    
    print(image_list)

    if(success == 0):
        print('Error retrieving tweets')
        return 1

    dev_image.convert_text(tweet_texts, image_list)
    
    os.system('ffmpeg -framerate 0.5 -i img0%d.png video.avi')

main()