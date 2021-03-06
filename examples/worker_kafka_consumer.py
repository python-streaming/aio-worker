import os

from aiokafka import AIOKafkaConsumer

from aioworker import Worker


BOOTSTRAP_SERVERS = os.getenv("BOOTSTRAP_SERVERS", "0.0.0.0:9092")
TOPIC = os.getenv("BOOTSTRAP_SERVERS", "test-topic-worker")
GROUP_ID = os.getenv("GROUP_ID", "test-consumer-group")
AUTO_OFFSET_RESET = os.getenv("AUTO_OFFSET_RESET", "earliest")

# Steps:
#  1. pip install aiokafka
#  2. make run-kafka-cluster
#  3. make create-topic
#  4. Execute `make send-event` to open a terminal with a prompt and type your events


async def consume_from_kafka(loop):
    print("Task Consuming from kafka initiated...")
    consumer = AIOKafkaConsumer(
        TOPIC,
        loop=loop,
        bootstrap_servers=BOOTSTRAP_SERVERS,
        group_id=GROUP_ID,
        auto_offset_reset=AUTO_OFFSET_RESET,
    )

    # Get cluster layout and join group `my-group`await consumer.start()
    await consumer.start()

    try:
        # Consume messages
        async for msg in consumer:
            print(f"Task Consuming from kafka")
            print(
                f"Topic: {msg.topic}, Partition: {msg.partition}, Offset: {msg.offset},"
                f" Key: {msg.key}, Value: {msg.value}, Timestamp: {msg.timestamp}\n"
            )
    finally:
        # Will leave consumer group; perform autocommit if enabled.
        await consumer.stop()


if __name__ == "__main__":
    #  Run the server using 1 worker processes.
    Worker(tasks=[consume_from_kafka]).run(workers=1)
