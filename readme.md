Initial Outline:

1. Setup various source for kafka like:
   - A docker image producing data to websocket. 
   - An API based app in python that is continuously generating data. 
   - An existing API like weather API, Twitter API etc 





Libraries used for websocket
pip install websocket-client
pip install websockets

### How to kill websocket app 

1. Get the process id:
```
ps aux | grep python
```

2. Kill the process: 
```
kill -9 <pid>
```

## Note: Create a Topic Before Producing:
```shell
kafka-topics.sh --create --topic websocket_s3d --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```


## List Kafka Topics
```shell
kafka-topics.sh --list --bootstrap-server localhost:9092

```
![list_kafka_topic.png](resources/img/list_kafka_topic.png)


## Producing to kafka
![kafka_producer.png](resources/img/kafka_producer.png)