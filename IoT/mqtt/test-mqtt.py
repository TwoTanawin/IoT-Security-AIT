import paho.mqtt.client as mqtt
import time

# Define MQTT broker settings
broker_address = "localhost"  # Change this to your MQTT broker's address
broker_port = 1883
topic = "test/topic"

# Define callback functions for MQTT events
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribe to the topic when connected
    client.subscribe(topic)

def on_message(client, userdata, msg):
    print("Received message: "+str(msg.payload.decode()))

# Create MQTT client instance
client = mqtt.Client()

# Assign callback functions to client
client.on_connect = on_connect
client.on_message = on_message

# Connect to MQTT broker
client.connect(broker_address, broker_port, 60)

# Start the MQTT client loop to process messages
client.loop_start()

# Publish "hello world" message
client.publish(topic, "hello my IoT")

# Wait for a moment to receive the message
time.sleep(2)

# Disconnect from the MQTT broker
client.disconnect()
