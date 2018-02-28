import discord
from discord.ext import commands

class OwnerInfo:
    """Gives information about the Bot owner."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=False)
    async def owner_twitter(self):
        """Gives the owner's twitter link."""
        await self.bot.say("http://www.twitter.com/ttxftw")
        
    @commands.command(hidden=False)
    async def owner_yt(self):
        """Gives the owner's youtube channel link."""
        await self.bot.say("http://www.youtube.com/ttxftw") 

def setup(bot):
    bot.add_cog(OwnerInfo(bot))
