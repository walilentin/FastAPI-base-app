import logging
import aio_pika
from core.config import settings


async def get_connection() -> aio_pika.Connection:
    connection = await aio_pika.connect_robust(
        host=settings.rmq.rmq_host, port=settings.rmq.rmq_port
    )
    return connection


def configure_logging(level: int = logging.INFO):
    logging.basicConfig(
        level=level,
        datefmt="%Y-%m-%d %H:%M:%S",
        format="[%(asctime)s.%(msecs)03d] %(funcName)20s %(module)s:%(lineno)d %(levelname)-8s - %(message)s",
    )
