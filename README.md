# Video Encoder FFMPEG
## Noah Malhi

For this hw, I utilized the twitter api. The format of the video is the image and then the tweet in which the image came from.

My assignment is able to run about 6 processes. At that point the terminal I am running is buggy after the run. To view the running processes, in my bash script:
    restart.sh
I used the command line cmd: ps -ef | grep python
This finds all the running processes produces from python. 

For threading, I threaded the FFMPEG command to generate the video as well as the processes of converted text to images. From using the linux 'time' command' I was able to lower run time by about .2 in most cases for total run time.

For multiprocessing I used "Processes" imported from multiprocessors. I was at most able to execute 6 processes cleanly. I made a lists of processes and had a four loop to call the main 6 times. The made processes were added to the list and after all the processes were made thier was a proccess join to wait for all the proccesses to complete before the program ended.

The separate videos were saved as video(process number).avi. Each process number was attained by using getpid().

The following are some images from the video:
