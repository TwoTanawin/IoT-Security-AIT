import paho.mqtt.publish as publish

# Define MQTT broker settings
broker_address = "localhost"  # Change this to your MQTT broker's address
topic = "test/topic"

# Publish "hello world" message
publish.single(topic, "hello Arsenal 3 - 1 Liverpool", hostname=broker_address)
