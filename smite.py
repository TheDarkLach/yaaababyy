import json

import pyrez
import pyrez.api
from pyrez.api import SmiteAPI
import pyrez.enumerations
import pyrez.models
import discord
from discord.ext import bridge,commands
import os
from dotenv import load_dotenv

load_dotenv()
id = os.getenv("pal_id")
key = os.getenv("pal_key")
smite1 = pyrez.SmiteAPI(id,key)

def getplayerID(user):
    return smite1.getPlayerId(user)

class smite(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bridge.bridge_command(help="smite")
    async def smite(self, ctx, player):
        username = player
        player = smite1.getPlayer(player)
        #print(player)
        playerid = player["ActivePlayerId"]
        icon = player["Avatar_URL"]
        hours = player["HoursPlayed"]
        level = player["Level"]
        clan = player["Team_Name"]
        embed = discord.Embed(title=username, description=clan, color=0x19B9B9)
        embed.add_field(name="Level: ", value=f"{level}", inline=True)
        embed.add_field(name="Hours Played: ", value=f"{hours}", inline=True)
        embed.add_field(name="ID: ", value=f"{playerid}", inline=True)
        embed.set_thumbnail(url=icon)
        await ctx.respond(embed=embed)

    @bridge.bridge_command(help="smite")
    async def god(self,ctx,god):
        gods = smite1.getGods()
        """dict = {
                "achilles":"0",
                "agni":"1",
                "ahmuzencab":"2",
                "ahpuch":"3",
                "amaterasu":"4",
                "anhur":"5",
                "anubis":"6",
                "aokuang":"7",
                "aphrodite":"8",
                "apollo":"9"
            }

        f1 = open('smite.txt', 'r+')
        input = f1.read()
        #result = json.loads(input)
        f1.close()
        out = open('smite2.json', 'w')
        json.dump(input,out,indent=6)
        out.close()
        with open("smite2.json", "w") as outfile:
            json.dump(dict, outfile,indent=6)"""

        f = open('smite2.json',)
        input = json.load(f)
        f.close()

        num = input[god]
        #print(num)
        print(gods[int(num)])
        name = gods[int(num)]["Name"]
        Role = gods[int(num)]["Roles"]
        type = gods[int(num)]["Type"]
        #lore = gods[int(num)]["Lore"]
        abilities = gods[int(num)]["Ability1"] + ", " + gods[int(num)]["Ability2"] + ", " + gods[int(num)]["Ability3"] + ", " + gods[int(num)]["Ability4"] + ", " + gods[int(num)]["Ability5"]
        icon = gods[int(num)]["godCard_URL"]

        embed = discord.Embed(title=name, description=Role + "\n" + type, color=0x19B9B9)
        embed.add_field(name="Abilities: ", value=f"{abilities}", inline=True)
        embed.set_thumbnail(url=icon)
        await ctx.respond(embed=embed)

    """@bridge.bridge_command(help="friends")
    async def Smitefriends(self, ctx, player):
        player1 = getplayerID(player)
        player = (player1[0]["player_id"])
        await ctx.respond(smite1.getFriends(player))"""

def setup(bot):
    bot.add_cog(smite(bot))