import discord
from discord.ext import commands
from random import randint
from random import choice

class Avatar:
    """Shows a users avatar."""
    def __init__(self, bot):
        self.bot = bot
    
    # Just a quick cog that will return a specified user's avatar.
    
    @commands.command(pass_context=True, no_pm=True)
    async def avatar(self, ctx, user : discord.Member):
    
        try:  
            colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
            colour = int(colour, 16)    
            embed=discord.Embed(colour=discord.Colour(value=colour))
            embed.set_author(name="{}'s avatar:".format(user.name), url=user.avatar_url)
            embed.set_image(url=user.avatar_url)
        
            await self.bot.say(embed=embed)     
        except discord.HTTPException:
            await self.bot.say(user.avatar_url)     
            print("Missing the embed permissions, so I won't embed")
   

def setup(bot):
    bot.add_cog(Avatar(bot))
