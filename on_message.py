import discord


class MessageRoot:
    def __init__(self, message: discord.Message):
        self.message = message
        self.content = message.contet
        self.author = message.author.display_name
        self.decide()

    def parser(self):
        if len(self.content.split()) == 1:
            pass
        pass
