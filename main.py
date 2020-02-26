import twitter_fetch
import video_stream
import dev_image
import threading
from multiprocessing import Process
import os
import sys


def dev_video(username):
    #each process runs ffmpeg using its own username.png files
    pid = os.getpid()
    os.system('ffmpeg -framerate 0.5 -i '+username+'%d.png video'+str(pid)+'.avi')

def main(username):
    image_list = []
    (image_list, tweet_texts, success) = twitter_fetch.vision_feed(image_list, username)

    if(success == 0):
        print('Error retrieving tweets')
        return 1

    dev_image.convert_text(tweet_texts, image_list, username)

    #Uses 3 threads to run FFMPEG
    dev_video(username)
    # threads = []
    # for n in range (1,4):
    #     x = threading.Thread(target=dev_video, args=(username,))
    #     x.start()
    #     threads.append(x)

    # for x in threads:
    #     x.join()
    


#makes multiple videos at once using multiprocessing
#using Intel i7 with 8 cores and can make 7 videos at once (7 processes)
# processes = []
#args=(tweet_texts, imagelist))

processes = []
if (len(sys.argv) < 8):
    for m in range (1,len(sys.argv)):
        username = sys.argv[m]   
        p = Process(target=main, args=(username,))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
else:
    print("Can not run with more than 7 usernames/processes")

    