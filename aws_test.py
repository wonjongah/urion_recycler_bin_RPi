# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

from awscrt import io, mqtt, auth, http
from awsiot import mqtt_connection_builder
import time as t
import json
import sys
import threading
from uuid import uuid4

# Define ENDPOINT, CLIENT_ID, PATH_TO_CERT, PATH_TO_KEY, PATH_TO_ROOT, MESSAGE, TOPIC, and RANGE
ENDPOINT = "YOUR_ENDPOINT"
CLIENT_ID = "wontest2"
PATH_TO_CERT = "certificate.pem.crt"
PATH_TO_KEY = "private.pem.key"
PATH_TO_ROOT = "root.pem"
MESSAGE = "this is jongah~~~~~~~~!!!!!!!!!!!!!!!!!!"
TOPIC = "test/testing"
SUB_TOPIC = "test/testing"
RANGE = 20
COUNT = 0
received_count = 0
received_all_event = threading.Event()

def on_message_received(topic, payload, **kwargs):
    print("Received message from topic '{}': {}".format(topic, payload))
    if(payload == b'end'):
        pub()

    global received_count
    received_count += 1
    if received_count == 0:
        received_all_event.set()


# Sub
def sub():
        print("Subscribing to topic '{}'...".format(SUB_TOPIC))
        subscribe_future, packet_id = mqtt_connection.subscribe(
        topic=SUB_TOPIC,
        qos=mqtt.QoS.AT_LEAST_ONCE,
        callback=on_message_received)

        subscribe_result = subscribe_future.result()
        print("Subscribed with {}".format(str(subscribe_result['qos'])))

        # Wait for all messages to be received.
        # This waits forever if count was set to 0.
        if COUNT != 0 and not received_all_event.is_set():
                print("Waiting for all messages to be received...")

        received_all_event.wait()
        print("{} message(s) received.".format(received_count))


# Pub
def pub():
        print('Begin Publish')
        data = "{}".format(MESSAGE)
        message = {"message" : data}
        mqtt_connection.publish(topic=TOPIC, payload=json.dumps(message), qos=mqtt.QoS.AT_LEAST_ONCE)

        print("Published: '" + json.dumps(message) + "' to the topic: " + "'test/testing'")
        print('Publish End')

        # print("Disconnecting...")
        # disconnect_future = mqtt_connection.disconnect()
        # disconnect_future.result()
        # print("Disconnected!")


if __name__ == "__main__":
        # Spin up resources
        event_loop_group = io.EventLoopGroup(1)
        host_resolver = io.DefaultHostResolver(event_loop_group)
        client_bootstrap = io.ClientBootstrap(event_loop_group, host_resolver)
        mqtt_connection = mqtt_connection_builder.mtls_from_path(
                endpoint=ENDPOINT,
                cert_filepath=PATH_TO_CERT,
                pri_key_filepath=PATH_TO_KEY,
                client_bootstrap=client_bootstrap,
                ca_filepath=PATH_TO_ROOT,
                client_id=CLIENT_ID,
                clean_session=False,
                keep_alive_secs=6
                )
        print("Connecting to {} with client ID '{}'...".format(
                ENDPOINT, CLIENT_ID))
        # Make the connect() call
        connect_future = mqtt_connection.connect()
        # Future.result() waits until a result is available
        connect_future.result()
        print("Connected!")

        sub()
        pub()
        
