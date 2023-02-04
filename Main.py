
import pyblox
import discord
import os
from discord.ext import commands
import requests
import sys
import json
import asyncio
import pyblox3
from pyblox3 import Users
from dotenv import load_dotenv
import re
import math
from googlesearch import search
import random

load_dotenv()

client = commands.Bot(command_prefix=commands.when_mentioned_or(
    '!'), intents=discord.Intents.all())
api_key = "a03b32c2-da8a-43c0-8605-58b8ebe64d09"
blacklisted_users = []

importpeopleids = [827494693251842069, 747737515963711548]
ownerid = [827494693251842069]


def BotCreator(ctx):
   return ctx.author.id in ownerid


def botowners(ctx):
    return ctx.author.id in importpeopleids


apikey = "6d0ba74b24a048e4887701b4df266643"
token = "1ad3ece751ee2537d1285400a6148280e30cac03089f8486f107127310e849c3"
idlist = "63da5eac649a7184845eec60"
webhook = "https://discord.com/api/webhooks/1070321788392849459/dHjJvJpxwSV1PtdZXd4YbEI5KluNWusDrONdRLJNIjZ-jmH9R7rDnGy05eUbZbmhqImQ"


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game(name=" With Cleo"))

client.remove_command('help')
# Commands!


@client.command()
async def ping(ctx):
    await ctx.send(f"**Pong! :ping_pong: {round(client.latency * 1000)} ms**")


@client.command()
@commands.has_role(970381430062456952)
async def endssu(ctx):
    ssuChannel = client.get_channel(967478783764475924)
    await ssuChannel.send('The SSU Has Sadly ended!')
    await ctx.message.delete()


@client.command()
@commands.has_role(760137391058059264)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    log_channel = client.get_channel(1068571594454220870)
    embed = discord.Embed(title="Mayflower Administration", color=0x71368a)
    embed.set_author(name=ctx.author, icon_url=ctx.author.display_avatar)
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/1064585576554176592/1070035431284027453/3RrncGxL_400x400.png")
    embed.add_field(name="Banned User", value=member, inline=False)
    embed.add_field(name="Ban Reason", value=reason, inline=True)
    embed.set_footer(text="Created in discord.py by alxz#9676")
    await log_channel.send(embed=embed)
    await ctx.send(embed=embed)


@client.command(name='8ball')
async def eight_ball(ctx, *, question: str):
    responses = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes - definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful.",
        "Even alxz said no"
    ]
    await ctx.send(f'**Question:** {question}\n**Answer:** {random.choice(responses)}')
    await ctx.message.delete()


@client.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount: int):
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f'Deleted {amount} messages.', delete_after=5.0)


@client.command()
@commands.has_role(760137391058059264)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    log_channel = client.get_channel(1068571594454220870)
    embed = discord.Embed(title="Mayflower Administration", color=0x71368a)
    embed.set_author(name=ctx.author, icon_url=ctx.author.display_avatar)
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/1064585576554176592/1070035431284027453/3RrncGxL_400x400.png")
    embed.add_field(name="Kicked User", value=member, inline=False)
    embed.add_field(name="Kick Reason", value=reason, inline=True)
    embed.set_footer(text="Created in discord.py by alxz#9676")
    await log_channel.send(embed=embed)
    await ctx.send(embed=embed)
    await ctx.message.delete()


@client.command(name='unban')
@commands.has_role(760137391058059264)
async def unban(ctx, user_id: int):
    guild = ctx.guild
    try:
        await guild.unban(discord.Object(id=user_id), reason='Unban command issued by admin.')
        await ctx.send(f'Successfully unbanned user with ID {user_id} in server {guild.name}.')
    except discord.Forbidden:
        await ctx.send(f'Unable to unban user with ID {user_id} in server {guild.name} due to lack of permissions.')
    except discord.HTTPException as error:
        await ctx.send(f'Unable to unban user with ID {user_id} in server {guild.name}. Error: {error}')


@client.command()
@commands.has_role(760137391058059264)
async def uban(ctx, member: discord.Member, *, reason=None):
    for guild in client.guilds:
        try:
            await guild.ban(member, reason=reason)
        except discord.Forbidden:
            continue
        log_channel = client.get_channel(1068571594454220870)
        embed = discord.Embed(title="Mayflower Administration", color=0x71368a)
        embed.set_author(name=ctx.author, icon_url=ctx.author.display_avatar)
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/1064585576554176592/1070035431284027453/3RrncGxL_400x400.png")
        embed.add_field(name="Banned User", value=member, inline=False)
        embed.add_field(name="Ban Reason", value=reason, inline=True)
        embed.add_field(name="Discords", value=guild.name, inline=True)
        embed.set_footer(text="Created in discord.py by alxz#9676")
        await log_channel.send(embed=embed)
        await ctx.send(embed=embed)
        await ctx.message.delete()


@client.command()
@commands.has_role(760137391058059264)
async def discserv(ctx):
   for guild in client.guilds:
        embed = discord.Embed(title="Mayflower Administration", color=0x71368a)
        embed.set_author(name=ctx.author, icon_url=ctx.author.display_avatar)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1064585576554176592/1070035431284027453/3RrncGxL_400x400.png")
        embed.add_field(name="Discords", value=guild.name, inline=True)
        await ctx.send(embed=embed)

@client.command()
@commands.has_role(970381430062456952)
async def ssu(ctx):
    ssuChannel = client.get_channel(967478783764475924)
    await ssuChannel.send(':desktop: Server Start Up!\n\n @everyone https://www.roblox.com/games/9898641609/New-Haven-County')
    await ctx.message.delete()


@client.command(name='unuban')
@commands.has_role(760137391058059264)
async def unban_user(ctx, user_id: int):
    for guild in client.guilds:
        try:
            await guild.unban(discord.Object(id=user_id), reason='Unban command issued by admin.')
            await ctx.send(f'Successfully unbanned user with ID {user_id} in server {guild.name}.')
        except discord.Forbidden:
            await ctx.send(f'Unable to unban user with ID {user_id} in server {guild.name} due to lack of permissions.')
        except discord.HTTPException as error:
            await ctx.send(f'Unable to unban user with ID {user_id} in server {guild.name}. Error: {error}')


@client.command(name='votessu', cooldown_per_user=3600, cooldown_after_parsing=3600)
async def start_server_up(ctx):
    ssu_channel = client.get_channel(967478783764475924)
    vote_message = await ssu_channel.send(':thinking: Should we start a server up? React with :thumbsup: to vote. @here')
    await vote_message.add_reaction('👍')
    await ctx.message.delete()

    def check(reaction, user):
        return user != client.user and str(reaction.emoji) == '👍' and reaction.count >= 6

    try:
        reaction, user = await client.wait_for('reaction_add', timeout=600, check=check)
    except TimeoutError:
        await vote_message.edit(content=':x: The vote has timed out. No server start up today.')
    else:
        await ssu_channel.send(':desktop: Server Start Up!\n\n @everyone https://www.roblox.com/games/9898641609/New-Haven-County')


@client.command()
@commands.has_role(968168224279633940)
async def dannounce(ctx, *, Message: str):
    announce = client.get_channel(970427539266891837)
    embed = discord.Embed(title="Department Announcement", color=0x71368a)
    embed.set_author(name=ctx.author, icon_url=ctx.author.display_avatar)
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/1064585576554176592/1070035431284027453/3RrncGxL_400x400.png")
    embed.add_field(name="Announcement", value=Message, inline=False)
    await announce.send(embed=embed)
    await announce.send('@here')
    await ctx.message.delete()


@client.command()
@commands.has_role(1070303741405843518)
async def announce(ctx, *, Message: str):
    announce = client.get_channel(970427539266891837)
    embed = discord.Embed(title="Announcement", color=0x71368a)
    embed.set_author(name=ctx.author, icon_url=ctx.author.display_avatar)
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/1064585576554176592/1070035431284027453/3RrncGxL_400x400.png")
    embed.add_field(name="Announcement", value=Message, inline=False)
    await announce.send(embed=embed)
    await announce.send('@here')
    await ctx.message.delete()


@client.command()
@commands.has_role(989177741922418738)
async def changelog(ctx, *, Message: str):
    announce = client.get_channel(760133975283859506)
    embed = discord.Embed(title="ChangeLog", color=0x71368a)
    embed.set_author(name=ctx.author, icon_url=ctx.author.display_avatar)
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/1064585576554176592/1070035431284027453/3RrncGxL_400x400.png")
    embed.add_field(name="Changes", value=Message, inline=False)
    await announce.send(embed=embed)
    await announce.send('@here')
    await ctx.message.delete()


@client.command()
async def suggest(ctx, *, suggestion: str):
    suggestchannel = client.get_channel(967479443885027329)
    suggestion_embed = discord.Embed(
        title="New Suggestion", description=suggestion, color=0x71368a)
    suggestion_embed.set_author(
        name=ctx.author, icon_url=ctx.author.display_avatar)
    suggestion_message = await suggestchannel.send(embed=suggestion_embed)
    await suggestion_message.add_reaction("✅")
    await suggestion_message.add_reaction("❌")
    await ctx.message.delete()


@client.command()
async def whois(ctx, member: discord.Member):
    embed = discord.Embed(
        title=f"{member.name}#{member.discriminator}", color=0x71368a)
    embed.set_thumbnail(url=member.display_avatar)
    embed.add_field(name="Discord name",
                    value=member.display_name, inline=True)
    embed.add_field(name="Joined Discord", value=member.joined_at.strftime(
        "%b %d, %Y %H:%M"), inline=True)
    embed.add_field(
        name="Nitro", value="Yes" if member.premium_since else "No", inline=True)
    await ctx.send(embed=embed)
    await ctx.message.delete()


@client.command()
async def say(ctx, *, message: str):
    await ctx.message.delete()
    await ctx.send(message)


@client.command(name='check')
@commands.has_role(760138708438876213)
async def find_guild(ctx, discord_id: int):
    api_key = "7ba9068f-d56e-4960-a318-fe7cf1ae0e93"
    headers = {
        "api-key": f"{api_key}",
        "Content-Type": "application/json"
    }
    url = f"https://v3.blox.link/developer/discord/{discord_id}?guildId=760132984237064233"

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        data2 = response.text
        guild_id = data.get("success")
        main = data.get("user")
        robloxID = main.get("robloxId")
        PrimaryID = main.get("primaryAccount")
        print(data2)
        await ctx.send(f"**Account Info: **\nVerified: **{guild_id}**\nRobloxID: **{robloxID}**\nPrimary Account: **{PrimaryID}**")
    else:
        await ctx.send(f"Error fetching data. Response code: {response.status_code}")


@client.command(name='checkid')
async def get_username(ctx, roblox_id: int):
    url = f"https://api.roblox.com/users/{roblox_id}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        username = data.get("Username")
        await ctx.send(f"Username: **{username}**")
    else:
        await ctx.send(f"Error fetching data. Response code: {response.status_code}")


@client.command(name='checkserv')
async def servers(ctx, server_id: str = None):
    response = requests.get(
        "https://games.roblox.com/v1/games/9898641609/servers/Public?sortOrder=Asc&limit=100")
    data = response.json()
    servers = data.get("data")

    if not servers:
        await ctx.send("Sorry 😣! There are currently no running servers!")
        return

    if server_id:
        found_server = None
        for server in servers:
            if server["id"] == server_id:
                found_server = server
                break

        if not found_server:
            await ctx.send("Sorry :persevere:! This server does not exist!")
        else:
            await ctx.send(f"Server Link: https://www.roblox.com/games/9898641609/New-Haven-County?jobId={server_id}")
    else:
        embed = discord.Embed(title="Servers")
        servers_count = 0
        for server in servers:
            servers_count += 1
            embed.add_field(
                name=f"Server {server['playing']}/{server['maxPlayers']} {server['id']}",
                value=f"[Server Link](https://www.roblox.com/games/9898641609/New-Haven-County?jobId={server['id']})",
                inline=False
            )
        embed.description = f"There are currently {servers_count} servers."
        await ctx.send(embed=embed)

@client.command(name='rank')
@commands.has_role(760138708438876213)
async def rank(ctx, *, user: str = None):
    group_id = 6987168
    cookie = '_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_EA04485563263B292A56E6D92D247162BC6F6B8E278F65A95AFCAC5E117D91791BE8EE9D671D46E1A6AB2CE37DCB558E1DBE33171E222F50D9D7D99B2EF24435B3DD3AFCD8D4162D6207126DAF476DF0A706B93F258F51F0E9B7DB7231C2AEE6043D36EBEC0BAEBA6103D83E2A8E1C0CA005235FA2BEC81698CB9A4B88A86C020162B8D879A75B95E694C4D761129E132B6B2E57A64FD6D9EB203B001E9DCFC90833A2D7AC3F2AC1B0652996277681B8F5067B3C619E49FF1EABBB87B1B71F096B67CA58082D590108BB49BF0B3F1CBC79001EFD51AC5345A6819A6CB1C27314B94E50F547F8343488AF75A5D29BD9E37B59276A13C8891149BB8237F491CF25EE96EC0FF73887E0C61303F7608C40B42FB51E50FE2377CB2AEB110D14D48EBD4117E5BB956AD807B6DB5E5057A7FD46FECC7D834D03781FEDCEFBDBF9BFDA494FCCAE21BC0EEE9CD10596097A4D715D1CDA8D260871C62363E04250916DF7D534563E8EB0D61478556C203523D662C90ACEC27612B40FA2966AA43CF34CA860792275F1'
    if not user:
        await ctx.send('Please enter the name or ID of the user to rank.')
        return

    # Connect to the Roblox group
    group = pyblox.Group(group_id, cookie)

    # Get the rank of the user in the group
    try:
        member = group.get_member(user)
        current_rank = group.get_rank(member.id)
        new_rank = current_rank + 1
        group.set_rank(member.id, new_rank)
        await ctx.send(f'{user} has been promoted to rank {new_rank} in the group.')
    except:
        await ctx.send(f'{user} is not a member of the group.')


@client.command(name='help', brief='Shows information about various commands.')
async def help(ctx):
    embed = discord.Embed(
        title='Help', description='List of available commands:', color=0x71368a)
    embed.add_field(
        name='ban', value='Bans a user from the server.', inline=False)
    embed.add_field(
        name='gban', value='Bans a user from playing games in the server.', inline=False)
    embed.add_field(
        name='unban', value='Unbans a user from the server.', inline=False)
    embed.add_field(
        name='Ungban', value='Removes the game ban of a user.', inline=False)
    embed.add_field(
        name='kick', value='Kicks a user from the server.', inline=False)
    embed.add_field(
        name='purge', value='Deletes a specified number of messages.', inline=False)
    embed.add_field(
        name='8ball', value='Asks the magic 8-ball a yes/no question.', inline=False)
    embed.add_field(
        name='ping', value='Checks the bot\'s latency.', inline=False)
    embed.add_field(
        name='suggest', value='Sends a suggestion to the server.', inline=False)
    embed.add_field(
        name='whois', value='Displays information about a user.', inline=False)
    embed.add_field(
        name='dannounce', value='Sends an announcement in department announcements', inline=False)
    embed.add_field(
        name='announce', value='Sends an announcement in general announcements.', inline=False)
    embed.add_field(name='ssu', value='Starts an ssu.', inline=False)
    embed.add_field(
        name='changelog', value='Displays the latest changes in the server.', inline=False)
    embed.add_field(
        name='uban', value='Ultra banning bans people from all discords the bot is available in', inline=False)
    embed.add_field(
        name='say', value='Makes the bot say a message.', inline=False)
    embed.add_field(name='shutdown', value='Shuts down the bot.', inline=False)
    embed.add_field(
        name='endssu', value='Displays the end of an SSU', inline=False)
    embed.add_field(name='unuban', value='lifts an Ultra Ban', inline=False)
    embed.add_field(
        name='votessu', value='starts a vote for an SSU', inline=False)
    embed.add_field(
        name='check', value='checks if someone is verified', inline=False)
    embed.add_field(
        name='checkid', value='Checks someones UserID and returns their Username', inline=False)
    embed.add_field(
        name='checkserv', value='Checks the game for any running servers and how many people are in it', inline=False)
    embed.set_footer(
        text='Note: The names of the commands are case-sensitive.')
    embed2 = discord.Embed(
        title='Help', description='List of available commands:', color=0x71368a)
    embed2.add_field(name='quarantine',
                     value='temporarily removes someones roles.', inline=False)
    embed2.set_footer(
        text='Note: The names of the commands are case-sensitive.')
    await ctx.send(embed=embed)
    await ctx.send(embed=embed2)


@client.command()
async def shutdown(ctx):
    id = str(ctx.author.id)
    if id == '827494693251842069':
        await ctx.send('Shutting down the bot!')
        await client.close()
    else:
        await ctx.send("You dont have sufficient permissions to perform this action!")


@client.command(name='q')
@commands.check(botowners)
async def quarantine(ctx, member: discord.Member):
    if not member.roles:
        await ctx.send("This user has no roles to quarantine.")
        return
    roles = member.roles.copy()
    await member.edit(roles=[])
    await ctx.send(f"{member.mention} has been quarantined.")

    def check(message):
        return message.author == ctx.author and message.content == f"unquarantine {member.id}"
    try:
        msg = await client.wait_for("message", check=check, timeout=60.0)
    except asyncio.TimeoutError:
        pass
    else:
        await member.edit(roles=roles)
        await ctx.send(f"{member.mention} has been unquarantined.")

# BOT - ROBLOX BAN


def sendlog(msg):
    json = {
        "content": msg,
        "embeds": None,
        "attachments": []
    }
    requests.post(webhook, json=json)


def getuser(userid):
  r = requests.get(f'https://users.roblox.com/v1/users/{userid}')
  response = r.json()
  plrusername = response["name"]
  print(plrusername)


@client.command()
@commands.check(botowners)
async def gban(ctx, user,*, reason=None):

    if reason == None:
      try:
        plrdata1 = Users.User(user)
        plrid1 = str(plrdata1.Id)
        plrusernamefunc = plrid1
        await ctx.send(f'{ctx.author} reason for banning {plrusernamefunc} (30 seconds to reply)')
      except:
        await ctx.send(f'{ctx.author} reason for banning {user} (30 seconds to reply)')

    def check(m):
        return m.channel == ctx.channel
    try:
      msg = await client.wait_for('message', timeout=30, check=check)
    except:
      return await ctx.send('You have not replied with a reason for this ban. Aborting Ban...')
    if msg.content == 'cancel':
      return await ctx.send('Undoing...')
    reason=msg.content


    if user in ['whitelisted users']:
      return await ctx.send('You cannot ban this user.')

    if user.isnumeric():
      opuser = getuser(user)
      print('User id')
    else:
      plrdata = Users.User(user)
      plrid = str(plrdata.Id)
      user = plrid


    url = "https://api.trello.com/1/cards"

    headers = {
      "Accept": "application/json"
    }

    query = {
      'idList': idlist,
      'key': apikey,
      'token': token
    }

    responsee = requests.request(
      "POST",
      url,
      headers=headers,
      params=query
    )

    a = responsee.json()
    this = a['shortLink']


    url = f"https://api.trello.com/1/cards/{this}"
    query = {'key': apikey, 'token': token}
    payload = {'name': user}
    response = requests.request("PUT", url, params=query, data=payload)

    try:
      plrdata1 = Users.User(user)
      plrid1 = str(plrdata1.Id)
      plrusernamefunc = plrid1
      await ctx.send(f'```\nBANNED ({ctx.author}): {plrusernamefunc} | reason: {reason}```')
    except:
      await ctx.send(f'```\nBANNED ({ctx.author}): {user} | reason: {reason}```')

    sendlog(f'Banned id: `{user}` with key `{this}` , {reason}')
      
    await ctx.message.add_reaction('\N{WHITE HEAVY CHECK MARK}')

@client.command()
@commands.check(botowners)
async def ungban(ctx, trelloident,*, reason=None):
  if reason==None:
    if trelloident.isnumeric():
      return await ctx.send(f'Please enter the users Ban Key not their ID/User.')
    else:
      await ctx.send(f'{ctx.author} reason for unbanning {trelloident} (30 seconds to respond)')

  def check(m):
      return m.channel == ctx.channel
  try:
    msg = await client.wait_for('message', timeout=30, check=check)
  except:
    return await ctx.send('You have not replied with a reason for this ban. Aborting Ban...')
  if msg.content == 'cancel':
    return await ctx.send('Undoing...')
  reason=msg.content

  url = f"https://api.trello.com/1/cards/{trelloident}"

  query = {
    'key': apikey,
    'token': token
  }

  response = requests.request(
    "DELETE",
    url,
    params=query
  )
  await ctx.send(f'```\nUN-BANNED ({ctx.author}): {trelloident} | reason: {reason}```')
  await ctx.message.add_reaction('\N{WHITE HEAVY CHECK MARK}')

@client.command(aliases=['e', 'evaluate'])
@commands.check(BotCreator)
async def eval(ctx, *, code):
    """Evaluates customized code"""
    language_specifiers = ["python", "py", "javascript", "js", "html", "css", "php", "md", "markdown", "go", "golang", "c", "c++", "cpp", "c#", "cs", "csharp", "java", "ruby", "rb", "coffee-script", "coffeescript", "coffee", "bash", "shell", "sh", "json", "http", "pascal", "perl", "rust", "sql", "swift", "vim", "xml", "yaml"]
    loops = 0
    while code.startswith("`"):
        code = "".join(list(code)[1:])
        loops += 1
        if loops == 3:
            loops = 0
            break
    for language_specifier in language_specifiers:
        if code.startswith(language_specifier):
            code = code.lstrip(language_specifier)
    try:
        while code.endswith("`"):
            code = "".join(list(code)[0:-1])
            loops += 1
            if loops == 3:
                break
        code = "\n".join(f"    {i}" for i in code.splitlines())
        code = f"async def eval_expr():\n{code}"
        def send(text):
            client.loop.create_task(ctx.send(text))
        env = {
            "bot": client,
            "client": client,
            "ctx": ctx,
            "print": send,
            "_author": ctx.author,
            "_message": ctx.message,
            "_channel": ctx.channel,
            "_guild": ctx.guild,
            "_me": ctx.me
        }
        env.update(globals())
        exec(code, env)
        eval_expr = env["eval_expr"]
        result = await eval_expr()
        await ctx.message.add_reaction("\N{WHITE HEAVY CHECK MARK}")
        if result:
            await ctx.send(result)
    except Exception as learntofuckingcode:
        await ctx.message.add_reaction("\N{WARNING SIGN}")
        await ctx.send(f'**Error**```py\n{learntofuckingcode}```')

@client.command(name='gtban')
@commands.has_role(1067618350861127700)
async def gtban(ctx, user, time: int):
    plrdata1 = Users.User(user)
    plrid1 = str(plrdata1.Id)
    plrusernamefunc = plrid1

    def check(m):
        return m.channel == ctx.channel
    try:
      msg = await client.wait_for('message', timeout=30, check=check)
    except:
      return await ctx.send('You have not replied with a reason for this tban. Aborting tBan...')
    if msg.content == 'cancel':
      return await ctx.send('Undoing...')
    reason=msg.content


    if user in ['whitelisted users']:
      return await ctx.send('You cannot tban this user.')

    if user.isnumeric():
      opuser = getuser(user)
      print('User id')
    else:
      plrdata = Users.User(user)
      plrid = str(plrdata.Id)
      user = plrid


    url = "https://api.trello.com/1/cards"

    headers = {
      "Accept": "application/json"
    }

    query = {
      'idList': idlist,
      'key': apikey,
      'token': token
    }

    responsee = requests.request(
      "POST",
      url,
      headers=headers,
      params=query
    )

    a = responsee.json()
    this = a['shortLink']


    url = f"https://api.trello.com/1/cards/{this}"
    query = {'key': apikey, 'token': token}
    payload = {'name': user}
    response = requests.request("PUT", url, params=query, data=payload)

    try:
      plrdata1 = Users.User(user)
      plrid1 = str(plrdata1.Id)
      plrusernamefunc = plrid1
      await ctx.send(f'```\nTBANNED ({ctx.author}): {plrusernamefunc}```')
    except:
      await ctx.send(f'```\nTBANNED ({ctx.author}): {user}```')

    sendlog(f'TBanned id: `{user}` with key `{this}` , {reason}')
      
    await ctx.message.add_reaction('\N{WHITE HEAVY CHECK MARK}')

    await asyncio.sleep(time * 60)

    url2 = f"https://api.trello.com/1/cards/{this}"

    query = {
        'key': apikey,
        'token': token
    }

    response2 = requests.request(
        "DELETE",
        url2,
        params=query
    )
    await ctx.send(f'```\nUN-TBANNED ({ctx.author}): {this}```')


    







client.run("ODg4NzY5Nzg4MDU3MzgyOTEy.GsWMlW.EbtVN0e03MNGjBRBWet9yWp2erXDqBBD0nU4SQ")
