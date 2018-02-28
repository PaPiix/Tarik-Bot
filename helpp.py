import discord
from discord.ext import commands

class Help:
    """Shows the commands of Tarik"""
    
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(pass_context=True)
    async def helpp(self, ctx):
        """Shows the commands of Tarik"""
        
        general = """
**{prefix}topservers** -  Shows the top 10 most popular servers that Tarik's in.
**{prefix}google** -  Search anything!
**{prefix}weather** -  Check the weather of any location!
**{prefix}calculate** -  Calculate a sum!
**{prefix}serverinfo** -  Shows information about the server.
**{prefix}userinfo** -  Shows information about a user.
**{prefix}avatar** -  Shows a users avatar.
**{prefix}names** -  Shows the list of a users past names/nicknames.
**{prefix}stopwatch** -  Starts/stops a stopwatch. 
**{prefix}donate** -  Information regarding donation.
**{prefix}donators** -  Get a list of all the donators & their commands.
**{prefix}website** -  The link to Tarik's website.
 
"""
        fun = """
**{prefix}meme** -  Generate a meme from a user's avatar or an image.   
**{prefix}penis** -  Check a user's penis length. (It's 100% accutate!) """
        
        mod = """
**{prefix}ban** -  Bans a user from the server.
**{prefix}softban** -  Kicks a user, deleting 1 day worth of messages.
**{prefix}hackban** -  Bans a user with their ID.
**{prefix}botclean** -  Cleans up all messages sent by bots.
**{prefix}cleaninvokes** -  Cleans all messages sent by bots & all it's triggers.
**{prefix}cleanup** -  Cleans up messages.
**{prefix}editrole** -  Edits role settings.
**{prefix}antilinkset** -  Removes links and warns users x times before kick.
**{prefix}filter** -  Filters/bans words from the server.
**{prefix}ignore** -  Makes the bot ignore the server/channel.
**{prefix}unignore** -  Unignores a channel/server.
**{prefix}kick** -  kicks a user from the server.
**{prefix}mute** -  Mutes a user from the server/channel.
**{prefix}unmute** -  Unmutes a user from the server/channel.
**{prefix}modset** -  Manages the server administration settings.
**{prefix}reason** -  Edits a users case.
**{prefix}rename** -  Changes a users nickname. """

#**{prefix}blacklist** -   Bans a user from using the bot.
#**{prefix}whitelist** -   Removes a user from the blacklist.   
        
        servermanagement = """   
**{prefix}autorole** -  Sets a specific role to a user when they join.  
**{prefix}antilink** -  Removes discord links; kicks the advertiser after x times. 
**{prefix}buyrole** -  A shop where users can buy roles using their credits.    
**{prefix}buyroleset** - Sets the shop for users to buy roles using their credits. """



        
        ctx_message=discord.Embed(title=":mailbox_with_mail: **Check your private messages!**", colour=0XFF0000)
        ctx_message.set_author(name="Tarik", icon_url=self.bot.user.avatar_url)
        
        title=discord.Embed(title="Here are all the commands:", colour=0xFF0000)
        title.set_author(name="Help sent", icon_url=self.bot.user.avatar_url)
        
        general = general.format(prefix=ctx.prefix)       
        embedgeneral=discord.Embed(colour=0xFF0000)
        embedgeneral.set_author(name="Page 1", icon_url=self.bot.user.avatar_url)
        embedgeneral.add_field(name="__**General**__", value=general)
        embedgeneral.set_thumbnail(url='http://i.imgur.com/jIpmTdQ.png')            
        
        fun = fun.format(prefix=ctx.prefix)
        embedfun=discord.Embed(colour=0xFF0000)
        embedfun.set_author(name="Page 2", icon_url=self.bot.user.avatar_url)
        embedfun.add_field(name="__**Fun**__", value=fun)
        embedfun.set_thumbnail(url='http://i.imgur.com/v99r4oR.png')
        
        mod = mod.format(prefix=ctx.prefix)
        embedmod=discord.Embed(colour=0xFF0000)
        embedmod.set_author(name="Page 3", icon_url=self.bot.user.avatar_url) 
        embedmod.add_field(name="__**Moderation Commands**__", value=mod) 
        embedmod.set_thumbnail(url='http://i.imgur.com/k6TjA9u.png')

        servermanagement = servermanagement.format(prefix=ctx.prefix)   
        embedservermanagement=discord.Embed(colour=0xFF0000)
        embedservermanagement.set_author(name="Page 4", icon_url=self.bot.user.avatar_url)
        embedservermanagement.add_field(name="__**Server Management**__", value=servermanagement)
        embedservermanagement.set_thumbnail(url='http://i.imgur.com/jgb8uHw.png')
        
        await self.bot.say(embed=ctx_message)
        await self.bot.whisper(embed=title)
        await self.bot.whisper(embed=embedgeneral)
        await self.bot.whisper(embed=embedfun)
        await self.bot.whisper(embed=embedmod)
        await self.bot.whisper(embed=embedservermanagement)
def setup(bot):
    bot.add_cog(Help(bot))