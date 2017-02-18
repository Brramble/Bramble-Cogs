import discord
from discord.ext import commands
import subprocess
import asyncio

class Speedtest:

    def __init__(self,bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @commands.cooldown(1, 3600)
    async def speedtest(self):
        """Test host speed!"""  
        await self.bot.say(":warning:**SPEED TESTING**\n\nThis may cause disruption to the bot temporarily. This may take a while...")
        speedresult = subprocess.check_output("speedtest-cli --secure --simple", shell=True).decode()
        message = speedresult
        message = '```{}```'.format(speedresult)
        await self.bot.say(message)
        await self.bot.say("Cooldown of 3600 seconds initiated.")

def setup(bot):
    n = Speedtest(bot)
    bot.add_cog(n)
