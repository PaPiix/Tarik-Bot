import discord
from discord.ext import commands

class OfficialDiscord:
    """Gives the link to the Official Discord of Tarik."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def officialdiscord(self):
        """Gives the official discord link to Tarik's HQ and Support."""
        await self.bot.say("discord.gg/tarik")

def setup(bot):
    bot.add_cog(OfficialDiscord(bot))