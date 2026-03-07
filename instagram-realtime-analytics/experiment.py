import time
import random
from kafka import KafkaProducer
import json
from datetime import datetime

KAFKA_BOOTSTRAP_SERVERS = 'localhost:9092'
KAFKA_TOPIC = 'instagram-feed'

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Realistic simulated Instagram data for workshop demo
USERS = [
    'tech_guru_2026', 'python_lover', 'data_scientist_jane', 'ml_master', 
    'cloud_ninja', 'dev_ops_pro', 'ai_enthusiast', 'code_with_sam',
    'stream_queen', 'kafka_king', 'opensearch_fan', 'workshop_winner'
]

CAPTIONS = [
    "Just deployed my first Kafka pipeline! 🚀 #kafka #streaming #python",
    "Real-time data is the future! Who else is learning OpenSearch? #opensearch #data",
    "Building cool stuff at the workshop today! #workshop #learning #tech",
    "My first event-driven app is live! 💻 #eventdriven #kafka #python",
    "Streaming data like a pro now 😎 #streaming #realtime #bigdata",
    "OpenSearch dashboards are amazing! #visualization #analytics #opensearch",
    "Learning Kafka and loving it! #kafka #messaging #devops",
    "Data engineering is my new passion! #dataengineering #career #tech",
    "Who knew real-time analytics could be this fun? #analytics #streaming",
    "From classroom to cloud! ☁️ #cloud #learning #python #workshop",
    "Just indexed my first million records! #opensearch #bigdata #milestone",
    "Event streaming workshop was amazing! #workshop #kafka #opensearch",
]

HASHTAGS_POOL = [
    ['#kafka', '#streaming', '#python'],
    ['#opensearch', '#data', '#analytics'],
    ['#workshop', '#learning', '#tech'],
    ['#eventdriven', '#kafka', '#python'],
    ['#streaming', '#realtime', '#bigdata'],
    ['#visualization', '#analytics', '#opensearch'],
    ['#kafka', '#messaging', '#devops'],
    ['#dataengineering', '#career', '#tech'],
    ['#analytics', '#streaming', '#realtime'],
    ['#cloud', '#learning', '#python', '#workshop'],
]

def generate_instagram_post():
    user = random.choice(USERS)
    caption = random.choice(CAPTIONS)
    hashtags = random.choice(HASHTAGS_POOL)
    return {
        'username': user,
        'caption': caption,
        'likes': random.randint(10, 5000),
        'comments': random.randint(0, 500),
        'hashtags': hashtags,
        'timestamp': datetime.utcnow().isoformat(),
        'url': f'https://www.instagram.com/p/{random.randint(100000, 999999)}/'
    }

if __name__ == '__main__':
    print('Producing simulated Instagram posts to Kafka in real-time...')
    print('Press Ctrl+C to stop.')
    try:
        while True:
            data = generate_instagram_post()
            producer.send(KAFKA_TOPIC, data)
            print(f"Sent: {data}")
            time.sleep(random.uniform(1, 3))  # Random delay for realism
    except KeyboardInterrupt:
        print('\nStopped producing posts.')