import discord
from discord.ext import commands
import wikipedia
import os
import sys
import requests
from random import choice, randint, random, shuffle

def restart_bot(): 
  os.execv(sys.executable, ['python'] + sys.argv)


class MC(commands.Cog):
  def __init__(self, bot):
      self.bot = bot


  @commands.command(help = 'Rolls a dice, can specify sides: d4,d6,d8,d10,d12,d20,d00(100)')
  async def roll(self, ctx, *args):
    diceSize = {
        "d4": 4,
        "d6": 6,
        "d8": 8,
        "d10": 10,
        "d00": 100,
        "d12": 12,
        "d20": 20,
    }
    # Default size and number of dice
    selSize = 6

    try:
        selSize = diceSize[args[0]]
        diceNum = int(args[1])
    except KeyError:
        if not str(args[0]).isdigit():
            ctx.send("bruh")
        diceNum = int(args[0])
    except (IndexError, ValueError):
        diceNum = 1

    # Cap dice number up to 5 to prevent bot from freezing
    diceNum = 5 if diceNum > 5 else diceNum
    results = [
        str(randint(0 if selSize == 100 else 1, selSize))
        + ("%" if selSize == 100 else "")
        for i in range(diceNum)
    ]
    return await ctx.send("You rolled {}".format(", ".join(results)))

  @commands.command(help = 'flips a coin')
  async def flip(self, ctx):
      await ctx.reply(f"You got {choice(['heads', 'tails'])}!")

  @commands.command(help = 'check bots ping') 
  async def ping(self, ctx):
    await ctx.send(f'Bruh: {round(self.bot.latency * 1000)} ms')


  @commands.command(help = 'roasts a user')
  async def roast(self, ctx, user: discord.User):
      insult = requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=json").json()["insult"]
      await ctx.send(f"Ayo {user.mention}, " + str(insult).lower())
    


  @commands.command(aliases=['guilds'], help = 'list all servers')
  async def servers(self, ctx):
    msg = '```js\n'
    msg += '{!s:19s} | {!s:>5s} | {} | {}\n'.format('ID', 'Members', 'Name', 'Owner')
    for guild in self.bot.guilds:
        msg += '{!s:19s} | {!s:>5s}| {} | {}\n'.format(guild.id, guild.member_count, guild.name, guild.owner)
    msg += '```'
    await ctx.send(msg)

  
  @commands.command(help = 'monke spin')  
  async def spin(self, ctx):
      await ctx.channel.send(
          "  https://tenor.com/view/monke-spin-spinning-monkey-spinning-monke-gif-20299211"
      )
  

      
  @commands.command(help = 'look something up on wikipedia')
  async def wiki(self, ctx, name):
    name = "'" + name + "'"
    result = wikipedia.summary(name)
    await ctx.send(result)
  
    
  @commands.command(help = 'enable message logging')
  async def deleteon(self, ctx):
    await ctx.send("deleting on")
    self.bot.load_extension("delete")


  @commands.command(help = 'disable message logging')
  async def deleteoff(self, ctx):
    await ctx.send("deleting off")
    self.bot.unload_extension("delete")

  

def setup(bot):
    bot.add_cog(MC(bot))