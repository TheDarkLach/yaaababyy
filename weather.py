from discord.ext import commands
import discord
import requests
from bs4 import BeautifulSoup


from discord.ext import commands
import discord
import requests
from bs4 import BeautifulSoup



class weather(commands.Cog):
  def __init__(self, bot):
      self.bot = bot


  @commands.command(help = 'weather')
  async def weather(self,ctx,*,city):
      try:
          base_url = "http://api.weatherapi.com/v1/current.json?key=713f2531413e4f02b95200222221407"
          city = city.replace(" ", "_")
          complete_url = base_url + "&q=" + city
          response = requests.get(complete_url)
          result = response.json()

          city = result['location']['name']
          country = result['location']['country']
          region = result['location']['region']
          time = result['location']['localtime']
          wcond = result['current']['condition']['text']
          celcius = result['current']['temp_c']
          fahrenheit = result['current']['temp_f']
          fclike = result['current']['feelslike_c']
          fflike = result['current']['feelslike_f']

          embed = discord.Embed(title=f"{city}, {region}"' Weather', description=f"{country}", color=0x19B9B9)
          embed.add_field(name="Temprature C°", value=f"{celcius}", inline=True)
          embed.add_field(name="Temprature F°", value=f"{fahrenheit}", inline=True)
          embed.add_field(name="Wind Condition", value=f"{wcond}", inline=False)
          embed.add_field(name="Feels Like C°", value=f"{fclike}", inline=True)
          embed.add_field(name="Feels Like F°", value=f"{fflike}", inline=True)
          embed.set_footer(text='Time: 'f"{time}")

          await ctx.send(embed=embed)
      except:
          embed = discord.Embed(title="No response", color=0x19B9B9)
          embed.add_field(name="Error", value="Please enter a city name", inline=True)
          await ctx.send(embed=embed)




def setup(bot):
    bot.add_cog(weather(bot))

