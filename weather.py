from discord.ext import commands
import discord
import requests

class weather(commands.Cog):
  def __init__(self, bot):
      self.bot = bot


  @commands.command(help = 'weather')
  async def weather(self,ctx,*,city):
      try:
          base_url = "http://api.weatherapi.com/v1/forecast.json?key=713f2531413e4f02b95200222221407"
          city = city.replace(" ", "_")
          complete_url = base_url + "&q=" + city
          response = requests.get(complete_url)
          result = response.json()

          city = result['location']['name']
          country = result['location']['country']
          region = result['location']['region']
          time = result['location']['localtime']
          wcond = result['current']['condition']['text']
          fahrenheit = result['current']['temp_f']
          fflike = result['current']['feelslike_f']
          icon = result['current']['condition']['icon']
          max = result['forecast']['forecastday'][0]['day']['maxtemp_f']
          min = result['forecast']['forecastday'][0]['day']['mintemp_f']
          rise = result['forecast']['forecastday'][0]['astro']['sunrise']
          set = result['forecast']['forecastday'][0]['astro']['sunset']
          humid = result['forecast']['forecastday'][0]['day']['avghumidity']
          icon = result['forecast']['forecastday'][0]['day']['condition']['icon']
          icon = "http:" + icon

          embed = discord.Embed(title=f"{city}, {region}"' Weather', description=f"{country}", color=0x19B9B9)
          embed.add_field(name="Current Temperature F°", value=f"{fahrenheit}", inline=True)
          embed.add_field(name="Feels Like F°", value=f"{fflike}", inline=True)
          embed.add_field(name="\u200B", value="\u200B")  # newline
          embed.add_field(name="Condition", value=f"{wcond}", inline=True)
          embed.add_field(name="Humidity",value=f'{humid}',inline=True)
          embed.add_field(name="\u200B", value="\u200B")  # newline
          embed.add_field(name="Min. Temperature F°", value=f"{min}", inline=True)
          embed.add_field(name="Max. Temperature F°", value=f"{max}", inline=True)
          embed.add_field(name="\u200B", value="\u200B")  # newline
          embed.add_field(name="Sunrise", value=f"{rise}", inline=True)
          embed.add_field(name="Sunset", value=f"{set}", inline=True)

          embed.set_thumbnail(url=icon)
          embed.set_footer(text='Time: 'f"{time}")

          await ctx.send(embed=embed)
      except:
          embed = discord.Embed(title="No response", color=0x19B9B9)
          embed.add_field(name="Error", value="Please enter a city name", inline=True)
          await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(weather(bot))

