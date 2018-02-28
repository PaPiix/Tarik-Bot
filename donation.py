import discord
from discord.ext import commands

class Donation:
    """Gives the link to Tarik's donation page."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=False)
    async def donate(self):
        """Gives the link to Tarik's donation page."""
        await self.bot.say("**Donate here** :heart:: https://patreon.com/tarik / http://www.paypal.me/tariktekelioglu")

def setup(bot):
    bot.add_cog(Donation(bot))
