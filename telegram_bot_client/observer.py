import asyncio
import json
from pathlib import Path

import loguru
from aiogram import Bot
from rx.core import Observer

from constants import TELEGRAM_BOT_TOKEN, TARGET_CHAT_ID


class TelegramBotObserver(Observer):
    def __init__(self):
        super().__init__()

        self._bot = Bot(TELEGRAM_BOT_TOKEN)

    def on_next(self, value):
        self._send_light_message(value)

    def _send_light_message(self, value):
        loguru.logger.debug(f"Value for telegram message: {value}")
        if value:
            self._send_light_exists_message()
        else:
            self._send_light_not_exists_message()

    def _send_light_exists_message(self):
        asyncio.run_coroutine_threadsafe(
            self._bot.send_message(TARGET_CHAT_ID, "Світло зʼявилось!"),
            asyncio.get_event_loop()
        )

    def _send_light_not_exists_message(self):
        asyncio.run_coroutine_threadsafe(
            self._bot.send_message(TARGET_CHAT_ID, "Світло зникло!"),
            asyncio.get_event_loop()
        )
