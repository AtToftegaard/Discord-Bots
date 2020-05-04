import asyncio
import discord
from autocorrect import spell
import enchant
import re
import random

snarkycomments =   ['Not sure why I even bother.', 
                    'But hey what do I know?',
                    'It happens to the best.', 
                    'It can happen to all of us.', 
                    'Not trying to get in your head or anything.',
                    'Kind of a rookie mistake.',
                    'What we in the business call "shit spelling".',
                    'How could that even happen?',
                    'Whoopsie-daisie.',
                    'That is pretty bad.'
                    'You did go to school right?']

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
    dic = enchant.Dict("en_us")
    suggestions = {}

    if (client.user.mentioned_in(message)):
        if (sleeping):
            await client.send_message(message.channel, '`I heard my name, so I will wake up.`')
        else:
            await client.send_message(message.channel, '`I heard my name, so I will sleep.`')
        sleeping = not(sleeping)
        skip = True
        
    if  (message.author != client.user and not(sleeping) and not skip):   

        message.content = re.sub('-', ' ', message.content)
        for word in message.content.split():
            word = re.sub('[!@#$?,.]', '', word)
            if not (dic.check(word)):
                probably = spell(word)
                if probably == word:
                    continue
                suggestions[word] = dic.suggest(word)
        
        for key in suggestions:
            if (random.randint(1,10) <= 2):
                await client.send_message(message.channel, '`You probably meant "{}" instead of {}. {}`'.format(probably, word, random.choice(snarkycomments)))
            else:
                await client.send_message(message.channel, '`You probably meant "{}" instead of {}.`'.format(probably, word))        
        
client.run()