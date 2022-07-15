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
        with open('mc.txt', mode='wb') as file:
            file.write(response.content)
        f1 = open('mc.txt', 'r+')
        input = f1.read()
        input = input.replace('"', "\n")
        f2 = open("mc.txt", "w+")
        f2.write(input)
        f1.close()
        f2.close()

        #line 8 is the uuid
        with open('mc.txt') as f:
            for i, line in enumerate(f, 1):
                if i == 8:
                    break
        uuid = line
        #print(uuid)

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
            print('Image sucessfully Downloaded: ', "mc.png")
        else:
            print('Image Couldn\'t be retrieved')
        with open('mc.png', "rb") as fh:
            f = discord.File(fh, filename='mc.png')
        await ctx.send(file=f)



def setup(bot):
    bot.add_cog(minecraft(bot))