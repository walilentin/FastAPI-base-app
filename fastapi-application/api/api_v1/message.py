from typing import Annotated

from fastapi import APIRouter, Depends
from aio_pika import Message

from api.dependencies.auth.f_users import current_user
from core.config import settings
from core.models import User
from rmq.connection import get_connection

router = APIRouter(prefix=settings.api.v1.message, tags=["Message"])


@router.post("/send")
async def send_message(
    receiver_id: int,
    message: str,
    user: Annotated[User, Depends(current_user)],
):
    connection = await get_connection()
    async with connection:
        channel = await connection.channel()
        queue_name = f"user_{receiver_id}_queue"
        queue = await channel.declare_queue(queue_name, durable=True)
        full_message = f"From {user.id}: {message}"

        await channel.default_exchange.publish(
            Message(full_message.encode("utf-8")), routing_key=queue.name
        )
    return {"message": "Message sent"}


@router.get("/receive")
async def receive_message(user: Annotated[User, Depends(current_user)]):
    connection = await get_connection()
    async with connection:
        channel = await connection.channel()
        queue_name = f"user_{user.id}_queue"
        queue = await channel.declare_queue(queue_name, durable=True)

        async with queue.iterator() as queue_iter:
            async for message in queue_iter:
                async with message.process():
                    return {"message": message.body.decode("utf-8")}

    return {"message": "No messages"}
