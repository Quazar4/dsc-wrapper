import discord

class DiscordWrapper:
    def __init__(self, token):
        self.token = token
        self.client = discord.Client()

        @self.client.event
        async def on_ready():
            print(f'Logged in as {self.client.user.name} ({self.client.user.id})')

        @self.client.event
        async def on_message(message):
            if message.author == self.client.user:
                return

            if message.content.startswith('!hi'):
                await message.channel.send('Hello!')

    def run(self):
        self.client.run(self.token)

wrapper = DiscordWrapper('TOKEN')
wrapper.run()
