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
        """SPEEEEEEEEED"""  
        await self.bot.say(":warning: SPEED TESTING")
        await self.bot.say("This may cause disruption to the bot temporarily. This may take a while...") 
        x = subprocess.check_output("speedtest-cli --secure --simple", shell=True).decode()
        message = x
        message = '```{}```'.format(x)
        await self.bot.say(message)

def setup(bot):
    n = Speedtest(bot)
    bot.add_cog(n)