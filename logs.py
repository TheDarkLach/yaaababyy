from discord.ext import commands
import discord

class logs(commands.Cog):
  def __init__(self, bot):
      self.bot = bot

  @commands.Cog.listener()
  async def on_message_delete(self, message):
    channel = self.bot.get_channel(996503232694206664)
    if message.author == self.bot.user:
        return
    elif "YAG" in str(message.author):
        return
    embed = discord.Embed(
        title="Deleted message!",
        description="**{0}** said **'{1}'** but it was deleted!".format(
            message.author.mention, message.content),
        color=0x19B9B9)
    await channel.send(embed=embed)

  @commands.Cog.listener()
  async def on_message_edit(self, before,after):
      channel = self.bot.get_channel(996503232694206664)
      if before.author == self.bot.user:
          return
      embed = discord.Embed(
        title="Message edited:",
        description="{0} \n before: **{1}** \n after: **'{2}'**".format(before.author.mention,before.content, after.content),color=0x19B9B9)
      await channel.send(embed=embed)

  @commands.Cog.listener()
  async def on_member_remove(self,member):
      channel = self.bot.get_channel(996503232694206664)
      try:
          await member.guild.fetch_ban(member)
          return
      except discord.NotFound:
          embed = discord.Embed(title="User left:",description="{0} left teh server. ".format(member.mention), color=0x19B9B9)
          await channel.send(embed=embed)

  @commands.Cog.listener()
  async def on_member_ban(self,guild,member):
      channel = self.bot.get_channel(996503232694206664)
      logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.ban).flatten()
      logs = logs[0]
      if logs.target == member:
          embed = discord.Embed(title="User banned:", description=f'{logs.target.mention} was banned by {logs.user.mention} at {logs.created_at}',color=0x19B9B9)
          await channel.send(embed=embed)

  @commands.Cog.listener()
  async def on_member_unban(self,guild,member):
      channel = self.bot.get_channel(996503232694206664)
      logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.unban).flatten()
      logs = logs[0]
      if logs.target == member:
          embed = discord.Embed(title="User unabnned:",
                                description=f'{logs.target.mention} was unbanned by {logs.user.mention} at {logs.created_at}',
                                color=0x19B9B9)
          await channel.send(embed=embed)

  @commands.Cog.listener()
  async def on_guild_update(self,before,after):
      channel = self.bot.get_channel(996503232694206664)
      embed = discord.Embed(title=f'{before} was changed to {after}',color=0x19B9B9)
      await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(logs(bot))

