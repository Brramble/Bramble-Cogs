import discord
from discord.ext import commands
import subprocess
import asyncio

class SpeedTest:

    def __init__(self,bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @commands.cooldown(1, 3600)
    async def speedtest(self):
        
        """Test host speed!"""
        
        await self.bot.say(":warning: This may cause disruption to the bot temporarily and may take a while...")
        speedresult = subprocess.check_output("speedtest-cli --secure --simple", shell=True).decode()
        message = speedresult
        em = discord.Embed(colour=0xEC2323, timestamp=__import__('datetime').datetime.utcnow())
        em.set_thumbnail(url=self.bot.user.avatar_url)
        em.add_field(name=":gear: SpeedTest Result\n", value="{}".format(speedresult))
        em.set_footer(text="Cooldown of 3600 seconds initiated")
        await self.bot.say(embed=em)
        

def setup(bot):
    n = SpeedTest(bot)
    bot.add_cog(n)
