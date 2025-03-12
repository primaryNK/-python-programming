import discord
import asyncio

async def test():
    print("Hello World")

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await test()

client.run('TOKEN')