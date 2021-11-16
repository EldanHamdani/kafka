import time
import json
import random
from datetime import datetime
#from data_generator import generate_message
from kafka import KafkaProducer
import requests
import sys
import time


# Messages will be serialized as JSON
def json_serializer(dummy_message):
    return json.dumps(dummy_message).encode('utf-8')


# Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=['34.219.55.140:9092'],
    value_serializer=json_serializer,
    api_version=(0, 10, 1)
)


if __name__ == '__main__':
    # Infinite loop - runs until you kill the program
    #while True:
        # Generate a message
       # dummy_message = generate_message()

        # Send it to our 'messages' topic
        while True:
          sys.stdout = open("json.txt", "w")
          response = requests.get("https://api.instantwebtools.net/v1/airlines/")
          response = response.json()
          counter=1
          for id in response:
            dummy_message = ""
            if (counter < 10000):
              if ('name' in id):
                dummy_message += "name: " + str(id["name"])
              if ('country' in id):
                dummy_message += " country: " + str(id["country"])
              if ('slogan' in id):
                dummy_message += " slogan: " + str(id["slogan"])
              if ('established' in id):
                dummy_message += " established: " + str(id["established"])
            counter = counter + 1
            #print (dummy_message)
            print('\nProducing message: {}'.format(dummy_message))
            producer.send('messages', dummy_message)

        # Sleep for a random number of seconds
        time.sleep(10)
        sys.stdout.close()
