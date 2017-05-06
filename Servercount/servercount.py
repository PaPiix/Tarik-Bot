import discord
from discord.ext import commands

class Servercount:
    """Shows the total servers and users that Tarik is connected to."""

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def servercount(self):
        """Shows the total servers and users that Tarik is connected to."""
        
        embed=discord.Embed(colour=0xFF0000)
        embed.add_field(name="__Servers__", value="Tarik is connected to __**{}**__ servers.".format(len(self.bot.servers)))
        embed.add_field(name="__Users__", value="Tarik is connected to __**{}**__ users.".format(str(len(set(self.bot.get_all_members())))))
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.set_author(name="Tarik", icon_url=self.bot.user.avatar_url)
        await self.bot.say(embed=embed) 
        
def setup(bot):
    bot.add_cog(Servercount(bot))