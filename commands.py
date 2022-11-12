import shutil
import discord
from discord.ext import commands,bridge
import wikipedia
import requests
from random import choice, randint


class MC(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @bridge.bridge_command(help='get an image from url')
    async def ss(self, ctx, url):
        response = requests.get(
            'https://api.apiflash.com/v1/urltoimage?access_key=64a2300d43cc4e0781553dc176b28874&url=https://' + url + '&delay=3',
            stream=True)
        with open('img.jpeg', 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response
        with open('img.jpeg', "rb") as fh:
            f = discord.File(fh, filename='img.jpeg')
        await ctx.respond(file=f)


    @bridge.bridge_command(help='Rolls a dice, can specify sides: d4,d6,d8,d10,d12,d20,d00(100)')
    async def roll(self, ctx, *args):
        diceSize = {
            "d4": 4,
            "d6": 6,
            "d8": 8,
            "d10": 10,
            "d00": 100,
            "d12": 12,
            "d20": 20,
        }
        # Default size and number of dice
        selSize = 6

        try:
            selSize = diceSize[args[0]]
            diceNum = int(args[1])
        except KeyError:
            if not str(args[0]).isdigit():
                ctx.respond("bruh")
            diceNum = int(args[0])
        except (IndexError, ValueError):
            diceNum = 1

        # Cap dice number up to 5 to prevent bot from freezing
        diceNum = 5 if diceNum > 5 else diceNum
        results = [
            str(randint(0 if selSize == 100 else 1, selSize))
            + ("%" if selSize == 100 else "")
            for i in range(diceNum)
        ]
        return await ctx.respond("You rolled {}".format(", ".join(results)))


    @bridge.bridge_command(help='flips a coin')
    async def flip(self, ctx):
        await ctx.respond(f"You got {choice(['heads', 'tails'])}!")

    @bridge.bridge_command(help='check bots ping')
    async def ping(self, ctx):
        await ctx.respond(f'Bruh: {round(self.bot.latency * 1000)} ms')


    @bridge.bridge_command(help='duck')
    async def duck(self, ctx):
        num = randint(0, 56)
        response2 = 'https://random-d.uk/api/v2/' + str(num) + '.gif'
        await ctx.respond(response2)

    #I should really redo this ngl
    #i will redo this at some point i swear (comment made like 6 months after previous)
    @bridge.bridge_command(help="random animal picture and facts")
    async def animal(self, ctx):
        url = "https://zoo-animal-api.herokuapp.com/animals/rand"
        response = requests.get(url)
        with open('animal.txt', mode='wb') as file:
            file.write(response.content)
        f1 = open('animal.txt', 'r+')
        input = f1.read()
        input = input.replace('"', "\n").replace('{', '').replace('}', '').replace(',', '').replace('latin_name',
                                                                                                    '').replace('name', '') \
            .replace('anime_type', '').replace('active_time', '').replace('length_min', '').replace('length_max',
                                                                                                    '').replace(
            'animal_type', '').replace('weight_min', '') \
            .replace('weight_max', '').replace('lifespan', '').replace('habitat', '').replace('diet', '').replace(
            'geo_range', '') \
            .replace('image_link', '')  # .replace(':','')
        f2 = open("animal.txt", "w+")
        f2.write(input)
        f1.close()
        f2.close()

        # remoec empty lines
        output = ''
        with open("animal.txt") as f:
            for line in f:
                if not line.isspace():
                    output += line

        f = open("animal.txt", "w")
        f.write(output)
        f.close()

        # delete last line cuz id line
        fd = open("animal.txt", "r")
        d = fd.read()
        fd.close()
        m = d.split("\n")
        s = "\n".join(m[:-2])
        fd = open("animal.txt", "w+")
        for i in range(len(s)):
            fd.write(s[i])
        fd.close()

        # removing every other cuz of :, cant remove that with replace cuz link breaks
        fn = open('animal.txt', 'r')

        # open other file in write mode
        fn1 = open('animal2.txt', 'w')

        # read the content of the file line by line
        cont = fn.readlines()
        type(cont)
        for i in range(0, len(cont)):
            if (i % 2 != 0):
                fn1.write(cont[i])
            else:
                pass

        # close the file
        fn1.close()

        # set all variable
        # link should be last line?
        with open('animal.txt') as f:
            for line in f:
                pass
            link = line

        with open('animal2.txt') as f:
            for i, line in enumerate(f, 1):
                if i == 1:
                    break
        name = line

        with open('animal2.txt') as f:
            for i, line in enumerate(f, 1):
                if i == 2:
                    break
        lname = line

        with open('animal2.txt') as f:
            for i, line in enumerate(f, 1):
                if i == 3:
                    break
        atype = line

        with open('animal2.txt') as f:
            for i, line in enumerate(f, 1):
                if i == 4:
                    break
        time = line

        with open('animal2.txt') as f:
            for i, line in enumerate(f, 1):
                if i == 5:
                    break
        length = line

        with open('animal2.txt') as f:
            for i, line in enumerate(f, 1):
                if i == 6:
                    break
        weight = line

        with open('animal2.txt') as f:
            for i, line in enumerate(f, 1):
                if i == 10:
                    break
        habitat = line
        with open('animal2.txt') as f:
            for i, line in enumerate(f, 1):
                if i == 11:
                    break
        diet = line
        with open('animal2.txt') as f:
            for i, line in enumerate(f, 1):
                if i == 12:
                    break
        geo = line

        embed = discord.Embed(title=f"{name}", description=f"_{lname}_", color=0x19B9B9)
        embed.add_field(name="Animal Type", value=f"{atype}", inline=True)
        embed.add_field(name="Active Time", value=f"{time}", inline=True)
        embed.add_field(name="\u200B", value="\u200B")  # newline
        embed.add_field(name="Max Length ft.", value=f"{length}", inline=True)
        embed.add_field(name="Max Weight lbs.", value=f"{weight}", inline=True)
        embed.add_field(name="\u200B", value="\u200B")  # newline
        embed.add_field(name="Habitat", value=f"{habitat}", inline=True)
        embed.add_field(name="Diet", value=f"{diet}", inline=True)
        embed.add_field(name="\u200B", value="\u200B")  # newline
        embed.add_field(name="Geological Range", value=f"{geo}", inline=True)
        embed.set_thumbnail(url=link)
        embed.set_footer(text=':)')

        await ctx.respond(embed=embed)

    #dumb
    """@commands.command(help='roasts a user')
    async def roast(self, ctx, user: discord.User):
        insult = requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=json").json()["insult"]
        await ctx.send(f"Ayo {user.mention}, " + str(insult).lower())"""


    @bridge.bridge_command(aliases=['guilds'], help='list all servers')
    async def servers(self, ctx):
        msg = '```js\n'
        msg += '{!s:19s} | {!s:>5s} | {} | {}\n'.format('ID', 'Members', 'Name', 'Owner')
        for guild in self.bot.guilds:
            msg += '{!s:19s} | {!s:>5s}| {} | {}\n'.format(guild.id, guild.member_count, guild.name, guild.owner)
        msg += '```'
        await ctx.respond(msg)


    @bridge.bridge_command(help='monke spin')
    async def spin(self, ctx):
        await ctx.respond(
            "  https://tenor.com/view/monke-spin-spinning-monkey-spinning-monke-gif-20299211"
        )


    @bridge.bridge_command(help='look something up on wikipedia')
    async def wiki(self, ctx, name):
        name = "'" + name + "'"
        result = wikipedia.summary(name)
        await ctx.respond(result)


    @bridge.bridge_command(help='enable message logging')
    async def deleteon(self, ctx):
        await ctx.respond("deleting on")
        self.bot.load_extension("delete")


    @bridge.bridge_command(help='disable message logging')
    async def deleteoff(self, ctx):
        await ctx.respond("deleting off")
        self.bot.unload_extension("delete")

    @commands.command(help="member list")
    async def members(self,ctx):
        list=""
        for member in ctx.guild.members:
            list = list + ", " + member.name
        await ctx.respond(list)
        


def setup(bot):
    bot.add_cog(MC(bot))