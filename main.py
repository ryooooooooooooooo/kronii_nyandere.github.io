import discord
import os
import datetime
import time
import pytz

from infinity import infinity

client = discord.Client()
orass = ["oras","orass","oras check","time check","ORAS CHEC","ORAS CHECK"]
aa = ["clock-chan","oras-chan","oras chan","clock chan"]

@client.event
async def on_ready():
  print("the kronii-copter has landed".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  a = message.content
  b = a.split()
  output = message.channel
  orasss = a.startswith("oras")
  timee = a.startswith("time")  

  if any(word in a for word in aa):
    await output.send("im a warden , not a clock, get your facts right")

  oras = datetime.datetime.now(pytz.timezone('Asia/Manila'))
  if orasss or timee is True:
      await message.channel.send(oras.strftime(r"%I:%M %p"))


infinity()
client.run(os.environ['kronii'])