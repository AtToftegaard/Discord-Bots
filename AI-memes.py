import asyncio
import discord
import re
import random
import Config

client = discord.Client()
sleeping = False

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-------------')

@client.event
async def on_message(message: discord.Message):
    global sleeping
    if message.author == client.user:
        return
    if message.content
    await message.channel.send('Hello!')
        
client.run(Config.AI_memes_token)