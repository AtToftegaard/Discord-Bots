import asyncio
import discord
from autocorrect import spell

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-------------')

@client.event
async def on_message(message):
    if  (message.author != client.user):
        if not(message.content.endswith('.') or message.content.endswith('?') or message.content.endswith('!')):
            await client.send_message(message.channel, '`Remember full stops {}!`'.format(message.author.name))
        firstletter = message.content[:1]
        if not(firstletter.isupper()):
            await client.send_message(message.channel, '`Remember uppercase {}!`'.format(message.author.name))
        
        

client.run('MzcyNjI4MDg1NjEyMjE2MzIw.DNHGVg.C1YYx4N6cv9uyz5ku-A0P24tJbs')