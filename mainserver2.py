import multiprocessing as mp
import cv2
from webcam import UsbCam
from file_sender import FileSocket
import os
import datetime
import paho.mqtt.client as mqtt
import keyboard
import threading
from aws_class2 import Aws2


if __name__ == "__main__":

   aws = Aws2()
   aws.run()


    