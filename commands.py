import discord
from discord.ext import commands
import wikipedia
import os
import sys
import asyncio
import datetime

def restart_bot(): 
  os.execv(sys.executable, ['python'] + sys.argv)


class MC(commands.Cog):
  def __init__(self, bot):
      self.bot = bot

  @commands.command()
  async def wisdom(self, ctx):
    import random
    from misc.wisdom import wisdom
    await ctx.send(random.choice(wisdom))
    
  @commands.command()
  async def help(self, ctx):
      embed = discord.Embed(
          title="AHHHH HELP!",
          description=
          "Commands include: \nkick: Kick a member \nban: Ban a member \nunban: Unban a member \nmute: Mute a member \ntimeout: puts user in timeout \nfree: releases user from timeout \ninfo: Print out info on the current server \ncurrent: Show info on current song \nspin: spinning monke \ndelete: enable deleted message logging \nnuke: creates channels and spams gifs and @everyone \nig: Lookup up instagram profiles",
          color=0x19B9B9)
      await ctx.channel.send(embed=embed)
  
  @commands.command()  
  async def spin(self, ctx):
      await ctx.channel.send(
          "  https://tenor.com/view/monke-spin-spinning-monkey-spinning-monke-gif-20299211"
      )
  
  
  @commands.command()
  async def spam(self, ctx, amount: int, *, message):
      for i in range(amount):
          await ctx.send(message)
          time.sleep(0.7)

      
  @commands.command()
  async def wiki(self, ctx, name):
    name = "'" + name + "'"
    result = wikipedia.summary(name)
    await ctx.send(result)
  
  @commands.command()
  @commands.has_permissions(administrator=True)
  async def r(self, ctx):
    message = await ctx.send("Restarting.")
    restart_bot()
    
  @commands.command()
  async def deleteon(self, ctx):
    await ctx.send("deleting on")
    self.bot.load_extension("delete")


  @commands.command()
  async def deleteoff(self, ctx):
    await ctx.send("deleting off")
    self.bot.unload_extension("delete")
    


def setup(bot):
    bot.add_cog(MC(bot))