#!/usr/bin/env python3
import random
import os

playlist = ["http://air.synthez.net:8888/192", "http://195.91.220.35:8005/live192", "http://online.radiorecord.ru:8102/ps_128", "http://online.radiorecord.ru:8101/rr_128", "http://sanfm.ru:8000/trance"]

random_playlist = (random.choice(playlist))
print(random_playlist)
