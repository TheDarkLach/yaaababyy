import discord
from discord.ext import commands, bridge

def is_owner():
    """Check if a user is the bot owner"""
    async def predicate(ctx):
        return ctx.author.id == 414931767129276428

    return commands.check(predicate)


class owner(commands.Cog):
  def __init__(self, bot):
      self.bot = bot

  @bridge.bridge_command()
  @is_owner()
  async def test(self,ctx):
    await ctx.respond("Test")


  @bridge.bridge_command()
  @is_owner()
  async def okick(self, ctx, user: discord.Member, *, reason="No reason"):
      await user.kick(reason=reason)
      embed = discord.Embed(title="Kicked!",description="**{0}** was kicked for **'{1}'**".format(user, reason),color=0x19B9B9)
      await ctx.channel.respond(embed=embed)

  @bridge.bridge_command(help='leave server')
  @is_owner()
  async def leaveserver(self, ctx, id):
      await self.bot.get_guild(int(id)).leave()
      await ctx.respond(f"I left: {id}")

  @bridge.bridge_command()
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
          await ctx.channel.respond(embed=embed)
    
    
def setup(bot):
    bot.add_cog(owner(bot))


