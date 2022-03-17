import discord
from discord.ext import commands
import os
from keep_alive import keep_alive

intents = discord.Intents.all()
intents.presences = True
intents.members = True
intents.messages = True


bot = commands.Bot(command_prefix='=',
                      help_command=None,
                      case_insensitive=True,
                      intents=intents,
                      allowed_mentions=discord.AllowedMentions(everyone=True))
bot.remove_command('help')


initial_extensions = (
    'delete',
    'mod',
    'commands',
    'events',
    'special',
    'social',
    'test',
)


for extension in initial_extensions:
  try:
    bot.load_extension(extension)
  except Exception as e:
    print(f'Failed to load extension {extension}.')

keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
bot.run(token)