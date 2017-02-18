import discord
from discord.ext import commands
import subprocess
import asyncio

class Speedtest:

    def __init__(self,bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @commands.cooldown(1, 3600)
    async def speedtest(self, ctx):
        server = ctx.message.server
        
        """Test internet speeds of the bot's host! Coded by Bramble."""
        
        if self.bot.is_voice_connected(server):
            await self.bot.say("You must make me leave the voice channel before I do my test.")
        else:
            await self.bot.say(":Warning: This may cause disruption to the bot temporarily and may take a while...")
            speedresult = subprocess.check_output("speedtest-cli --secure --simple", shell=True).decode()
            em = discord.Embed(colour=0xEC2323, timestamp=__import__('datetime').datetime.utcnow())
            em.set_thumbnail(url=self.bot.user.avatar_url)
            em.add_field(name=":gear: SpeedTest Result\n", value="{}".format(speedresult))
            em.set_footer(text="Cooldown of 3600 seconds initiated")
            await self.bot.say(embed=em)       

def setup(bot):
    n = Speedtest(bot)
    bot.add_cog(n)
