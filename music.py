import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import colorsys
import random
import os
import youtube_dl

client = Bot(command_prefix="d!", pm_help = True)
client.remove_command('help')


@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------')
    print('--------')
    print('Started BOT')
    print('Created by Utkarsh')

@client.command(pass_context=True)
async def play(ctx, url):
          server = ctx.message.server
          voice_client = client.voice.client_in
          player = await voice_client.create_ytdl_player(url)
          players[server.id] = player
          player.start()

@client.command(pass_context= True)
async def leave(ctx):
         server = ctx.message.server
         voice.client = client.voice_client_in(server)
         await voice_client.disconnect()

