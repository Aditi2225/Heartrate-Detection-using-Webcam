import cv2
import numpy as np
import time

class Video(object):
    def __init__(self):
        self.dirname = ""
        self.cap = None
        t0 = 0
        
    def start(self):
        print("Start video")
        if self.dirname == "":
            print("invalid filename!")
            return
            
        self.cap = cv2.VideoCapture(self.dirname)
        fps = self.cap.get(cv2.CAP_PROP_FPS)
        self.frame_count = self.cap.get(cv2.CAP_PROP_FRAME_COUNT)
        print(fps)
        self.t0 = time.time()
        print(self.t0)
        self.valid = False
        try:
            resp = self.cap.read()
            self.shape = resp[1].shape
            self.valid = True
        except:
            self.shape = None
    
