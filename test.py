import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import colorsys
import random
import os

client = Bot(command_prefix="d!", pm_help = True)
client.remove_command('help')


@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------')
    print('--------')
    print('Started BOT')
    print('Created by Utkarsh')
    return await client.change_presence(game=discord.Game(name='Looking for d!help'))

@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def setup(ctx):
    author = ctx.message.author
    server = ctx.message.server
    mod_perms = discord.Permissions(=True)
    await client.create_role(author.server, name="Owner", permissions=perms)
    await client.create_role(author.server, name="Admin")
    await client.create_role(author.server, name="G.O.H")
    await client.create_role(author.server, name="Moderator")
    await client.create_role(author.server, name="Muted")
    await client.create_role(author.server, name="Trial Moderator")
    await client.create_role(author.server, name="Friend of Owner")
    await client.create_role(author.server, name="Verified")
    everyone_perms = discord.PermissionOverwrite(send_messages=False, read_messages=True)
    everyone = discord.ChannelPermissions(target=server.default_role, overwrite=everyone_perms)
    user_perms = discord.PermissionOverwrite(read_messages=True)
    user = discord.ChannelPermissions(target=server.default_role, overwrite=user_perms)
    private_perms = discord.PermissionOverwrite(read_messages=False)
    private = discord.ChannelPermissions(target=server.default_role, overwrite=private_perms)    
    await client.create_channel(server, 'welcome',everyone)
    await client.create_channel(server, 'rules',everyone)
    await client.create_channel(server, 'announcements',everyone)
    await client.create_channel(server, 'featured_content',everyone)
    await client.create_channel(server, 'chatting_here',user)
    await client.create_channel(server, 'bots_zone',user)
    await client.create_channel(server, 'private_chat',private)
    await client.create_channel(server, 'Music Zone', type=discord.ChannelType.voice)
    await client.create_channel(server, 'music_commands',user)

