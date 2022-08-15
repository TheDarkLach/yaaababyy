from discord.ext import commands
import discord

"""
def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)


async def calc(bruh):
    global n, m, x
    n = bruh.content.lower()
    m = n
    if '+' in n:
        n = n.split('+')
        x = 0
        for i in range(len(n)):
            x = x + float(n[i])
        await bruh.channel.send(m + " = " + str(x))
    elif '-' in n:
        n = n.split('-')
        x = float(n[0])
        for i in range(len(n) - 1):
            x = x - float(n[i + 1])
        await bruh.channel.send(m + " = " + str(x))
    elif '*' in n:
        n = n.split('*')
        x = 1
        for i in range(len(n)):
            x = x * float(n[i])
        await bruh.channel.send(m + " = " + str(x))
    elif '!' in n:
        n = n.split('!')
        x = 1
        n = int(n[0])
        for i in range(n):
            x = x * (n - i)
        await bruh.channel.send(m + " = " + str(x))
    elif '/' in n:
        n = n.split('/')
        x = int(n[0]) / int(n[1])
        await bruh.channel.send(m + " = " + str(x))
    elif '^' in n:
        n = n.split('^')
        x = int(n[0]) ** int(n[1])
        await bruh.channel.send(m + " = " + str(x))"""


class events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        role = discord.utils.get(member.guild.roles, name="human")
        await member.add_roles(role)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            text = "Sorry {}, you do not have permissions to do that lol".format(
                ctx.message.author.mention)
            await ctx.channel.send(text)
        if isinstance(error, commands.CommandNotFound):
            await ctx.channel.send("not even a real command bruh")
        else:
            raise error
            await ctx.send(error)

    @commands.Cog.listener()
    async def on_message(self, message):
        if self.bot.user.mentioned_in(message) and self.bot.user != message.author:
            await message.reply("lol dat me")

        '''if self.bot.user != message.author and '<' not in message.content:
            if has_numbers(message.content) == True:
                for i in message.content:
                    if i.lower() in letter:
                        break
                    else:
                        await calc(message)
                        break'''
        if message.content.lower() == 'utsho':
            await message.channel.send('What a sexy beast <:bite:806383682629664840> ')
        if message.content.lower() == 'kiss me':
            await message.reply(
                'https://tenor.com/view/caught-in-4k-caught-in4k-chungus-gif-19840038'
            )

def setup(bot):
    bot.add_cog(events(bot))
