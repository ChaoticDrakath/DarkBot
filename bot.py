import discord
import asyncio
from games import TicTacToe, XTacToe
from sys import exit

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.lower().startswith('hi'):
        await msg_hi(message)

    elif message.content.lower().startswith('!challenge'):
        await msg_challenge(message)

    elif message.content.lower().startswith('!move'):
        await msg_move(message)

    elif message.content.lower().startswith('!redraw'):
        await msg_redraw(message)

    elif message.content.lower().startswith('!quit'):
        await msg_quit(message)

    elif message.content.lower().startswith('!games'):
        await msg_games(message)

    elif message.content.lower().startswith('!help'):
        await msg_help(message)

    elif message.content.lower().startswith('!kill'):
        await client.send_message(message.channel, 'rip')
        exit()

        
async def msg_hi(message):
    await client.send_message(message.channel, ':piou:')

async def msg_challenge(message):
    p1 = message.author
    if len(message.mentions) != 1:
        await client.send_message(message.channel, 'Please mention exactly one player.')
        return
    p2 = message.mentions[0]

    for g in games:
        if p1 in g.players or p2 in g.players:
            await client.send_message(message.channel, 'One player is already in a game.')
            return

    if p2 == p1:
        await client.send_message(message.channel, 'Can\'t play against yourself.')
        return

    cnt = message.content.lower()
    game = None
    if 'tictactoe' in cnt:
        game = TicTacToe([p1, p2])
    elif 'xtactoe' in cnt:
        game = XTacToe([p1, p2])
    else:
        await client.send_message(message.channel, 'Please enter a proper game name (see !help).')
        return
    await game.start(client, message)
    
    print('Created game ' + str(game))
    games.append(game)

async def msg_move(message):
    for i in range(len(games)):
        g = games[i]
        if message.author == g.get_whose_turn():
            await g.make_move(client, message)

            if g.is_over():
                del games[i]
            break

async def msg_redraw(message):
    for g in games:
        if message.author in g.players:
            print('Redrawing ' + str(g))
            await g.draw(client, message)
            break

async def msg_quit(message):
    for i in range(len(games)):
        if message.author in games[i].players:
            print('Killing game ' + str(games[i]))
            await client.send_message(message.channel, 'Destroyed game: ' + str(games[i]))
            del games[i]
            return
    await client.send_message(message.channel, 'You are not in any game.')
    
async def msg_games(message):
    if len(games) == 0:
        await client.send_message(message.channel, 'No games currently on.')
        return
    
    t = 'Printing all games out of ' + str(len(games)) + ':\n'
    for g in games:
        t += '- ' + str(g)
    await client.send_message(message.channel, t)

async def msg_help(message):
    t = '```\n'
    
    t += 'hi - hi\n'
    t += 'challenge @mention game_name - challenge @mention for a game\n'
    t += 'move X - make move X\n'
    t += 'redraw - redraw the board\n'
    t += 'quit - leave the game you\'re in\n'
    t += 'games - list all active games\n'

    t += '\n\n'
    t += 'Games available: tictactoe, xtactoe'

    t += '```'
    await client.send_message(message.channel, t)

        
games = []
client.run(get_Token())
