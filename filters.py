import discord

#function to filter bots from users
def filterBots(user):
    return not user.bot

#used to filter text channels from rest of the channels
def filterTextChannels(channel):
    if channel.type == discord.ChannelType.text:
        return True
    else:
        return False