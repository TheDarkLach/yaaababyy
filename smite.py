import json

import pyrez.models
import discord
from discord.ext import bridge,commands,pages
import os
from dotenv import load_dotenv
import re
import datetime

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
        try:
            username = player
            id = getplayerID(username)
            player = smite1.getPlayer(player)
        except Exception as e:
            await ctx.respond("Player not found or private")
            return
        # print(player)

        playerid = player["ActivePlayerId"]
        icon = player["Avatar_URL"]
        hours = player["HoursPlayed"]
        level = player["Level"]
        clan = player["Team_Name"]

        gods = smite1.getGodRanks(playerid)

        one = gods[0]["god"]
        two = gods[1]["god"]
        three = gods[2]["god"]
        four = gods[3]["god"]
        five = gods[4]["god"]

        kda1 = round((int(gods[0]["Kills"]) + int(0.5 * gods[0]["Assists"])) / int(gods[0]["Deaths"]), 2)
        kda2 = round((int(gods[1]["Kills"]) + int(0.5 * gods[1]["Assists"])) / int(gods[1]["Deaths"]), 2)
        kda3 = round((int(gods[2]["Kills"]) + int(0.5 * gods[2]["Assists"])) / int(gods[2]["Deaths"]), 2)
        kda4 = round((int(gods[3]["Kills"]) + int(0.5 * gods[3]["Assists"])) / int(gods[3]["Deaths"]), 2)
        kda5 = round((int(gods[4]["Kills"]) + int(0.5 * gods[4]["Assists"])) / int(gods[4]["Deaths"]), 2)

        conquestrank = player["RankedConquest"]["Tier"]
        print(conquestrank)

        f = open('tiers.json', )
        input = json.load(f)
        f.close()

        conquestrank = input[str(conquestrank)]
        conquestwl = f'{player["RankedConquest"]["Wins"]} / {player["RankedConquest"]["Losses"]}'
        conquestmmr = round(player["RankedConquest"]["Rank_Stat"])
        conquesttp = player["RankedConquest"]["Points"]

        joustrank = player["RankedJoust"]["Tier"]

        joustrank = input[str(joustrank)]
        joustwl = f'{player["RankedJoust"]["Wins"]} / {player["RankedJoust"]["Losses"]}'
        joustmmr = round(player["RankedJoust"]["Rank_Stat"])
        jousttp = player["RankedJoust"]["Points"]

        duelrank = player["RankedDuel"]["Tier"]

        duelrank = input[str(duelrank)]
        duelwl = f'{player["RankedDuel"]["Wins"]} / {player["RankedDuel"]["Losses"]}'
        duelmmr = round(player["RankedDuel"]["Rank_Stat"])
        dueltp = player["RankedDuel"]["Points"]

        wins = player["Wins"]
        losses = player["Losses"]
        mastery = player["MasteryLevel"]
        worshipers = player["Total_Worshipers"]

        realpages = [
            pages.Page(
                embeds=[
                    discord.Embed(timestamp=datetime.datetime.now(), color=0x19B9B9).add_field(name="Level: ",
                                                                                               value=level,
                                                                                               inline=True).add_field(
                        name="Mastery", value=mastery, inline=True).add_field(name="Worshippers", value=worshipers,
                                                                              inline=True) \
                        .add_field(name="Hours Played", value=hours, inline=True).add_field(name="Wins", value=wins,
                                                                                            inline=True).add_field(
                        name="Losses", value=losses, inline=True) \
                        .add_field(name="Ranked Conquest",
                                   value=f'{conquestrank}\nW/L: {conquestwl}\nMMR: {conquestmmr}\nTP: {conquesttp}',
                                   inline=True).add_field(name="Ranked Joust",
                                                          value=f'{joustrank}\nW/L: {joustwl}\nMMR: {joustmmr}\nTP: {jousttp}',
                                                          inline=True).add_field(name="Ranked Duel",
                                                                                 value=f'{duelrank}\nW/L: {duelwl}\nMMR: {duelmmr}\nTP: {dueltp}',
                                                                                 inline=True) \
                        .set_footer(text="\u200b").set_author(name=f'{username} [{clan}]', icon_url=icon)
                ]
            ),
            pages.Page(
                # REDO THIS FOR ONE EMBED OR SOMETHIGN SO ITS DOESNT LOOK SO CLUTTERED
                embeds=[
                    discord.Embed(timestamp=datetime.datetime.now(), color=0x19B9B9).add_field(name=one, value=kda1,
                                                                                               inline=True).add_field(
                        name=two, value=kda2, inline=True) \
                        .add_field(name=three, value=kda3, inline=True).add_field(name=four, value=kda4,
                                                                                  inline=True).add_field(name=five,
                                                                                                         value=kda5,
                                                                                                         inline=True) \
                        .set_footer(text="\u200b").set_author(name=f'{username} [{clan}]', icon_url=icon)
                ]
            )
        ]

        paginator = pages.Paginator(pages=realpages)
        await paginator.respond(ctx.interaction, ephemeral=False)



        #await ctx.respond(embed=embed)

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