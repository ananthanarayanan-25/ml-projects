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

USERS = [
    'tech_guru_2026', 'python_lover', 'data_scientist_jane', 'ml_master',
    'cloud_ninja', 'dev_ops_pro', 'ai_enthusiast', 'code_with_sam',
    'stream_queen', 'kafka_king', 'opensearch_fan', 'workshop_winner'
]

CAPTIONS = [
    "Just deployed my first Kafka pipeline! 🚀 #kafka #streaming #python",
    "Real-time data is the future! #opensearch #data",
    "Building cool stuff at the workshop today! #workshop #learning #tech",
    "My first event-driven app is live! 💻 #eventdriven #kafka #python",
    "Streaming data like a pro 😎 #streaming #realtime #bigdata",
    "OpenSearch dashboards are amazing! #visualization #analytics #opensearch",
]

def generate_post():
    return {
        "username": random.choice(USERS),
        "caption": random.choice(CAPTIONS),
        "likes": random.randint(10, 5000),
        "comments": random.randint(0, 500),
        "timestamp": datetime.utcnow().isoformat()
    }

if __name__ == "__main__":
    print("Producing Instagram posts to Kafka...")
    while True:
        data = generate_post()
        producer.send(KAFKA_TOPIC, data)
        print("Sent:", data)
        time.sleep(random.uniform(1, 3))