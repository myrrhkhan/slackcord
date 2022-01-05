'''from dotenv import load_dotenv

load_dotenv()'''

import discord
import keep_alive
import os

import time
from discord.ext import commands

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
		f = open("message.txt", "w")
		f.write("hello there")
		f.close()
		await message.channel.send("General Kenobi! you are a bold one!\nsending message to slack")


bot.add_listener(my_message, 'on_message')

keep_alive.keep_alive()

bot.run(os.environ['DISCORD_TOKEN'], bot=True, reconnect=True)