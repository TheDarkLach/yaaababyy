import json
import shutil
import discord
import requests
from discord.ext import commands
from io import BytesIO

class minecraft(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="mc skin renders")
    async def skin(self,ctx,user):
        url = "https://api.mojang.com/users/profiles/minecraft/" + user
        response = requests.get(url)
        result = json.loads(response.text)
        uuid = result['id']

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'
        }
        uuid = uuid.strip()
        url = "https://crafatar.com/renders/body/" + uuid + "?size=512&default=MHF_Steve&overlay=true.png"

        response = requests.get(url,headers=headers,stream=True)
        response.raw.decode_content = True
        if response.status_code == 200:
            with open("mc.png", 'wb') as f:
                shutil.copyfileobj(BytesIO(response.content), f)
        else:
            print('Image Couldn\'t be retrieved :(')
        with open('mc.png', "rb") as fh:
            f = discord.File(fh, filename='mc.png')
        await ctx.send(file=f)



async def setup(bot):
    await bot.add_cog(minecraft(bot))