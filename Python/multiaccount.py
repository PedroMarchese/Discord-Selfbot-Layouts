import discord
import asyncio

# THE FIRST ONE IS FOR XYLIASE LIST =]
# tokens = list(map(lambda t : t.split(':')[2], open('tokens.txt', 'r', encoding='utf-8').readlines()))

# THIS IS FOR A LIST WITH ONLY TOKENS SEPARETED LINE BY LINE
tokens = open('tokens.txt', 'r', encoding='utf-8').readlines()

# HERE THE PROGRAM STARTS
async def main():
    while True:
        for token in tokens:
            client = discord.Client()

            @client.event
            async def on_ready():
                print(f'Logged on as {client.user.name}')
                await asyncio.sleep(5)
                await client.close()

            try:
                # HERE YOU NEED TO PAY ATTENTION CUZ IF YOU'RE NOT USING DISCORD.PY-SELF, THEN YOU 
                # MUST SPECIFY WHEN YOU'RE USING AN USER ACCOUNT WITH BOT PARAMETER
                client.loop.run_until_complete(await client.start(token)) # FOR DISCORD.PY-SELF
                # client.loop.run_until_complete(await client.start(token, bot=False)) # FOR STANDARD DISCORD.PY
            except Exception as e:
                continue

asyncio.run(main())