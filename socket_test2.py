import websocket
import time
 
ws = websocket.WebSocket()
ws.connect("ws://192.168.35.90/")
 

ws.send("hahahah jonga~~~~~~~~~~")

 
ws.close()