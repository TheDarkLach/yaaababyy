from discord.ext import commands
import discord

class delete(commands.Cog):
  def __init__(self, bot):
      self.bot = bot


  @commands.Cog.listener()
  async def on_message_delete(self, message):
    if message.author == self.bot.user:
        return
    elif "YAG" in str(message.author):
        return
    embed = discord.Embed(
        title="Deleted message!",
        description="**{0}** said **'{1}'** but it was deleted!".format(
            message.author.mention, message.content),
        color=0x19B9B9)
    await message.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(delete(bot))

