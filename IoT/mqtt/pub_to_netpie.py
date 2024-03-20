import paho.mqtt.publish as publish

# Define MQTT broker settings
broker_address = "mqtt.netpie.io:1883"  # Change this to your MQTT broker's address
topic = "test/topic"
client_id = "e8c0fbbf-dd1c-4f84-b500-a3bfb8b3a6c6"  # Client ID

# Publish "hello world" message
publish.single(topic, "hello world", hostname=broker_address, client_id=client_id)
