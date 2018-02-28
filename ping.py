import discord
from discord.ext import commands
from .utils.chat_formatting import *
from random import randint
from random import choice as randchoice
import time
from __main__ import send_cmd_help


class Ping:
    """Know your ping"""

    def __init__(self,bot):
        self.bot = bot
        

    @commands.command(pass_context=True)
    async def pingt(self,ctx):
        """time-ping time"""
        channel = ctx.message.channel
        colour = ''.join([randchoice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)		
        t1 = time.perf_counter()
        await self.bot.send_typing(channel)
        t2 = time.perf_counter()
        em = discord.Embed(description="Ping result: {}ms".format(round((t2-t1)*1000)), colour=discord.Colour(value=colour))

        await self.bot.say(embed=em)
        

def setup(bot):
    bot.add_cog(Ping(bot))


