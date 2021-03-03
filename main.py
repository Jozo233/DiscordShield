import random
import requests
import youtube_dl
import discord
import json
import os
import dotenv
import flask
import keep_alive

from keep_alive import keep_alive
from discord.ext import commands
from dotenv import load_dotenv


client = discord.Client()
client = commands.Bot(command_prefix="/")
client.remove_command("help")
load_dotenv()
TOKEN = os.getenv('TOKEN')




@client.event  # zaciatok
async def on_ready():
    print("-------------")
    print(client.user.name)
    print(client.user.id)
    print(discord.__version__)
    print(client.latency * 1000)
    print("-------------")

    guild_members = len(set(client.get_all_members()))
    await client.change_presence(activity=discord.Game(name='na {} serveru'.format(guild_members)))






@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
        
keep_alive()
client.run('TOKEN')
