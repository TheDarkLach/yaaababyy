import json
import discord
import requests
from discord.ext import commands,bridge

class pokemon(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bridge.bridge_command(help="pokemon info")
    async def pokemon(self,ctx,pk):
        url = "https://pokeapi.co/api/v2/pokemon/" + pk
        response = requests.get(url)
        response_dict = json.loads(response.text)
        pk = pk.capitalize()

        ability = ''
        for i in response_dict['abilities']:
                ability = ability + ', ' + i['ability']['name']
        ability = ability[1:]

        icon_url = response_dict['forms'][0]['url']
        response2 = requests.get(icon_url)
        response2 = json.loads(response2.text)
        icon = response2['sprites']['front_default']

        type = ''
        for i in response2['types']:
            type = type + ', ' + i['type']['name']
        type = type[1:]

        embed = discord.Embed(title=f"{pk} ", color=0x19B9B9)
        embed.add_field(name="Abilities", value=f"{ability}", inline=True)
        embed.add_field(name="Type", value=f"{type}", inline=True)
        embed.set_thumbnail(url=icon)
        embed.set_footer(text=':)')

        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(pokemon(bot))