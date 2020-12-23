from awscrt import io, mqtt, auth, http
from awsiot import mqtt_connection_builder
import time as t
import json
import sys
import threading
from uuid import uuid4
import threading
import os
import multiprocessing as mp
import cv2
from webcam import UsbCam
import datetime
import paho.mqtt.client as Mqtt
from prediction_code2 import Ai 
import pyzbar.pyzbar as pyzbar
from qr_class import qr

result = 0
bottle_kind = 0
time_real = ""
today_real = ""
order = 0
user_id = ""
full1 = 0
full2 = 0
full3 = 0
class Aws2():
        def __init__(self):
            self.ENDPOINT = "YOUR_ENDPOINT"
            self.CLIENT_ID = "wontest2"
            self.PATH_TO_CERT = "certificate.pem.crt"
            self.PATH_TO_KEY = "private.pem.key"
            self.PATH_TO_ROOT = "root.pem"
            self.FULLMESSAGE1 = "1"
            self.FULLMESSAGE2 = "2"
            self.FULLMESSAGE3 = "3"
            self.FULLTOPIC = "full"
            self.RFIDTOPIC = "user/rfid"
            self.SUB_TOPIC = "user/end"
            self.RANGE = 20
            self.COUNT = 0

        def id(self, id):
            global user_id
            user_id = id
            print("received rfid", user_id)

        def run(self):
                def voice_end():
                        os.system("aplay voice/end.wav")
                
                def voice_start():
                        os.system("aplay voice/시작.wav")

                def voice_1():
                        os.system("aplay voice/재사용1.wav")
                        os.system("aplay voice/1넣.wav")

                def voice_2():
                        os.system("aplay voice/재활용2.wav")
                        os.system("aplay voice/2넣.wav")

                def voice_3():
                        os.system("aplay voice/쓰레기3.wav")
                        os.system("aplay voice/3넣.wav")

                def voice_qr():
                        os.system("aplay voice/qr.wav")

                def save_qr():
                        qr_data = qr()
                        
                
                def on_connect(client, userdata, flags, rc):
                        print("Connected with result code "+ str(rc))
                        if rc == 0:
                            client.subscribe("esp8266/+") # 연결 성공시 토픽 구독 신청
                            print("subscribed")
                        else:
                            print('연결 실패 : ', rc)

                def on_message(client, userdata, msg):
                        global full1, full2, full3

                        # rifd 체크하고 병을 놓았을 때
                        if(msg.topic == "esp8266/loadcell"):
                            
                            print("received roadcell value")
                            global order 
                            order += 1
                            # 사진 찍고, ai 돌림
                        #     cam = UsbCam()
                        #     cam.run()
                            os.system("fswebcam -r 1280x720 --no-banner --set brightness=60% image_data/통합본2/vita/pic.jpg")

                            # 결과값을 1, 2, 3으로 나누기
                            ai = Ai()
                            global bottle_kind
                            bottle_kind = ai.predict()
                            bottle_kind = bottle_kind[0]
                            global result
                            print("bottle's kind is {0}".format(bottle_kind))
                            if(bottle_kind in [0, 3, 5, 6, 7, 8, 10, 11, 15]):
                                    result = 3
                            elif(bottle_kind in [1, 12]):
                                    result = 1
                            else:
                                    result = 2
                            print("ai result is {0}".format(result))


                            # 결과값에 따라서 모터 pub & 음성 내보내기

                            if(result == 1):
                                client.publish("RPi/result", "1")
                                print("published 1 to esp8266")
                                th = threading.Thread(target=voice_1)
                                th.start()
                                full1 += 1
                            elif(result == 2):
                                client.publish("RPi/result", "2")
                                print("published 2 to esp8266")
                                th = threading.Thread(target=voice_2)
                                th.start()
                                full2 += 1
                            elif(result == 3):
                                client.publish("RPi/result", "3")
                                print("published 3 to esp8266")
                                th = threading.Thread(target=voice_3)
                                th.start()
                                full3 += 1
                            if(full1 == 3):
                                    pub(self.FULLTOPIC, self.FULLMESSAGE1)
                                    full1 = 0
                            elif(full2 == 3):
                                    pub(self.FULLTOPIC, self.FULLMESSAGE2)
                                    full2 = 0
                            elif(full3 == 3):
                                    pub(self.FULLTOPIC, self.FULLMESSAGE3)
                                    full3 = 0
                        

                        elif(msg.topic == "esp8266/rfid"):
                            global user_id
                            user_id  = msg.payload.decode()
                            global today_real 
                            today_real = str(datetime.date.today()).replace("-","")
                            global time_real 
                            time_real = datetime.datetime.now().strftime("%H%M%S")
                            t.sleep(9)
                            my_thread = threading.Thread(target=voice_start)
                            my_thread.start()
                            pub(self.RFIDTOPIC, user_id)

                def send_to_s3():
                        global user_id
                        global today_real
                        global time_real
                        global bottle_kind
                        global result
                        global order
                        
                        os.system("aws s3 cp image_data/통합본2/vita/pic.jpg s3://recycle-img/{0}_{1}_{2}_{3}_{4}_{5}.jpg".format(user_id, today_real, time_real, bottle_kind, result, order)) 

                def on_message_received(topic, payload, **kwargs):
                        global user_id

                        print("Received message from topic '{}': {}".format(topic, payload))
                        if(payload == b'end'):
                            # 종료 버튼 누르면 
                            start_thread = threading.Thread(target=voice_end)
                            start_thread.start()

                            th = threading.Thread(target=send_to_s3)
                            th.start()

                            client.publish("RPi/end", "4")
                            global order
                            order = 0
                        # elif(payload == b'start'):
                        #         voice_qr()
                                
                        #         # evt = threading.Event()
                        #         # th = threading.Thread(target=save_qr)
                        #         # th.start()
                        #         # evt.wait()
                        #         qr_data = qr()
                        #         print(qr_data)
                        #         t.sleep(4)
                        #         voice_start()
                        #         user_id = qr_data
                        #         pub(self.RFIDTOPIC, user_id)
                        #         client.publish("RPi/end", "5")
                                

                        self.received_count += 1
                        if self.received_count == 0:
                            self.received_all_event.set()


                # Sub
                def sub():
                        print("Subscribing to topic '{}'...".format(self.SUB_TOPIC))
                        subscribe_future, packet_id = mqtt_connection.subscribe(
                        topic=self.SUB_TOPIC,
                        qos=mqtt.QoS.AT_LEAST_ONCE,
                        callback=on_message_received)

                        subscribe_result = subscribe_future.result()
                        print("Subscribed with {}".format(str(subscribe_result['qos'])))

                        # Wait for all messages to be received.
                        # This waits forever if count was set to 0.
                        if self.COUNT != 0 and not self.received_all_event.is_set():
                                print("Waiting for all messages to be received...")
                        
                        client.connect("localhost")
                        client.loop_forever()

                        self.received_all_event.wait()
                        print("{} message(s) received.".format(self.received_count))


                # Pub
                def pub(pub_topic, pub_message):
                        print('Begin Publish')
                        data = "{}".format(pub_message)
                        message = {"message" : data}
                        mqtt_connection.publish(topic=pub_topic, payload=json.dumps(message), qos=mqtt.QoS.AT_LEAST_ONCE)

                        
                        print("Published: '" + json.dumps(message) + "' to the topic: " + pub_topic)
                        print('Publish End')

                        # print("Disconnecting...")
                        # disconnect_future = mqtt_connection.disconnect()
                        # disconnect_future.result()
                        # print("Disconnected!")
        
                
                self.received_count = 0
                self.received_all_event = threading.Event()

                client = Mqtt.Client()

                client.on_connect = on_connect
                client.on_message = on_message

                event_loop_group = io.EventLoopGroup(1)

                host_resolver = io.DefaultHostResolver(event_loop_group)
                client_bootstrap = io.ClientBootstrap(event_loop_group, host_resolver)
                mqtt_connection = mqtt_connection_builder.mtls_from_path(
                        endpoint=self.ENDPOINT,
                        cert_filepath=self.PATH_TO_CERT,
                        pri_key_filepath=self.PATH_TO_KEY,
                        client_bootstrap=client_bootstrap,
                        ca_filepath=self.PATH_TO_ROOT,
                        client_id=self.CLIENT_ID,
                        clean_session=False,
                        keep_alive_secs=6
                        )
                print("Connecting to {} with client ID '{}'...".format(
                        self.ENDPOINT, self.CLIENT_ID))
                # Make the connect() call
                connect_future = mqtt_connection.connect()
                # Future.result() waits until a result is available
                connect_future.result()
                print("Connected!")

                sub()
