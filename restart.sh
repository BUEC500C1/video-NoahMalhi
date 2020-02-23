#!/bin/bash
rm -r *.png
rm -r *.avi

python3 main.py -y &
ps -ef | grep python

