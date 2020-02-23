import twitter_fetch
import video_stream
import dev_image
import threading
from multiprocessing import Process
import os


def dev_video():

    pid = os.getpid()
    os.system('ffmpeg -framerate 0.5 -i img0%d.png video'+str(pid)+'.avi')

def main():
    image_list = []
    (image_list, tweet_texts, success) = twitter_fetch.vision_feed(image_list)
    
    print(image_list)

    if(success == 0):
        print('Error retrieving tweets')
        return 1

    dev_image.convert_text(tweet_texts, image_list)
    
    x = threading.Thread(target=dev_video)
    x.start()

if __name__ == '__main__':
    processes = []

    for m in range (1,7):
        p = Process(target=main)
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    