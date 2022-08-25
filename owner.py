import discord
from discord.ext import commands

def is_owner():
    """Check if a user is the bot owner"""
    async def predicate(ctx):
        return ctx.author.id == 414931767129276428

    return commands.check(predicate)


class owner(commands.Cog):
  def __init__(self, bot):
      self.bot = bot

  @commands.command()
  @is_owner()
  async def test(self,ctx):
    await ctx.send("Test")


  @commands.command()
  @is_owner()
  async def okick(self, ctx, user: discord.Member, *, reason="No reason"):
      await user.kick(reason=reason)
      embed = discord.Embed(title="Kicked!",description="**{0}** was kicked for **'{1}'**".format(user, reason),color=0x19B9B9)
      await ctx.channel.send(embed=embed)


  @commands.command()
  @is_owner()
  async def oban(self, ctx, user: discord.Member = None, *, reason="No reason"):
      if user == None:
          await ctx.reply("bruh ban who")
      else:
          await user.ban(reason=reason)
          embed = discord.Embed(
              title="Banned!",
              description="**{0}** was banned for **'{1}'**".format(
                  user, reason),
              color=0x19B9B9)
          await ctx.channel.send(embed=embed)
    
    
async def setup(bot):
    await bot.add_cog(owner(bot))


