from kafka import KafkaConsumer
from opensearchpy import OpenSearch
import json

consumer = KafkaConsumer(
    "instagram-feed",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    group_id="os-group",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

os_client = OpenSearch(
    hosts=[{"host": "localhost", "port": 9200}],
    http_auth=("admin", "admin"),
    use_ssl=True,
    verify_certs=False,
    ssl_assert_hostname=False,
    ssl_show_warn=False
)

print("Consuming from Kafka and indexing into OpenSearch...")

for message in consumer:
    data = message.value
    os_client.index(index="instagram-posts", body=data)
    print("Indexed:", data["username"], "| Likes:", data["likes"])