import discord
from discord.ext import commands
from __main__ import send_cmd_help


class Giveme:
    """This cog is made for Tarik's Discord only."""

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(pass_context=True)
    async def giveme(self, ctx, *, role_name):
        """Apply a role in Tarik's Discord."""

        roles = ['coding', 'gamer', 'content creator', 'international', 'student', 'anime', 'gfx', 'c++', 'html/php', 'java', 'python', 'javascript', 'nsfw', 'tarik info', 'dank memer', 'red', 'blue', 'ocean blue', 'green', 'navy', 'purple', 'pink', 'yellow', 'grey', 'purple', 'brown', 'black', 'orange', 'turquoise', 'dark purple']  
        tariksdiscord = self.bot.get_server("210535197286989826")

        server = ctx.message.server
        author = ctx.message.author
        name = role_name
        if server.id == tariksdiscord.id:
            for role in server.roles:
                if role.name.lower() == name.lower() and name.lower() in roles:
                    try:
                        em = discord.Embed(colour=0xFF0000)
                        em.set_author(name='Role {} has been applied to {}.'.format(role.name, author.display_name), icon_url=author.avatar_url)
                        await self.bot.add_roles(author, role)
                        await self.bot.say(embed=em)
                    except:
                        pass 
                    if roles in author.roles:
                        em = discord.Embed(colour=0xFF0000)
                        em.set_author(name='You already have the {} role.'.format(role_name))
                        await self.bot.say(embed=embed) 

    @commands.command(pass_context=True)
    async def giveback(self, ctx, *, role_name):
        """Apply a role in Tarik's Discord."""

        roles = ['coding', 'gamer', 'content creator', 'international', 'student', 'anime', 'gfx', 'c++', 'html/php', 'java', 'python', 'javascript', 'nsfw', 'tarik info', 'dank memer', 'red', 'blue', 'ocean blue', 'green', 'navy', 'purple', 'pink', 'yellow', 'grey', 'purple', 'brown', 'black', 'orange', 'turquoise', 'dark purple']  
        tariksdiscord = self.bot.get_server("210535197286989826")

        server = ctx.message.server
        author = ctx.message.author
        name = role_name
        if server.id == tariksdiscord.id:
            for role in server.roles:
                if role.name.lower() == name.lower() and name.lower() in roles:
                    try:
                        em = discord.Embed(colour=0xFF0000)
                        em.set_author(name='Role {} has been removed from {}.'.format(role.name, author.display_name), icon_url=author.avatar_url)
                        await self.bot.remove_roles(author, role)
                        await self.bot.say(embed=em)
                    except:
                        pass                        
                        
def setup(bot):
    n = Giveme(bot)
    bot.add_cog(n)
                        
