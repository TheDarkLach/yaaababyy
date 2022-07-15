
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
          #print(result)
          with open('test.txt', mode='wb') as file:
              file.write(response.content)

          f1 = open('test.txt', 'r+')
          input = f1.read()
          input = input.replace('{', "{\n").replace(',',',\n')
          f2 = open("test.txt", "w+")
          f2.write(input)
          f1.close()
          f2.close()

          with open('test.txt') as f:
              for i, line in enumerate(f, 1):
                  if i == 44:
                      break
          max = line
          print(max)
          with open('test.txt') as f:
              for i, line in enumerate(f, 1):
                  if i == 46:
                      break
          min = line
          with open('test.txt') as f:
              for i, line in enumerate(f, 1):
                  if i == 66:
                      break
          rise = line
          with open('test.txt') as f:
              for i, line in enumerate(f, 1):
                  if i == 67:
                      break
          set = line
          with open('test.txt') as f:
              for i, line in enumerate(f, 1):
                  if i == 29:
                      break
          humid = line




          city = result['location']['name']
          country = result['location']['country']
          region = result['location']['region']
          time = result['location']['localtime']
          wcond = result['current']['condition']['text']
          fahrenheit = result['current']['temp_f']
          fflike = result['current']['feelslike_f']
          icon = result['current']['condition']['icon']
          max = max.replace('"maxtemp_f":','').replace(',','')
          min = min.replace('"mintemp_f":', '').replace(',', '')
          rise = rise.replace('"sunrise":','').replace(',','').replace('"','')
          set = rise.replace('"sunset":', '').replace(',', '').replace('"','')
          humid = humid.replace('"humidity":','').replace(',','')
          icon = "http:" + icon
          print(icon)

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


def setup(bot):
    bot.add_cog(weather(bot))

