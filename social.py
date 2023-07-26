import discord
from discord.ext import commands, bridge
import datetime
import random
import requests


class social(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bridge.bridge_command(help='gives kanye quote')
    async def kanyequote(self, ctx):
        kanyeIMGS = [
            "https://www.biography.com/.image/ar_1:1%2Cc_fill%2Ccs_srgb%2Cg_face%2Cq_auto:good%2Cw_300/MTU0OTkwNDUxOTQ5MDUzNDQ3/kanye-west-attends-the-christian-dior-show-as-part-of-the-paris-fashion-week-womenswear-fall-winter-2015-2016-on-march-6-2015-in-paris-france-photo-by-dominique-charriau-wireimage-square.jpg",
            "https://storage.googleapis.com/afs-prod/media/1f764b198a42470189b99b4084be6cf0/800.jpeg",
            "https://www.gannett-cdn.com/presto/2019/03/07/USAT/71d24511-e504-40e1-95eb-180f883eeb81-LL_MW_KanyeWest_010319.JPG?width=600&height=900&fit=crop&format=pjpg&auto=webp",
            "https://pyxis.nymag.com/v1/imgs/014/a62/bc3a72ed5c47e8c0dd5bc52028c5df5005-kanye-west.2x.rsquare.w330.jpg",
            "https://www.aljazeera.com/wp-content/uploads/2020/09/Ye-1.jpg?resize=770%2C513",
            "https://images.businessoffashion.com/profiles/asset/1797/43897e2e4a6d155d72dd9df352017b546ef9e229.jpeg?auto=format%2Ccompress&fit=crop&h=360&w=660",
            "https://i.insider.com/5f624c55323fc4001e0d6a47?width=2000&format=jpeg&auto=webp",
            "https://www.wmagazine.com/wp-content/uploads/2019/10/25/5db30d540e538e000830c68a_GettyImages-1183294345.jpg?w=1352px",
            "https://i.guim.co.uk/img/media/07ad3146c3879e9d3da5e81aa32edf7160b93888/0_195_2326_1396/master/2326.jpg?width=1200&height=1200&quality=85&auto=format&fit=crop&s=8bdf6ca2f739479415c3a3b6d8fe890a",
        ]
        pick_img = random.choice(kanyeIMGS)

        response = requests.get('https://api.kanye.rest')
        data = response.json()

        embed = discord.Embed(
            title="From the Words of Kanye West:",
            description=f'"{data["quote"]}"',
            color=0,
        )

        embed.set_footer(
            text=f"Requested By {ctx.author}", icon_url=ctx.author.avatar_url
        )
        embed.set_thumbnail(url=pick_img)

        await ctx.respond(embed=embed)

    @bridge.bridge_command()
    async def president(self, ctx):
        embed = discord.Embed(
            title="This is your president:",
            description=
            "Sup dawgs it's me, ya boy, president Not BN. In my offtime I like long walks on the beach during sunset. Otherwise i'm fuckin bitches in my 3 story condo. bih yah peace out",
            color=0x19B9B9)
        embed.set_author(
            name="President Not BN",
            url="https://twitter.com/LachDark",
            icon_url=
            "https://pbs.twimg.com/profile_images/1397996923508781058/CNBym2zc_400x400.jpg"
        )
        embed.set_footer(text="Note: Not BN is in no way affiliated with BN")
        embed.set_thumbnail(url="https://i.imgur.com/C4QKvfT.png")
        await ctx.respond(embed=embed)

    @bridge.bridge_command(help='info on a server')
    async def info(self, ctx):
        embed = discord.Embed(title=f"{ctx.guild.name}",
                              description="Server data:",
                              timestamp=datetime.datetime.utcnow(),
                              color=0x19B9B9)
        embed.add_field(name="Server created at:", value=f"{ctx.guild.created_at}")
        embed.add_field(name="Server Owner:", value=f"{ctx.guild.owner}")
        embed.add_field(name="Server Region:",
                        value=f"{ctx.guild.region}".capitalize())
        embed.add_field(name="Server ID:", value=f"{ctx.guild.id}")
        embed.set_thumbnail(url=f"{ctx.guild.icon_url}")

        await ctx.respond(embed=embed)

    """ broken :(
    @bridge.bridge_command(aliases=["ig"], help='lookup an instagram page')
    async def instagram(self, ctx, instaUsername):
        from os import environ
        environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
        bot = Instaloader()
        profile = Profile.from_username(bot.context, str(instaUsername))
        embed = discord.Embed(title=f"Instagram", color=0x11019e)
        embed.add_field(name="Username",
                        value=f"`@{profile.username}`",
                        inline=True)
        embed.add_field(name="Followers",
                        value=f"{profile.followers}",
                        inline=True)
        embed.add_field(name="Follows", value=f"{profile.followees}", inline=True)
        embed.add_field(name="Bio", value=f"{profile.biography}", inline=True)
        await ctx.respond(embed=embed)
        """

    @bridge.bridge_command(aliases=["listening"], help='display current song')
    async def current(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author
            pass
        if user.activities:
            for activity in user.activities:
                if isinstance(activity, discord.Spotify):
                    embed = discord.Embed(description="Listening on spotify",
                                          color=0x19B9B9)
                    embed.set_author(name=user.name, icon_url=user.avatar_url)
                    embed.add_field(name="Track",
                                    value=f"{activity.title}",
                                    inline=False)
                    embed.add_field(name="Album",
                                    value=f"{activity.album}",
                                    inline=False)
                    embed.add_field(name="Artist",
                                    value=f"{activity.artist}",
                                    inline=False)
                    embed.set_thumbnail(url=activity.album_cover_url)
                    await ctx.respond(embed=embed)
        else:
            await ctx.respond("Bruh your activity empty")


def setup(bot):
    bot.add_cog(social(bot))
