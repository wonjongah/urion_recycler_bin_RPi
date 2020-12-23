import multiprocessing as mp
import cv2
from webcam import UsbCam
from file_sender import FileSocket
import os
import datetime
import paho.mqtt.client as mqtt
import keyboard
import threading
from aws_class import Aws

if __name__ == "__main__":

   aws = Aws()
   aws.run()


    