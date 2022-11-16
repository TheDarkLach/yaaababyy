import discord
from discord.ext.pages import PaginatorButton, Paginator
from discord.ext import bridge, commands, pages


class page(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.pages = [
            "Page 1",
            [
                discord.Embed(title="Page 2, Embed 1"),
                discord.Embed(title="Page 2, Embed 2"),
            ],
            "Page Three",
            discord.Embed(title="Page Four"),
            discord.Embed(
                title="Page Five",
                fields=[
                    discord.EmbedField(
                        name="Example Field", value="Example Value", inline=False
                    ),
                ],
            ),
            [
                discord.Embed(title="Page Six, Embed 1"),
                discord.Embed(title="Page Seven, Embed 2"),
            ],
        ]
        self.pages[3].set_image(
            url="https://c.tenor.com/pPKOYQpTO8AAAAAM/monkey-developer.gif"
        )
        self.pages[4].add_field(
            name="Another Example Field", value="Another Example Value", inline=False
        )

        self.more_pages = [
            "Second Page One",
            discord.Embed(title="Second Page Two"),
            discord.Embed(title="Second Page Three"),
        ]

        self.even_more_pages = ["11111", "22222", "33333"]

        self.new_pages = [
            pages.Page(
                content="Page 1 Title!",
                embeds=[
                    discord.Embed(title="New Page 1 Embed Title 1!"),
                    discord.Embed(title="New Page 1 Embed Title 2!"),
                ],
            ),
            pages.Page(
                content="Page 2 Title!",
                embeds=[
                    discord.Embed(title="New Page 2 Embed Title 1!"),
                    discord.Embed(title="New Page 2 Embed Title 2!"),
                ],
            ),
        ]

    def get_pages(self):
        return self.pages

    @bridge.bridge_command(help="test")
    async def page(self,ctx):
        page_buttons = [
            pages.PaginatorButton(
                "first", label="<<-", style=discord.ButtonStyle.green
            ),
            pages.PaginatorButton("prev", label="<-", style=discord.ButtonStyle.green),
            pages.PaginatorButton(
                "page_indicator", style=discord.ButtonStyle.gray, disabled=True
            ),
            pages.PaginatorButton("next", label="->", style=discord.ButtonStyle.green),
            pages.PaginatorButton("last", label="->>", style=discord.ButtonStyle.green),
        ]
        paginator = pages.Paginator(
            pages=self.get_pages(),
            show_disabled=True,
            show_indicator=True,
            use_default_buttons=False,
            custom_buttons=page_buttons,
            loop_pages=True,
        )
        await paginator.respond(ctx, ephemeral=False)

def setup(bot):
    bot.add_cog(page(bot))