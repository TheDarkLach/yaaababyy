import discord
from discord.ext import commands
import datetime
from instaloader import Instaloader, Profile

class social(commands.Cog):
  def __init__(self, bot):
      self.bot = bot



  
  @commands.command()
  async def president(self, ctx):
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


  @commands.command()
  async def info(self, ctx):
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
  
  
  @commands.command(aliases=["ig"])
  async def instagram(self, ctx, instaUsername):
      from os import environ
      environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
      bot = Instaloader()
      profile = Profile.from_username(bot.context, str(instaUsername))
      embed = discord.Embed(title=f"Instagram", color=0x11019e)
      embed.add_field(name="Username",
                      value=f"`@{profile.username}`",
                      inline=True)
      embed.add_field(name="Followers",
                      value=f"{profile.followers}",
                      inline=True)
      embed.add_field(name="Follows", value=f"{profile.followees}", inline=True)
      embed.add_field(name="Bio", value=f"{profile.biography}", inline=True)
      await ctx.send(embed=embed)
  
  
  
  @commands.command(aliases=["listening"])
  async def current(self, ctx, user: discord.Member = None):
      if user == None:
          user = ctx.author
          pass
      if user.activities:
          for activity in user.activities:
              if isinstance(activity, discord.Spotify):
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
          commands.send("Bruh your activity empty")

def setup(bot):
    bot.add_cog(social(bot))