from kafka import KafkaProducer

def read(event, context):
    print event['data']
    return event['data']

def sayhello(event, context):
    try:
        producer = KafkaProducer(bootstrap_servers='broker.kubeless:9092')
        for x in range(1000):
            producer.send('hello', event['data'] +'_'+ str(x))

        producer.flush()
        return "wrote 1000"
    except Exception as e:
        return str(e)

def writepayload(event, context):
    try:
        producer = KafkaProducer(bootstrap_servers='broker.kubeless:9092')
        payload = """
        {
            "workflowType": "oracle-code-tweet-processor",
            "workflowConversationIdentifier": "OracleCodeTweetProcessor1525151206872",
            "creationTimeStamp": 1525148332841,
            "creator": "WorkflowLauncher",
            "audit": [
                {
                    "when": 1525148332841,
                    "who": "WorkflowLauncher",
                    "what": "creation",
                    "comment": "initial creation of workflow"
                },
                {
                    "when": 1525151212318,
                    "who": "TweetBoard",
                    "what": "update",
                    "comment": "Tweet Board Capture done"
                }
            ],
            "payload": {
                "text": "#556 Today is a microservice workshop at Fontys Hogeschool in Eindhoven",
                "author": "lucasjellema",
                "authorImageUrl": "http://pbs.twimg.com/profile_images/427673149144977408/7JoCiz-5_normal.png",
                "createdTime": "May 9th, 2018 at 08:39AM",
                "tweetURL": "http://twitter.com/SaibotAirport/status/853935915714138112",
                "firstLinkFromTweet": "https://t.co/cBZNgqKk0U",
                "enrichment": "Lots of Money",
                "translations": [
                    "# 556 Heute ist ein Microservice-Workshop in der Fontys Hogeschool in Eindhoven",
                    "# 556 Vandaag is een microservice-workshop aan de Fontys Hogeschool in Eindhoven"
                ]
            },
            "updateTimeStamp": 1525151212318,
            "lastUpdater": "TweetBoard"
            }
        """

        producer.send('hello', payload )

        producer.flush()
        return "wrote 1"
    except Exception as e:
        return str(e)
