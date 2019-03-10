from kafka import KafkaProducer
import pprint

print 'hello'
try:
    producer = KafkaProducer(bootstrap_servers='bootstrap.kafka:9092')
    for x in range(100):
        producer.send('hello', b'hello brian' + str(x))

    producer.flush()
except Exception as e:
    print str(e)

