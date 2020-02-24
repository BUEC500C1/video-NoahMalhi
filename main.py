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

    if(success == 0):
        print('Error retrieving tweets')
        return 1

    dev_image.convert_text(tweet_texts, image_list)
    
#threads the main() function that pull images and develops pictures from tweets
#uses 4 threads --> utilizes lists rather than queues , it was faster for some reason
threads = []
for n in range (1,4):
    x = threading.Thread(target=main)
    x.start()
    threads.append(x)

for x in threads:
    x.join()

#makes multiple videos at once using multiprocessing
#using Intel i7 with 8 cores and can make 7 videos at once (7 processes)
processes = []

for m in range (1,6):
    p = Process(target=dev_video)
    p.start()
    processes.append(p)

for p in processes:
    p.join()

    