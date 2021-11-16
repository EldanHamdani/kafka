**Containers Architechture:**

In the following diagram we can ses the all the containers and how they are comunicating each other.
if we want access to kafka manager in order to manage all the topic, partitions etc- we will access with port 9000- http://<ip>:9000
the external and internal port of kafka is 9092, and 2181 for zookeeper.
In addtion we can see that exists on my architecture two additional containers:
  producer- contains python script which get data from instegram api, extract the relevant information and send it to kafka.
  consumer- contains python script which recieve the messages from the fafka.
![image](https://user-images.githubusercontent.com/93048074/142061074-427dc4f3-18ee-4eee-bd99-e807723c073c.png)

On my assigment I have the following architecture:
producer which send data to a topic with 1 partition on kafka cluster (the topic called-"messages").
Kafka container streaming the data and the consumer gets his data from that topic.  
![image](https://user-images.githubusercontent.com/93048074/142082967-0c396205-c80b-4638-a82d-c9b5927e17ff.png)
