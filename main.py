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
  message = ""
  for extension in initial_extensions:
    try:
      bot.unload_extension(extension)
      bot.load_extension(extension)
      #await ctx.send("reloaded " + extension)
      message = message + "reloaded " + extension + "\n"
    except Exception as e:
      #await ctx.send(f'Failed to reload extension {extension}.')
      message = message + "Failed to reload " + extension + "\n"
  await ctx.send(message)


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