import discord
from discord.ext import commands
import tarik

class Invite:
    """Gives the invite link to Tarik"""

    def __init__(self, bot):
        self.bot = tarik.Tarik

    @commands.command()    
    async def invite(self, ctx):
        """Gives the user my OAuth2 link"""
        try:
            await ctx.send('Send it to you through dms')
            await ctx.author.send('https://discordapp.com/oauth2/authorize?client_id=363788846011252739&scope=bot&permissions=8')
        except Excepttion as e:
            await ctx.send("Doh! I couldn't send you the dm.")
            tarik.logger.warning(e)
def setup(bot):
    bot.add_cog(Invite())
    logger.info('loaded this dumbass cog')
