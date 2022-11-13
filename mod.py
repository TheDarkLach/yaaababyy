from discord.ext import commands,bridge
import discord

class mod(commands.Cog):
  def __init__(self, bot):
      self.bot = bot
    
  @bridge.bridge_command(help = 'kick')
  @commands.has_permissions(kick_members=True)
  async def kick(self, ctx, user: discord.Member, *, reason="No reason"):
      await user.kick(reason=reason)
      embed = discord.Embed(
          title="Kicked!",
          description="**{0}** was kicked for **'{1}'**".format(user, reason),
          color=0x19B9B9)
      await ctx.respond(embed=embed)
  
  
  @bridge.bridge_command(help = 'ban')
  @commands.has_permissions(ban_members=True)
  async def ban(self, ctx, user: discord.Member = None, *, reason="No reason"):
    if user == None:
      await ctx.reply("bruh ban who")
    else:
      await user.ban(reason=reason)
      embed = discord.Embed(
          title="Banned!",
          description="**{0}** was banned for **'{1}'** ".format(
              user, reason),
          color=0x19B9B9)
      await ctx.respond(embed=embed)

  @bridge.bridge_command(help = 'ban through id (idt this works)')
  @commands.has_permissions(ban_members=True)
  async def banid(self, ctx, id: int, *, reason="No reason"):
    user = await commands.fetch_user(id)
    if user == None:
      await ctx.reply("bruh ban who")
    else:
      await ctx.guild.ban(user,reason=reason)
      embed = discord.Embed(
          title="Banned!",
          description="**{0}** was banned for **'{1}'**".format(
              user, reason),
          color=0x19B9B9)
      await ctx.respond(embed=embed)
  
  
  @bridge.bridge_command(help = 'unban')
  @commands.has_permissions(ban_members=True)
  async def unban(self, ctx, id: int):
      user = await commands.fetch_user(id)
      await ctx.guild.unban(user)
      await ctx.respond("{0} has been unbanned".format(user.mention))
  
  
  @bridge.bridge_command(help = 'probably mutes a user')
  @commands.has_permissions(ban_members=True)
  async def mute(self, ctx, member: discord.Member):
      role = discord.utils.get(ctx.guild.roles, name='Muted')
      await member.add_roles(role)
      await ctx.respond("free my mans he aint do none")
  
  
  @bridge.bridge_command(help = 'times a user out')
  @commands.has_permissions(ban_members=True)
  async def timeout(self, ctx, member: discord.Member):
      role = discord.utils.get(ctx.guild.roles, name='Timeout')
      await member.add_roles(role)
      await ctx.respond("hahahaha loser")
  
  
  @bridge.bridge_command(help = 'probably unmuted a user')
  @commands.has_permissions(ban_members=True)
  async def unmute(self, ctx, member: discord.Member):
      role = discord.utils.get(ctx.guild.roles, name='Muted')
      await member.remove_roles(role)
      await ctx.respond("FREED")
  
  
  @bridge.bridge_command(help = 'free a user from timeout')
  @commands.has_permissions(ban_members=True)
  async def free(self, ctx, member: discord.Member):
      role = discord.utils.get(ctx.guild.roles, name='Timeout')
      await member.remove_roles(role)
      await ctx.respond("FREED")


def setup(bot):
    bot.add_cog(mod(bot))
