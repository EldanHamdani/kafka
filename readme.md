**Containers Architechture:**

In the following diagram we can ses the all the containers and how they are comunicating each other.
if we want access to kafka manager in order to manage all the topic, partitions etc- we will access with port 9000- http://<ip>:9000
the external and internal port of kafka is 9092, and 2181 for zookeeper.
In addtion we can see that exists on my architecture two additional containers:
  producer- contains python script which get data from instegram api, extract the relevant inform
  ation and send it to kafka.
  consumer- contains python script which recieve the messages from the fafka.
![image](https://user-images.githubusercontent.com/93048074/142061074-427dc4f3-18ee-4eee-bd99-e807723c073c.png)

On my assigment I have the following architecture:
producer which send data to a topic with 1 partition on kafka cluster (the topic called-"messages").
Kafka container streaming the data and the consumer gets his data from that topic.  
![image](https://user-images.githubusercontent.com/93048074/142082967-0c396205-c80b-4638-a82d-c9b5927e17ff.png)

  
**simple flow:**
1. run docker-compose for creating all the containers (kafka, zookeeper, kafka manager, producer, consumer)
   docker-compose -f docker-compose.yml up -d
2. docker ps
![image](https://user-images.githubusercontent.com/93048074/142083494-6a412693-9351-4fa4-b281-6d0490fe475c.png)

3. now you can check if the consumer indeed get the data from the kafka by running:
   docker logs <consumer_container_id>
   for example:
  ![image](https://user-images.githubusercontent.com/93048074/142083975-0c8b79e6-d499-4b5b-aadc-2c8115a510d8.png)

4. connect to kafka manager and see that latest offset increaced:
  ![image](https://user-images.githubusercontent.com/93048074/142084200-963eaae2-899f-4193-8c67-495f84bd2192.png)
