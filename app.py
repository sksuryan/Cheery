#loads .env file
from dotenv import load_dotenv
load_dotenv()

import os
import random
import discord
from messages import returnRandomMessage, addUserMessage
from discord.ext import commands, tasks
from filters import filterBots, filterTextChannels

#gets client id for Bot
BOT=os.environ.get('BOT')

#enables permissions which allows Bot to get list of users etc.
intents = discord.Intents.all()

#Bot object
client = commands.Bot(command_prefix = '-',intents=intents)

textChannels = []

#executes when the Bot is readt
@client.event
async def on_ready():
    global textChannels 
    
    textChannels = list(client.get_all_channels())
    textChannels = list(filter(filterTextChannels, textChannels))

    print('Bot is ready!')
    motivateMe.start()

#command for appreciating a random person with a random text
@client.command(
    name='Random Moment of Appreciation',
    brief='- shorthand "-r", tags a random person',
    aliases=['r'],
    description='command for appreciating a random person with a random wholesome text, use shorthand "-r" for it.')
async def randomMomentOfAppreciation(ctx):
    channel = ctx.message.channel

    if type(channel) != discord.DMChannel:
        users = channel.members

        sentBy = ctx.author

        users.remove(sentBy)
        users = list(filter(filterBots,users))

        userIndex = random.randint(0,len(users)-1)

        await ctx.send(f'<@{users[userIndex].id}> {returnRandomMessage()}')

    else:
        sentBy = ctx.author
        await ctx.send(f'<@{sentBy.id}> {returnRandomMessage()}')

#command to add a new message in the message db
@client.command(
    name='Add your own messages',
    aliases=['a'],
    brief='- use shorthand "-a <message>" to add a message')
async def addANewMessage(ctx,*,msg):
    addUserMessage(msg)
    sentBy = ctx.author

    await ctx.send(f'<@{sentBy.id}> thank you! Have a lovely day or night! Idk your timezone, oof this is awkward👉👈')

#background loop that executes after a given time interval
#used to send a random message for motivation to text channels
@tasks.loop(hours=4)
async def motivateMe():
    for channel in textChannels:
        await channel.send(f"{returnRandomMessage()}")

client.run(BOT)