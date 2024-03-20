import paho.mqtt.client as mqtt

# Define MQTT broker settings
broker_address = "localhost"  # Change this to your MQTT broker's address
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
client.connect(broker_address, 1883, 60)

# Start the MQTT client loop to process messages
client.loop_forever()
