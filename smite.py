import json

import pyrez
import pyrez.api
from pyrez.api import SmiteAPI
import pyrez.enumerations
import pyrez.models
import discord
from discord.ext import bridge,commands,pages
import os
from dotenv import load_dotenv
import re

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
        id = getplayerID(username)
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

        #gods = smite1.getGodRanks(playerid)


        await ctx.respond(embed=embed)

    """@bridge.bridge_command(help="smite")
    async def godp(self,ctx,god):
        gods = smite1.getGods()

        f = open('smite2.json',)
        input = json.load(f)
        f.close()

        #formatting
        god = god.lower()
        regex = re.compile('[^a-zA-Z]')
        # First parameter is the replacement, second parameter is your input string
        god = regex.sub('', god)

        num = input[god]

        #print(gods[int(num)])
        name = gods[int(num)]["Name"]
        Role = gods[int(num)]["Roles"]
        type = gods[int(num)]["Type"]
        auth = gods[int(num)]["godIcon_URL"]
        title = gods[int(num)]["Title"]
        a1 = gods[int(num)]["godAbility1_URL"]
        a2 = gods[int(num)]["godAbility2_URL"]
        a3 = gods[int(num)]["godAbility3_URL"]
        a4 = gods[int(num)]["godAbility4_URL"]
        a5 = gods[int(num)]["godAbility5_URL"]

        abilities = gods[int(num)]["Ability1"] + ", " + gods[int(num)]["Ability2"] + ", " + gods[int(num)]["Ability3"] + ", " + gods[int(num)]["Ability4"] + ", " + gods[int(num)]["Ability5"]
        icon = gods[int(num)]["godCard_URL"]

        embed = discord.Embed(title=title, color=0x19B9B9)
        embed.set_author(name=name, icon_url=auth)
        embed.add_field(name="Role: ", value=Role, inline=True)
        embed.add_field(name="Type: ", value=type, inline=True)
        #embed.add_field(name="Abilities: ", value=f"{abilities}", inline=False)
        embed.set_thumbnail(url=icon)
        await ctx.respond(embed=embed)

    @bridge.bridge_command(help="friends")
    async def Smitefriends(self, ctx, player):
        player1 = getplayerID(player)
        player = (player1[0]["player_id"])
        await ctx.respond(smite1.getFriends(player))"""

    @bridge.bridge_command(help="smite")
    async def god(self, ctx, god):
        gods = smite1.getGods()

        f = open('smite2.json', )
        input = json.load(f)
        f.close()

        # formatting
        god = god.lower()
        regex = re.compile('[^a-zA-Z]')
        # First parameter is the replacement, second parameter is your input string
        god = regex.sub('', god)

        num = input[god]

        #print(gods[int(num)])
        name = gods[int(num)]["Name"]
        Role = gods[int(num)]["Roles"]
        type = gods[int(num)]["Type"]
        auth = gods[int(num)]["godIcon_URL"]
        title = gods[int(num)]["Title"]

        a1 = gods[int(num)]["Ability1"]
        a2 = gods[int(num)]["Ability2"]
        a3 = gods[int(num)]["Ability3"]
        a4 = gods[int(num)]["Ability4"]
        a5 = gods[int(num)]["Ability5"]

        a1d = gods[int(num)]["Ability_1"]["Description"]["itemDescription"]["description"]
        a2d = gods[int(num)]["Ability_2"]["Description"]["itemDescription"]["description"]
        a3d = gods[int(num)]["Ability_3"]["Description"]["itemDescription"]["description"]
        a4d = gods[int(num)]["Ability_4"]["Description"]["itemDescription"]["description"]
        a5d = gods[int(num)]["Ability_5"]["Description"]["itemDescription"]["description"]

        a1u = gods[int(num)]["godAbility1_URL"]
        a2u = gods[int(num)]["godAbility2_URL"]
        a3u = gods[int(num)]["godAbility3_URL"]
        a4u = gods[int(num)]["godAbility4_URL"]
        a5u = gods[int(num)]["godAbility5_URL"]

        icon = gods[int(num)]["godCard_URL"]

        realpages = [
            pages.Page(
                embeds=[
                    discord.Embed(title = title,color=0x19B9B9).set_author(name=name,icon_url=auth).add_field(name="Role: ", value=Role, inline=True).add_field(name="Type: ", value=type, inline=True).set_thumbnail(url=icon)
                ]
            ),
            pages.Page(
                embeds=[
                    discord.Embed(title=a1,color=0x19B9B9).set_thumbnail(url=a1u).add_field(name="Description: ", value=a1d, inline=False)
                ]
            ),
            pages.Page(
                embeds=[
                    discord.Embed(title=a2, color=0x19B9B9).set_thumbnail(url=a2u).add_field(name="Description: ",
                                                                                             value=a2d, inline=False)
                ]
            ),
            pages.Page(
                embeds=[
                    discord.Embed(title=a3, color=0x19B9B9).set_thumbnail(url=a3u).add_field(name="Description: ",
                                                                                             value=a3d, inline=False)
                ]
            ),
            pages.Page(
                embeds=[
                    discord.Embed(title=a4, color=0x19B9B9).set_thumbnail(url=a4u).add_field(name="Description: ",
                                                                                             value=a4d, inline=False)
                ]
            ),
            pages.Page(
                embeds=[
                    discord.Embed(title=a5 + " (Passive)", color=0x19B9B9).set_thumbnail(url=a5u).add_field(name="Description: ",
                                                                                             value=a5d, inline=False)
                ]
            )
        ]

        paginator = pages.Paginator(pages=realpages)
        await paginator.respond(ctx.interaction, ephemeral=False)


    @bridge.bridge_command(help="smite")
    async def rec(self, ctx, god):
        send = ""
        f = open('smite3.json', )
        input = json.load(f)
        f.close()

        # formatting
        god = god.lower()
        regex = re.compile('[^a-zA-Z]')
        # First parameter is the replacement, second parameter is your input string
        god = regex.sub('', god)

        id = input[god]
        items = smite1.getGodRecommendedItems(id)
        print(items)
        for i in range(0, len(items)):
            send = send + items[i]["Item"] + "\n"
            #print(items[i]["Item"])
        #await ctx.respond(send)





def setup(bot):
    bot.add_cog(smite(bot))