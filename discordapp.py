import asyncio
import discord
import keep_alive
import os
os.system("pip3 install slack_sdk")
import time
from discord.ext import commands
#import watch

bot = commands.Bot(command_prefix="anoop!")

@bot.event
async def on_ready():
  print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

async def my_message(message):
  if message.author == bot.user:
    return

  if message.content.startswith("hello there"):
    await message.channel.send("General Kenobi! you are a bold one")

def announcement(message, announcement):
  print("announcing")
  announcement = watch.watchandwrite()
  message.channel.send(announcement)

bot.add_listener(my_message, 'on_message')

keep_alive.keep_alive()

bot.run(os.getenv('DISCORD_TOKEN'), bot=True, reconnect=True)