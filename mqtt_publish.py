import paho.mqtt.client as mqtt_client

broker = 'localhost'
port = 8000
# topic = "python/mqtt"
# Generate a Client ID with the publish prefix.
client_id = f'publish-{410}'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def publish(client, topic, msg):
    result = client.publish(topic, msg)
    status = result[0]
    if status == 0:
        print(f"Send `{msg}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")


# def run():
#     client = connect_mqtt()
#     client.loop_start()
#     publish(client)
#     client.loop_stop()