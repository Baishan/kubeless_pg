from kafka import KafkaConsumer
import pprint

print 'hello'
try:
    consumer = KafkaConsumer('hello', bootstrap_servers='broker.kubeless:9092')
    for msg in consumer:
        print msg
except Exception as e:
    print str(e)

