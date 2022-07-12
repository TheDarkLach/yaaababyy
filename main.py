import discord
from discord.ext import commands
import os
import time
from pretty_help import DefaultMenu, PrettyHelp
from dotenv import load_dotenv

intents = discord.Intents().all()
intents.presences = True
intents.members = True
intents.messages = True


bot = commands.Bot(command_prefix='=',
                      help_command=PrettyHelp(),
                      case_insensitive=True,
                      intents=intents,
                      allowed_mentions=discord.AllowedMentions(everyone=True))
#bot.remove_command('help')

def is_owner():
    """Check if a user is the bot owner"""
    async def predicate(ctx):
        return ctx.author.id == 414931767129276428

    return commands.check(predicate)

initial_extensions = (
    'logs',
    'mod',
    'commands',
    'events',
    'special',
    'social',
    'music',
    'owner'
)

@bot.command(help = 'reloads modules')
@is_owner()
async def r(ctx):
  message = "```diff\n"
  for extension in initial_extensions:
    try:
      bot.unload_extension(extension)
      bot.load_extension(extension)
      message = message + "+ Reloaded " + extension + ".py\n"
    except Exception as e:
      message = message + "- Failed to reload " + extension + ".py\n"
  message = message + "```"
  await ctx.send(message)

@bot.command()
async def t(ctx):
    await ctx.send("```diff\n+ hi\n```")


for extension in initial_extensions:
  try:
    bot.load_extension(extension)
  except Exception as e:
    print(f'Failed to load extension {extension}.')

menu = DefaultMenu('◀️', '▶️', '❌') # You can copy-paste any icons you want.
bot.help_command = PrettyHelp(navigation=menu, color=discord.Colour.green(),no_category="Main") 

load_dotenv()
token = os.getenv("DISCORD_BOT_SECRET")
bot.run(token)