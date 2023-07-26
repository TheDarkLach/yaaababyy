import json

import pyrez
import pyrez.api
from pyrez.api import PaladinsAPI, SmiteAPI, RealmRoyaleAPI
import pyrez.enumerations
import pyrez.models
import discord
from discord.ext import bridge,commands
import os
from dotenv import load_dotenv

load_dotenv()
id = os.getenv("pal_id")
key = os.getenv("pal_key")
paladins1 = pyrez.PaladinsAPI(id,key)

def getplayerID(user):
    return paladins1.getPlayerId(user)

class paladins(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bridge.bridge_command(help="paladins")
    async def paladins(self,ctx):
        print(paladins1.getChampions())

    @bridge.bridge_command(help="player")
    async def player(self, ctx,player):
        await ctx.defer()
        player1 = paladins1.getPlayer(player)
        #print(type(player1))
        #print(player1)
        playerid = player1["ActivePlayerId"]
        icon = player1["AvatarURL"]
        hours = player1["HoursPlayed"]
        title = player1["Title"]
        tier = player1["Tier_RankedKBM"]
        tierc = player1["Tier_RankedController"]

        if tier == 0:
            tier = "Unranked"
        if tier == 1:
            tier = "Bronze 5"
        elif tier == 2:
            tier = "Bronze 4"
        elif tier == 3:
            tier = "Bronze 3"
        elif tier == 4:
            tier = "Bronze 2"
        elif tier == 5:
            tier = "Bronze 1"
        elif tier == 6:
            tier = "Silver 5"
        elif tier == 7:
            tier = "Silver 4"
        elif tier == 8:
            tier = "Silver 3"
        elif tier == 9:
            tier = "Silver 2"
        elif tier == 10:
            tier = "Silver 1"
        elif tier == 11:
            tier = "Gold 5"
        elif tier == 12:
            tier = "Gold 4"
        elif tier == 13:
            tier = "Gold 3"
        elif tier == 14:
            tier = "Gold 2"
        elif tier == 15:
            tier = "Gold 1"
        elif tier == 16:
            tier = "Platinum 5"
        elif tier == 17:
            tier = "Platinum 4"
        elif tier == 18:
            tier = "Platinum 3"
        elif tier == 19:
            tier = "Platinum 2"
        elif tier == 20:
            tier = "Platinum 1"
        elif tier == 21:
            tier = "Diamond 5"
        elif tier == 22:
            tier = "Diamond 4"
        elif tier == 23:
            tier = "Diamond 3"
        elif tier == 24:
            tier = "Diamond 2"
        elif tier == 25:
            tier = "Diamond 1"

        if tierc == 0:
            tierc = "Unranked"
        if tierc == 1:
            tierc = "Bronze 5"
        elif tierc == 2:
            tierc = "Bronze 4"
        elif tierc == 3:
            tierc = "Bronze 3"
        elif tierc == 4:
            tierc = "Bronze 2"
        elif tierc == 5:
            tierc = "Bronze 1"
        elif tierc == 6:
            tierc = "Silver 5"
        elif tierc == 7:
            tierc = "Silver 4"
        elif tierc == 8:
            tierc = "Silver 3"
        elif tierc == 9:
            tierc = "Silver 2"
        elif tierc == 10:
            tierc = "Silver 1"
        elif tierc == 11:
            tierc = "Gold 5"
        elif tierc == 12:
            tierc = "Gold 4"
        elif tierc == 13:
            tierc = "Gold 3"
        elif tierc == 14:
            tierc = "Gold 2"
        elif tierc == 15:
            tierc = "Gold 1"
        elif tierc == 16:
            tierc = "Platinum 5"
        elif tierc == 17:
            tierc = "Platinum 4"
        elif tierc == 18:
            tierc = "Platinum 3"
        elif tierc == 19:
            tierc = "Platinum 2"
        elif tierc == 20:
            tierc = "Platinum 1"
        elif tierc == 21:
            tierc = "Diamond 5"
        elif tierc == 22:
            tierc = "Diamond 4"
        elif tierc == 23:
            tierc = "Diamond 3"
        elif tierc == 24:
            tierc = "Diamond 2"
        elif tierc == 25:
            tierc = "Diamond 1"



        embed = discord.Embed(title=f"{player} '{title}'", color=0x19B9B9)
        embed.add_field(name="Hours Played: ", value=f"{hours}", inline=True)
        embed.add_field(name="ID: ", value=f"{playerid}", inline=True)
        embed.add_field(name="PC Rank: ", value=f"{tier}", inline=False)
        embed.add_field(name="Console Rank: ", value=f"{tierc}", inline=True)
        embed.set_thumbnail(url=icon)
        await ctx.respond(embed=embed)

    @bridge.bridge_command(help="friends")
    async def friends(self, ctx, player):
        player1 = getplayerID(player)
        player = (player1[0]["player_id"])
        await ctx.respond(paladins1.getFriends(player))

    @bridge.bridge_command(help="friends")
    async def champs(self, ctx, player):
        await ctx.defer()
        ogplayer = player
        x = 0
        player1 = getplayerID(player)
        player = (player1[0]["player_id"])
        test =""
        await ctx.channel.send("Gathering data please wait !")
        for i in paladins1.getChampionRanks(player):
            test = test + (str(paladins1.getChampionRanks(player)[x]["champion"]) + ", lvl " + str(paladins1.getChampionRanks(player)[x]["Rank"]) + "\n")
            x+=1

        embed = discord.Embed(title=f"{ogplayer}'s champions",description=test, color=0x19B9B9)

        await ctx.respond(embed=embed)




def setup(bot):
    bot.add_cog(paladins(bot))