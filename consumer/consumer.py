from kafka import KafkaConsumer
import json
if __name__ == "__main__":
  consumer = KafkaConsumer(
       "messages",
       bootstrap_servers='34.219.55.140:9092',
       auto_offset_reset='earliest',
       api_version=(0, 10, 1),
       group_id="messages")
  print("starting the consumer")
  for msg in consumer:
    print("messages = {}".format(json.loads(msg.value)))
