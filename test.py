from discord.ext import commands
import discord


class matplot(commands.Cog):
  def __init__(self, bot):
      self.bot = bot



def setup(bot):
  bot.add_cog(matplot(bot))