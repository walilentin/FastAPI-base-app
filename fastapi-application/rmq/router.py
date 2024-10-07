from fastapi import APIRouter
from aio_pika import Message

from rmq.connection import get_connection

router = APIRouter()


@router.post("/send")
async def send_message(message: str):
    connection = await get_connection()
    async with connection:
        channel = await connection.channel()
        queue = await channel.declare_queue("test_queue", durable=True)
        await channel.default_exchange.publish(
            Message(message.encode("utf-8")), routing_key=queue.name
        )
    return {"message": "Message sent"}


@router.get("/receive")
async def receive_message():
    connection = await get_connection()
    async with connection:
        channel = await connection.channel()
        queue = await channel.declare_queue("test_queue", durable=True)
        async with queue.iterator() as queue_iter:
            async for message in queue_iter:
                async with message.process():
                    return {"message": message.body.decode("utf-8")}

    return {"message": "No messages"}
