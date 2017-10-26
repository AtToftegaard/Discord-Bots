import asyncio
import discord
from autocorrect import spell
import enchant
import re

client = discord.Client()
sleeping = False

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-------------')


@client.event
async def on_message(message):
    global sleeping
    skip = False
    if (client.user.mentioned_in(message)):
            sleeping = not(sleeping)
            await client.send_message(message.channel, '`I heard my name, so I will either sleep or wake up.`')
            skip = True
    if  (message.author != client.user and (not(sleeping) and not skip)):
        if not(message.content.endswith('.') or message.content.endswith('?') or message.content.endswith('!')):
            await client.send_message(message.channel, '`Remember full stops {}!`'.format(message.author.name))
        firstletter = message.content[:1]
        if not(firstletter.isupper()):
            await client.send_message(message.channel, '`Remember uppercase {}!`'.format(message.author.name))
        dic = enchant.Dict("en_us")
        corrWords = {}
        for word in message.content.split():
            word = re.sub('[!@#$]', '', word)
            if not (dic.check(word)):
                corrWords[word] = dic.suggest(word)
                probably = spell(word)
        for key in corrWords:
            await client.send_message(message.channel, '`Did you mean {}? Probably {}`'.format(corrWords[key], probably))
                
        

client.run('MzcyNjI4MDg1NjEyMjE2MzIw.DNHGVg.C1YYx4N6cv9uyz5ku-A0P24tJbs')