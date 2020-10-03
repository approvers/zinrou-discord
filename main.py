import asyncio

import discord

from on_message import MessageRoot


class MainClient(discord.Client):
    def __init__(self, token):
        super()
        self.token = token

    def run(self, token):
        super(token)

    def on_ready(self):
        pass

    async def on_message(self, message:discord.Message):
        if message.content.startswith("!z"):
            parsed = MessageRoot(message)

    async def message_sender(self, channel, content):
        pass


if __name__ == "__main__":
    token = ""
    bot = MainClient(token)
