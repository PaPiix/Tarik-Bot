import discord
import time
from discord.ext import commands
from random import choice, randint
import cogs.utils
import asyncio
from cogs.utils import checks
class disco:
    """Disco role"""

    def __init__(self, bot):
        self.bot = bot
    @checks.is_owner()
    @commands.command(pass_context = True, no_pm=True)
    async def discorole(self, ctx, times:int, interval:float, *, role):
        roleObj = discord.utils.find(lambda r: r.name == role, ctx.message.server.roles)
        if not roleObj:
            await self.bot.say("`{}` is not a valid role".format(role))
            return
        time = 0
        while time < times:
            colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
            colour = int(colour, 16)
            await self.bot.edit_role(ctx.message.server, roleObj, colour=discord.Colour(value=colour))
            time = time + 1
            await asyncio.sleep(interval)
    
    @checks.is_owner()
    @commands.command(pass_context = True, no_pm=True)
    async def discoroleinfinite(self, ctx, interval:float, *, role):
        roleObj = discord.utils.find(lambda r: r.name == role, ctx.message.server.roles)
        if not roleObj:
            await self.bot.say("`{}` is not a valid role".format(role))
            return
        while True:
            colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
            colour = int(colour, 16)
            await self.bot.edit_role(ctx.message.server, roleObj, colour=discord.Colour(value=colour))
            await asyncio.sleep(interval)

def setup(bot):
    n = disco(bot)
    bot.add_cog(n)