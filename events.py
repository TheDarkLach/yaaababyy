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

    @commands.Cog.listener()
    async def on_message(self, message):
        letter = 'abcdefghijklmnopqrstuvyxyz'
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

        if message.content.lower() == 'yasa':
            await message.channel.send('lol hate that guy')
        if message.author.id == 888925448954871868:
            await message.channel.send(
                "<@888925448954871868> suckin milk outta your moms titties like fine wine"
            )
        if message.content.lower() == 'utsho':
            await message.channel.send('What a sexy beast <:bite:806383682629664840> ')
        if message.content.lower() == 'nick':
            await message.channel.send('<:SAS:786066634929733663>')
        if message.content.lower() == 'looc':
            await message.channel.send(
                'Hot Hot Hot Hot Hot Hot Hot Hot Hot Hot Hot Hot Hot Hot Hot Hot Hot Hot Hot Hot Hot ')
        if message.content.lower() == 'boobie':
            await message.channel.send('mmm, yummy.')
        if message.content.lower() == 'kuzy':
            await message.channel.send(
                'your name is joe, ur opinion is irrelevant')
        if message.content.lower() == 'shoo':
            await message.channel.send('shoutout all the pears')
        if message.content.lower() == 'nafiz':
            await message.channel.send('fucking bitch ass hoe')
        if message.content.lower() == 'roudro':
            await message.channel.send('failed abortion')
        if message.content.lower() == 'cd':
            if 'cdn' in message.content:
                return
            else:
                await message.reply('see deez nuts lmao')
        if message.content.lower() == 'parodies':
            await message.reply('pair of deez nuts in ur mouth lmao')
        if message.content.lower() == 'tucker':
            await message.channel.send(
                'god he gives me such a raging boner lord have mercy')
        if message.content.lower() == 'disability':
            await message.reply('dis ability to fuck yo bitch')
        if message.content.lower() == 'fitness':
            await message.reply('fit this dick in yo mouth')
        if message.content.lower() == 'im gay':
            await message.reply('then prove it and come smack my ass ;)')
        if message.content.lower() == 'varun':
            await message.reply('lol come suck my dick bbg ;) -Utsho')
        if message.content.lower() == 'candice':
            await message.reply('candice dick fit in yo mouth, bitch')
        if message.content.lower() == 'parody':
            await message.reply('pair of deez nuts in yo mouth lmao')
        if message.content.lower() == 'kenya':
            await message.reply('kenya fit deez nuts in yo mouth')
        if message.content.lower() == 'russian':
            await message.reply("russian to suck dn")
        if message.content.lower() == 'dn':
            await message.reply("deez nuts")
        if message.content.lower() == 'pull':
            await message.reply("why don't you pull some bitches")
        if message.content.lower() == 'milk':
            await message.reply("0 hoes, ugly ass name")
        if message.content.lower() == 'james':
            await message.reply(
                "fat fucking white bitch whore ass fuck tard cum gobbler no hoes fat fuck musty as hell")

        if message.content.lower() == 'balls':
            await message.reply(
                "https://tenor.com/view/balls-love-struck-lick-tongue-gif-14644911"
            )
        if 'ass' in message.content:
            await message.reply(
                 'https://cdn.discordapp.com/emojis/627664851531071518.gif?v=1'
            )
        if message.content.lower() == 'kiss me':
            await message.reply(
                'https://tenor.com/view/caught-in-4k-caught-in4k-chungus-gif-19840038'
            )


def setup(bot):
    bot.add_cog(events(bot))
