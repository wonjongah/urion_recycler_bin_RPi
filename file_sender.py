import os
import socket

HOST = "192.168.0.103"
PORT = 6666
FILE_PATH = "/home/pi/workspace/opencv-ex/data/test_pic3.jpg"

class FileSocket:
    def __init__(self, host, port):
        self.host = HOST
        self.port = PORT
        self.filepath = FILE_PATH
        self.filename = "test.jpg"
    
    def file_read(self, file_path):
        with open(file_path, "rb") as f:
            while True:
                data = f.read(1024)
                if not data:
                    break
                yield data
    
    def file_send():
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.connet((HOST, PORT))
                file_size = os.path.getsize(FILE_PATH)

                # 파일 크기 전송
                print("전송 파일 크기 : ", file_size)
                s.sendall(str(file_size).encode())

                # 준비 상태 수신
                isready = s.recv(1024).decode()
                if isready == "ready":
                    # 파일 전송
                    for data in file_read(FILE_PATH):
                        s.sendall(data)
                    print("전송 완료")
            
            except Exception as e:
                print(e)