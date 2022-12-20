import discord
from discord.ext import commands,bridge
import os
from pretty_help import DefaultMenu, PrettyHelp
from dotenv import load_dotenv

intents = discord.Intents().all()


bot = bridge.Bot(command_prefix='=',
                      help_command=PrettyHelp(),
                      case_insensitive=True,
                      intents=intents,
                      allowed_mentions=discord.AllowedMentions(everyone=True))

def is_owner():
    """Check if a user is the bot owner"""
    async def predicate(ctx):
        return ctx.author.id == 414931767129276428

    return commands.check(predicate)



@bot.event
async def on_ready():
  print("Logged in as: " + str(bot.user))
  await bot.change_presence(activity=discord.Game(name="Ur Mom"))

initial_extensions = (
    'logs',
    'mod',
    'commands',
    'events',
    'special',
    'social',
    'music',
    'owner',
    'weather',
    'minecraft',
    'pokemon',
    'automod',
    'paladins',
    'page',
    'smite',
)

@bot.bridge_command(help = 'reloads modules')
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
  await ctx.respond(message)

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