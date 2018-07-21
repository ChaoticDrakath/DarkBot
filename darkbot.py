import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import os

client = Bot(description="DarkBot Bot is best", command_prefix="d!", pm_help = False)


@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------')
    print('--------')
    print('Started Dark BOT')
    print('Created by Utkarsh')
    return await client.change_presence(game=discord.Game(name='Looking for d!help'))

@client.event
async def on_member_join(member):
    print("In our server" + member.name + " joined just joined")
    await client.send_message(member, newUserMessage)
    print("Sent message to " + member.name)

@client.command(pass_context=True)  
@commands.has_permissions(kick_members=True)     
async def kick(ctx,user:discord.Member):

    if ctx.message.author.server_permissions.kick_members: 
        await client.say('==>')      
        
    try:
        await client.kick(user)
        await client.say(user.name+' was kicked✅  Good bye '+user.name+'!')

    except discord.Forbidden:
        await client.say('Permission denied.')
        return
    except discord.HTTPException:
        await client.say('kick failed.')
        return		 	

@client.command(pass_context = True)
@commands.has_permissions(manage_messages=True)  
async def clear(ctx, number):

    if ctx.message.author.server_permissions.ban_members: 
         mgs = [] #Empty list to put all the messages in the log
         number = int(number) #Converting the amount of messages to delete to an integer
    async for x in client.logs_from(ctx.message.channel, limit = number+1):
        mgs.append(x)             
        
    try:
        await client.delete_messages(mgs)          
        await client.say(str(number)+' messages deleted')

    except discord.Forbidden:
        await client.say('Permission denied.')
        return
    except discord.HTTPException:
        await client.say('clear failed.')
        return			


    await client.delete_messages(mgs)   	

@client.command(pass_context=True)
    
@commands.has_permissions(mute_members=True)      

async def mute(ctx,user:discord.Member):
    if ctx.message.author.server_permissions.mute_members: 
             
       role = discord.utils.get(ctx.message.server.roles,name='Muted')        
    try:
        await client.add_roles(ctx.message.mentions[0], role)	 		
        await client.say('Muted ✅ '+user.name+' 🔇')
          

    except discord.Forbidden:
        await client.say('Permission denied.')
        return
    except discord.HTTPException:
        await client.say('mute failed.')
        return    	



@client.command(pass_context=True)
    
@commands.has_permissions(mute_members=True)      

async def unmute(ctx,user:discord.Member):
    if ctx.message.author.server_permissions.mute_members: 
             
       role = discord.utils.get(ctx.message.server.roles,name='Muted')        
    try:
        await client.remove_roles(ctx.message.mentions[0], role)	 		
        await client.say('Unmuted ✅ '+user.name+' 🔉')
    except discord.Forbidden:
        await client.say('Permission denied.')
        return
    except discord.HTTPException:
        await client.say('mute failed.')
        return        	

    	 		


@client.command(pass_context=True)  
@commands.has_permissions(ban_members=True)      
async def ban(ctx,user:discord.Member):

    if ctx.message.author.server_permissions.ban_members: 
        await client.say('==>')      
        
    try:
        await client.ban(user)
        await client.say(user.name+' was banned ✅  Good bye '+user.name+'!')

    except discord.Forbidden:

        await client.say('Permission denied.')
        return
    except discord.HTTPException:
        await client.say('ban failed.')
        return		 



@client.command(pass_context=True)  
@commands.has_permissions(ban_members=True)     


async def unban(ctx):
    ban_list = await client.get_bans(ctx.message.server)

    # Show banned users
    await client.say("Ban list:\n{}".format("\n".join([user.name for user in ban_list])))

    # Unban last banned user
    if not ban_list:
    	
        await client.say('Ban list is empty.')
        return
    try:
        await client.unban(ctx.message.server, ban_list[-1])
        await client.say('Unbanned user: `{}`'.format(ban_list[-1].name))
    except discord.Forbidden:
        await client.say('Permission denied.')
        return
    except discord.HTTPException:
        await client.say('unban failed.')
        return		      	 		 		  
  
@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def say(ctx, *, msg = None):
    await client.delete_message(ctx.message)

    if not msg: await client.say("Please specify a message to send")
    else: await client.say(msg)
    return

client.run(os.getenv('Token'))
