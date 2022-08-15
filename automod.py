from googleapiclient import discovery
from discord.ext import commands
import discord

result = ''
class automod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_message(self, message):
        global result
        if message.author == self.bot.user:
            return
        if message.author.bot:
            return
        try:
            API_KEY = 'AIzaSyDi5mm1Mb15JT7NTjt_npguMxu5S6A-8tI'
            analyze_request = {
                'comment': {'text': message.content},
                'requestedAttributes': {'TOXICITY': {}}
            }
            client = discovery.build(
                "commentanalyzer",
                "v1alpha1",
                developerKey=API_KEY,
                discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
                static_discovery=False,
            )
            response = client.comments().analyze(body=analyze_request).execute()
            result = response['attributeScores']['TOXICITY']['summaryScore']['value']
            print(result)
            #print(json.dumps(response, indent=2))
            if result >= 0.7:
                embed = discord.Embed(title=f"{message.author}, please tone it down", description=f"your toxicity score was {result}", color=0x19B9B9)
                await message.channel.send(embed=embed)
        except:
            print("something went wrong")


def setup(bot):
    bot.add_cog(automod(bot))
