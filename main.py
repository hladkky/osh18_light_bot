import asyncio
import os

import dotenv

from grpc_client import GRPCClient
from socket_state_subject import socket_state_subject
from telegram_bot_client.observer import TelegramBotObserver


async def main():
    client = GRPCClient()

    task = asyncio.create_task(client.start_power_monitoring(socket_state_subject))
    socket_state_subject.subscribe(TelegramBotObserver())

    await task


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
