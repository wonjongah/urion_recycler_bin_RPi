import cv2
import numpy as np

class UsbCam:
    def __init__(self, show=False, framerate=25, width=640, height=480):
        self.size = (width, height)
        self.show = show
        self.framerate = framerate

    def run(self):
        k = 0
        self.cap = cv2.VideoCapture(0) # 1번 카메라

        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.size[0])
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.size[1])

        roi_width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        roi_height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


        # print('frame_size = ', self.frame_size)

        retval, frame = self.cap.read() # 프레임 캡처, retval(성공여부), frame(실제값)
        if not retval: cv2.destroyAllWindows()  # 실패
        cv2.imshow('frame', frame)  # 실패 아니면 화면 출력
        
        # roi = frame[0:roi_height, 0:roi_width]
        frame2 = np.full(frame.shape, (65, 80, 100), dtype=np.uint8)
        frame3 = cv2.add(frame,frame2)

        cv2.imwrite("image_data/통합본2/vita/pic.jpg", frame3)


        
        if self.cap.isOpened(): # 열려있으면
            self.cap.release() # 카메라 닫아주기

        cv2.destroyAllWindows() # 윈도우 닫아주기
  
