import math

import discord
from discord.ext import commands,bridge

import ytdl
import voice


class music(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.voice_states = {}

    def get_voice_state(self, ctx: commands.Context):
        """Returns or creates voice.VoiceState for the guild defined in the passed ctx"""
        state = self.voice_states.get(ctx.guild.id)
        if not state or not state.exists:
            state = voice.VoiceState(self.bot, ctx)
            self.voice_states[ctx.guild.id] = state

        return state

    def cog_unload(self):
        """Unloads the music cog"""
        for state in self.voice_states.values():
            self.bot.loop.create_task(state.stop())

    def cog_check(self, ctx: commands.Context):
        """Prevent calling commands in DM's"""
        if not ctx.guild:
            raise commands.NoPrivateMessage('This command can\'t be used in DM channels.')

        return True

    async def cog_before_invoke(self, ctx: commands.Context):
        # Set voice state for every command
        ctx.voice_state = self.get_voice_state(ctx)

    async def cog_command_error(self, ctx: commands.Context, error: commands.CommandError):
        await ctx.respond('An error occurred: {}'.format(str(error)))

    @bridge.bridge_command(invoke_without_subcommand=True)
    async def join(self, ctx: commands.Context):
        """Joins a voice channel."""

        destination = ctx.author.voice.channel
        if ctx.voice_state.voice:
            await ctx.voice_state.voice.move_to(destination)
            return

        ctx.voice_state.voice = await destination.connect()

    @bridge.bridge_command(help = 'brings scoob to vc')
    async def summon(self, ctx: commands.Context, *, channel: discord.VoiceChannel = None):
        """Summons the bot to a voice channel.
        If no channel was specified, it joins your channel.
        """

        if not channel and not ctx.author.voice:
            raise voice.VoiceError('You are neither connected to a voice channel nor specified a channel to join.')

        destination = channel or ctx.author.voice.channel
        if ctx.voice_state.voice:
            await ctx.voice_state.voice.move_to(destination)
            return

        ctx.voice_state.voice = await destination.connect()

    @bridge.bridge_command(help = 'leave vc')
    async def leave(self, ctx: commands.Context):
        """Clears the queue and leaves the voice channel."""

        if not ctx.voice_state.voice:
            return await ctx.respond('Not connected to any voice channel.')

        await ctx.voice_state.stop()
        del self.voice_states[ctx.guild.id]

    @bridge.bridge_command(help = 'adjusts volume (does not work)')
    async def volume(self, ctx: commands.Context, *, volume: int):
        """Sets the volume of the player."""

        if not ctx.voice_state.is_playing:
            return await ctx.respond('Nothing being played at the moment.')

        if 0 > volume > 100:
            return await ctx.respond('Volume must be between 0 and 100')
        try:
            self.source.volume = float(volume) / 100.0
            await ctx.respond('Volume of the player set to {}%'.format(volume))
        except Exception as e:
            print(e)

    @bridge.bridge_command(help = 'display current song')
    async def now(self, ctx: commands.Context):
        """Displays the currently playing song."""
        embed = ctx.voice_state.current.create_embed()
        await ctx.respond(embed=embed)

    @bridge.bridge_command(help = 'pause music')
    async def pause(self, ctx: commands.Context):
        """Pauses the currently playing song."""
        print(">>>Pause Command:")
        if ctx.voice_state.is_playing and ctx.voice_state.voice.is_playing():
            ctx.voice_state.voice.pause()
            await ctx.message.add_reaction('⏯')

    @bridge.bridge_command(help = 'resume music')
    async def resume(self, ctx: commands.Context):
        """Resumes a currently paused song."""

        if ctx.voice_state.is_playing and ctx.voice_state.voice.is_paused():
            ctx.voice_state.voice.resume()
            await ctx.message.add_reaction('⏯')

    @bridge.bridge_command(help = 'stop playing')
    async def stop(self, ctx: commands.Context):
        """Stops playing song and clears the queue."""

        ctx.voice_state.songs.clear()

        if ctx.voice_state.autoplay:
            ctx.voice_state.autoplay = False
            await ctx.respond('Autoplay is now turned off')

        if ctx.voice_state.is_playing:
            ctx.voice_state.voice.stop()
            await ctx.message.add_reaction('⏹')

    @bridge.bridge_command(help = 'skip song')
    async def skip(self, ctx: commands.Context):
        """Vote to skip a song. The requester can automatically skip.
        3 skip votes are needed for the song to be skipped.
        """

        if not ctx.voice_state.is_playing:
            return await ctx.respond('Not playing any music right now...')

        voter = ctx.message.author
        if voter == ctx.voice_state.current.requester:
            await ctx.message.add_reaction('⏭')
            ctx.voice_state.skip()

        elif voter.id not in ctx.voice_state.skip_votes:
            ctx.voice_state.skip_votes.add(voter.id)
            total_votes = len(ctx.voice_state.skip_votes)

            if total_votes >= 3:
                await ctx.message.add_reaction('⏭')
                ctx.voice_state.skip()
            else:
                await ctx.respond('Skip vote added, currently at **{}/3**'.format(total_votes))

        else:
            await ctx.respond('You have already voted to skip this song.')

    @bridge.bridge_command(help = 'displays queue')
    async def queue(self, ctx: commands.Context, *, page: int = 1):
        """Shows the player's queue.
        You can optionally specify the page to show. Each page contains 10 elements.
        """

        if len(ctx.voice_state.songs) == 0:
            return await ctx.respond('Empty queue.')

        items_per_page = 10
        pages = math.ceil(len(ctx.voice_state.songs) / items_per_page)

        start = (page - 1) * items_per_page
        end = start + items_per_page

        queue = ''
        for i, song in enumerate(ctx.voice_state.songs[start:end], start=start):
            queue += '`{0}.` [**{1.source.title}**]({1.source.url})\n'.format(i + 1, song)

        embed = (discord.Embed(description='**{} tracks:**\n\n{}'.format(len(ctx.voice_state.songs), queue))
                 .set_footer(text='Viewing page {}/{}'.format(page, pages)))
        await ctx.respond(embed=embed)

    @bridge.bridge_command(help = 'show songs played during this session')
    async def history(self, ctx: commands.Context, *, page: int = 1):
        """Shows the player's history.
        You can optionally specify the page to show. Each page contains 10 elements.
        """

        if len(ctx.voice_state.song_history) == 0:
            return await ctx.respond('Empty history.')

        items_per_page = 10
        pages = math.ceil(len(ctx.voice_state.song_history) / items_per_page)

        start = (page - 1) * items_per_page
        end = start + items_per_page

        queue = ''
        for i, song in enumerate(ctx.voice_state.song_history[start:end], start=start):
            queue += '`{0}.` [**{1.source.title}**]({1.source.url})\n'.format(i + 1, song)

        embed = (discord.Embed(description='**{} tracks:**\n\n{}'.format(len(ctx.voice_state.song_history), queue))
                 .set_footer(text='Viewing page {}/{}'.format(page, pages)))
        await ctx.respond(embed=embed)

    @bridge.bridge_command(help = 'shuffle queue')
    async def shuffle(self, ctx: commands.Context):
        """Shuffles the queue."""

        if len(ctx.voice_state.songs) == 0:
            return await ctx.respond('Empty queue.')

        ctx.voice_state.songs.shuffle()
        await ctx.message.add_reaction('✅')

    @bridge.bridge_command(help = 'remove a song in the queue')
    async def remove(self, ctx: commands.Context, index: int):
        """Removes a song from the queue at a given index."""

        if len(ctx.voice_state.songs) == 0:
            return await ctx.respond('Empty queue.')

        ctx.voice_state.songs.remove(index - 1)
        await ctx.message.add_reaction('✅')

    @bridge.bridge_command(help = 'loops a song')
    async def loop(self, ctx: commands.Context):
        """Loops the currently playing song.
        Invoke this command again to unloop the song.
        """

        if not ctx.voice_state.is_playing:
            return await ctx.respond('Nothing being played at the moment.')

        # Inverse boolean value to loop and unloop.
        ctx.voice_state.loop = not ctx.voice_state.loop
        await ctx.message.add_reaction('✅')
        await ctx.respond('Looping a song is now turned ' + ('on' if ctx.voice_state.loop else 'off'))

    @bridge.bridge_command(help = 'doesnt even work so who cares')
    async def autoplay(self, ctx: commands.Context):
        """Automatically queue a new song that is related to the song at the end of the queue.
        Invoke this command again to toggle autoplay the song.
        """

        if not ctx.voice_state.is_playing:
            return await ctx.respond('Nothing being played at the moment.')

        # Inverse boolean value to loop and unloop.
        ctx.voice_state.autoplay = not ctx.voice_state.autoplay
        await ctx.message.add_reaction('✅')
        await ctx.respond('Autoplay after end of queue is now ' + ('on' if ctx.voice_state.autoplay else 'off'))

    @bridge.bridge_command(help = 'play a song !')
    async def play(self, ctx: commands.Context, *, search: str):
        """Plays a song.
        If there are songs in the queue, this will be queued until the
        other songs finished playing.
        This command automatically searches from various sites if no URL is provided.
        A list of these sites can be found here: https://rg3.github.io/youtube-dl/supportedsites.html
        """

        async with ctx.typing():
            try:
                source = await ytdl.YTDLSource.create_source(ctx, search, loop=self.bot.loop)
            except ytdl.YTDLError as e:
                await ctx.respond('An error occurred while processing this request: {}'.format(str(e)))
            else:
                if not ctx.voice_state.voice:
                    await ctx.invoke(self.join)

                song = voice.Song(source)
                await ctx.voice_state.songs.put(song)
                await ctx.respond('Added {} to queue'.format(str(source)))

    @bridge.bridge_command(help = 'doesnt work either')
    async def search(self, ctx: commands.Context, *, search: str):
        """Searches youtube.
        It returns an imbed of the first 10 results collected from youtube.
        Then the user can choose one of the titles by typing a number
        in chat or they can cancel by typing "cancel" in chat.
        Each title in the list can be clicked as a link.
        """
        async with ctx.typing():
            try:
                source = await ytdl.YTDLSource.search_source(self.bot, ctx, search, loop=self.bot.loop)
            except ytdl.YTDLError as e:
                await ctx.respond('An error occurred while processing this request: {}'.format(str(e)))
            else:
                if source == 'sel_invalid':
                    await ctx.respond('Invalid selection')
                elif source == 'cancel':
                    await ctx.respond(':white_check_mark:')
                elif source == 'timeout':
                    await ctx.respond(':alarm_clock: **Time\'s up bud**')
                else:
                    if not ctx.voice_state.voice:
                        await ctx.invoke(self._join)

                    song = voice.Song(source)
                    await ctx.voice_state.songs.put(song)
                    await ctx.respond('Enqueued {}'.format(str(source)))


    async def ensure_voice_state(self, ctx: commands.Context):
        if not ctx.author.voice or not ctx.author.voice.channel:
            raise commands.CommandError('You are not connected to any voice channel.')

        if ctx.voice_client:
            if ctx.voice_client.channel != ctx.author.voice.channel:
                raise commands.CommandError('Bot is already in a voice channel.')

# needed to add cog to bot
def setup(bot):
    bot.add_cog(music(bot))