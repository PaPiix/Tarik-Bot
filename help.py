import discord
from discord.ext import commands

class Help:
    """Shows the commands of Tarik"""
    
    
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(pass_context=True, name='help')
    async def _help(self, ctx):
        """Shows the commands of Tarik"""
        
        general = """
**{prefix}topservers :** Shows the top 10 most popular servers that Tarik's in.
**{prefix}google :** Search anything!
**{prefix}weather :** Check the weather of any location!
**{prefix}calculate :** Calculate a sum!
**{prefix}serverinfo :** Shows information about the server.
**{prefix}userinfo :** Shows information about a user.
**{prefix}avatar :** Shows a users avatar.
**{prefix}names :** Shows the list of a users past names/nicknames.
**{prefix}stopwatch :** Starts/stops a stopwatch. 
**{prefix}away :** Tell the bot if you're away or not.
**{prefix}translate :** Translates to any language.
**{prefix}roles :** Displays all the roles in the server.
**{prefix}role :** Displays all the users with a specific role and the amount.
**{prefix}nsfw :** All NSFW commands.
 
"""
        music = """
**{prefix}play :** Plays a link / searches and play.
**{prefix}song :** Info about the current song.
**{prefix}pause :** Pauses the current song, .resume to continue.
**{prefix}resume :** Resumes a paused song or playlist.
**{prefix}skip :** Skips a song, using the set threshold if the requester isn't.
**{prefix}stop :** Stops a currently playing song or playlist.
**{prefix}volume :** Sets the volume (0 - 100).
**{prefix}queue :** Shows the current queue.
**{prefix}disconnect :** Disconnects Tarik from the voice channel. """       
        
        
        fun = """
**{prefix}meme :** Generate a meme from a user's avatar or an image.   
**{prefix}penis :** Check a user's penis length. (It's 100% accutate!) 
**{prefix}3dtext :** Turns text into 3D.             
**{prefix}3dtext1 :** Turns text into 3D v1.            
**{prefix}3dtext2 :** Turns text into 3D v2.           
**{prefix}3dtext3 :** Turns text into 3D v3.          
**{prefix}3dtext4 :** Turns text into 3D v4.         
**{prefix}art :** Turns text into Art.                
**{prefix}ascii :** Turns text into Ascii.             
**{prefix}bigtext :** Massivly enlarges text. 3-4 characters only.          
**{prefix}blocktext :** Turns text into Blocks.          
**{prefix}graffiti :** Turns text into Graffiti.          
**{prefix}keytext :** Turns text into a keyboard.               
**{prefix}matrix :** Turns text into a matrix style.                 
**{prefix}mirrortext :** Mirrors a text.            
**{prefix}puffytext :** Turns text into a puffy writing.          
**{prefix}slant :** Slants text.             
**{prefix}speedtext :** Turns text into a speedy style. 
**{prefix}text :** Generates an image with text on it.      """

        fun2 = """
**{prefix}lottery :** Server lotteries where users can earn credits!
**{prefix}setlottery :** Lottery settings. 
**{prefix}buyrole :** A shop where users can buy roles using their credits. 
**{prefix}trivia :** Trivia games.
**{prefix}build :** Generates fancy images.
**{prefix}rickroll :** Generates rickroll images.         
**{prefix}userbar :** Generates a server-based userbar.
**{prefix}gif :** Retrieves first search result from giphy.
**{prefix}gifr :** Retrieves a random gif from a giphy search .
**{prefix}imgur :** Retrieves a picture from imgur. 
**{prefix}kill :** Kill someone in a __creative__ way! 
**{prefix}shop :** Shop Commands.
**{prefix}pending :** Pending shop list. 
**{prefix}marry :** Marry a user.
**{prefix}divorce :** Divorce a user.
**{prefix}marryset :** Sets the channel for the marriage logs. Set no channel to disable.
**{prefix}spoiler :** Generates a spoiler GIF.""" 

        fun3 = """
**{prefix}gardening :** Gardening commands.
 """      
        
        mod = """
**{prefix}ban :** Bans a user from the server.
**{prefix}softban :** Kicks a user, deleting 1 day worth of messages.
**{prefix}hackban :** Bans a user with their ID.
**{prefix}botclean :** Cleans all messages sent by bots & all it's triggers.
**{prefix}cleanup :** Cleans up messages.
**{prefix}prune :** Prunes messages, images, embeds etc..
**{prefix}editrole :** Edits role settings.
**{prefix}filter :** Filters/bans words from the server.
**{prefix}ignore :** Makes the bot ignore the server/channel.
**{prefix}unignore :** Unignores a channel/server.
**{prefix}kick :** kicks a user from the server.
**{prefix}mute :** Mutes a user from the server/channel.
**{prefix}unmute :** Unmutes a user from the server/channel.
**{prefix}modset :** Manages the server administration settings.
**{prefix}reason :** Edits a users case.
**{prefix}rename :** Changes a users nickname.
**{prefix}massmove :** Moves everyone for one channel to another.
**{prefix}move :** Moves users from a voice channel to another. 
**{prefix}logs :** Logs past activity. """

#**{prefix}blacklist :**  Bans a user from using the bot.
#**{prefix}whitelist :**  Removes a user from the blacklist.   
        
        servermanagement = """   
**{prefix}autorole :** Sets a specific role to a user when they join.  
**{prefix}antilink :** Removes discord links; kicks the advertiser after x times.   
**{prefix}serverprefix :** Sets Tarik's server prefix.
**{prefix}buyroleset :** Sets the shop for users to buy roles using their credits. 
**{prefix}setshop :** Shop configuration settings
**{prefix}p :** Commands/cogs permissions settings.
**{prefix}disable :** Disables a command.
**{prefix}disabled :** Lists all disabled commands.
**{prefix}enable :** Enables a command.
**{prefix}modlogset :** Sets the channel for activity logging.
**{prefix}modlogtoggle :** Toggles all the activity you want the bot to log.
**{prefix}welcomeset :** Sets a welcome/goodbye message. (Simple)
**{prefix}welcomer :** An advanced version of welcomeset. Can be embeded.
**{prefix}freerole :** Free roles which anyone can apply for. Mainly used for colours.
**{prefix}addcom :** Adds a custom command for the server.
**{prefix}customcommands :** Lists all the custom server commands.
**{prefix}delcom :** Deletes a custom command.
**{prefix}editcom :** Edits a custom command.
"""

        servermanagement2 = """
**{prefix}scheduler :** Makes the bot run a command. Can be repeated every x seconds. """       
        
        economy = """
**{prefix}bank :** All the bank related things/settings.   
**{prefix}payday :** Daily free credits. 
**{prefix}balance :** Shows your/users current balance.
**{prefix}casino :** All the casino related things.
**{prefix}setcasino :** All the casino settings.
**{prefix}heist :** All heist related things.
**{prefix}setheist : ** All the heist settings.
**{prefix}economyset :** All the economy settings.
**{prefix}slot :** Bet your credits.
**{prefix}blackjack :** Bet your casino credits with blackjack.
**{prefix}allin :** Bet everything you have.
**{prefix}pay :** Pay a user. 
**{prefix}coin :** Bet on heads or tails.      
**{prefix}cups :** Pick the cup that is hiding the gold coin. Choose 1, 2, 3...
**{prefix}dice :** Roll 2, 7, 11 or 12 to win.
**{prefix}hilo :** Pick High, Low, Seven. Lo is < 7 Hi is > 7. 6x payout on 7.
**{prefix}war :** Modified War Card Game. """

        botinfo = """
**{prefix}info :** Shows all of Tarik's information.
**{prefix}servercount :** Shows the total servers and users Tarik connected to.
**{prefix}website :** Shows Tarik's website.
**{prefix}officialdiscord :** Links Tarik's official Discord.
**{prefix}donate :** Information regarding donation.
**{prefix}donators :** Get a list of all the donators & their commands. """     
        
        help = """
**{prefix}help :** Returns this entire message.
**{prefix}invite :** Invite Tarik.
**{prefix}contact :** Contacts the owner.
**{prefix}moderation :** Shows all the moderation commands.
**{prefix}general :** Shows all the general commands.
**{prefix}economy :** Shows all the economy commands.      
**{prefix}cooltext :** Shows all the cool text commands. """
            
        
        ctx_message=discord.Embed(title=":mailbox_with_mail: **Check your private messages!**", colour=0XFF0000)
        ctx_message.set_author(name="Help sent!", icon_url=self.bot.user.avatar_url)
        
        title=discord.Embed(title="Here are all the commands:", colour=0xFF0000)
        title.set_author(name="Help sent")
        
        general = general.format(prefix=ctx.prefix)       
        embedgeneral=discord.Embed(colour=0x00FF29)
        embedgeneral.set_author(name="Page 1")
        embedgeneral.add_field(name="__**General**__", value=general)           
        
        music = music.format(prefix=ctx.prefix)       
        embedmusic=discord.Embed(title="NOTE: MUSIC IS CURRENTLY DISABLED.", colour=0x7A00FF)
        embedmusic.set_author(name="Page 2")
        embedmusic.add_field(name="__**Music**__", value=music)     
        
        fun = fun.format(prefix=ctx.prefix)
        embedfun=discord.Embed(colour=0xFBCB03)
        embedfun.set_author(name="Page 3")
        embedfun.add_field(name="__**Fun 1/3**__", value=fun)
        
        fun2 = fun2.format(prefix=ctx.prefix)
        embedfun2=discord.Embed(colour=0xFBCB03)
        embedfun2.set_author(name="Page 4")
        embedfun2.add_field(name="__**Fun 2/3**__", value=fun2)
        
        fun3 = fun3.format(prefix=ctx.prefix)
        embedfun3=discord.Embed(colour=0xFBCB03)
        embedfun3.set_author(name="Page 5")
        embedfun3.add_field(name="__**Fun 3/3**__", value=fun3)
        
        mod = mod.format(prefix=ctx.prefix)
        embedmod=discord.Embed(colour=0x0000FF)
        embedmod.set_author(name="Page 6") 
        embedmod.add_field(name="__**Moderation**__", value=mod) 

        servermanagement = servermanagement.format(prefix=ctx.prefix)   
        embedservermanagement=discord.Embed(colour=0x73738A)
        embedservermanagement.set_author(name="Page 7")
        embedservermanagement.add_field(name="__**Server Management 1/2**__", value=servermanagement)
        
        servermanagement2 = servermanagement2.format(prefix=ctx.prefix)   
        embedservermanagement2=discord.Embed(colour=0x73738A)
        embedservermanagement2.set_author(name="Page 8")
        embedservermanagement2.add_field(name="__**Server Management 2/2**__", value=servermanagement2)
        
        economy = economy.format(prefix=ctx.prefix)   
        embedeconomy=discord.Embed(colour=0x080B3F)
        embedeconomy.set_author(name="Page 9")
        embedeconomy.add_field(name="__**Economy**__", value=economy)
        
        botinfo = botinfo.format(prefix=ctx.prefix)   
        embedbotinfo=discord.Embed(colour=0xAD00FF)
        embedbotinfo.set_author(name="Page 10")
        embedbotinfo.add_field(name="__**Bot Info**__", value=botinfo)
        
        help = help.format(prefix=ctx.prefix)
        embedhelp=discord.Embed(colour=0XFF0000)
        embedhelp.set_author(name="Page 11")
        embedhelp.add_field(name="__**Help**__", value=help)
        
        await self.bot.say(embed=ctx_message)
        await self.bot.whisper("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        await self.bot.whisper(embed=title)
        await self.bot.whisper(embed=embedgeneral)
        await self.bot.whisper(embed=embedmusic)
        await self.bot.whisper(embed=embedfun)
        await self.bot.whisper(embed=embedfun2)
        await self.bot.whisper(embed=embedfun3)
        await self.bot.whisper(embed=embedmod)
        await self.bot.whisper(embed=embedservermanagement)
        await self.bot.whisper(embed=embedservermanagement2)
        await self.bot.whisper(embed=embedeconomy)
        await self.bot.whisper(embed=embedbotinfo)
        await self.bot.whisper(embed=embedhelp)
        await self.bot.whisper("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        
        
    @commands.command(pass_context=True, name='moderation')
    async def _moderation(self, ctx):
    
        mod = """
**{prefix}ban :** Bans a user from the server.
**{prefix}softban :** Kicks a user, deleting 1 day worth of messages.
**{prefix}hackban :** Bans a user with their ID.
**{prefix}botclean :** Cleans all messages sent by bots & all it's triggers.
**{prefix}cleanup :** Cleans up messages.
**{prefix}prune :** Prunes messages, images, embeds etc..
**{prefix}editrole :** Edits role settings.
**{prefix}filter :** Filters/bans words from the server.
**{prefix}ignore :** Makes the bot ignore the server/channel.
**{prefix}unignore :** Unignores a channel/server.
**{prefix}kick :** kicks a user from the server.
**{prefix}mute :** Mutes a user from the server/channel.
**{prefix}unmute :** Unmutes a user from the server/channel.
**{prefix}modset :** Manages the server administration settings.
**{prefix}reason :** Edits a users case.
**{prefix}rename :** Changes a users nickname.
**{prefix}massmove :** Moves everyone for one channel to another.
**{prefix}move :** Moves users from a voice channel to another.
**{prefix}logs :** Logs past activity. """
        
        mod = mod.format(prefix=ctx.prefix)
        embed=discord.Embed(title="__Moderation__", colour=0xFF0000)
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.add_field(name="Commands:", value=mod)
        embed.set_author(name="Type {}help to see all the commands".format(ctx.prefix), icon_url=self.bot.user.avatar_url)
        await self.bot.say(embed=embed)
        
    @commands.command(pass_context=True, name='general')
    async def _general(self, ctx):  
    
        general = """
**{prefix}topservers :** Shows the top 10 most popular servers that Tarik's in.
**{prefix}google :** Search anything!
**{prefix}weather :** Check the weather of any location!
**{prefix}calculate :** Calculate a sum!
**{prefix}serverinfo :** Shows information about the server.
**{prefix}userinfo :** Shows information about a user.
**{prefix}avatar :** Shows a users avatar.
**{prefix}names :** Shows the list of a users past names/nicknames.
**{prefix}stopwatch :** Starts/stops a stopwatch. 
**{prefix}away :** Tell the bot if you're away or not.
**{prefix}translate :** Translates to any language.
**{prefix}roles :** Displays all the roles in the server.
**{prefix}role :** Displays all the users with a specific role and the amount. """

        general = general.format(prefix=ctx.prefix)
        embed=discord.Embed(title="__general__", colour=0xFF0000)
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.add_field(name="Commands:", value=general)
        embed.set_author(name="Type {}help to see all the commands".format(ctx.prefix), icon_url=self.bot.user.avatar_url)
        await self.bot.say(embed=embed)
        
    @commands.command(pass_context=True, name='economy')
    async def _economy(self, ctx):      
    
        economy = """
**{prefix}bank :** All the bank related things/settings.   
**{prefix}payday :** Daily free credits. 
**{prefix}balance :** Shows your/users current balance.
**{prefix}casino :** All the casino related things.
**{prefix}setcasino :** All the casino settings.
**{prefix}heist :** All heist related things.
**{prefix}setheist : ** All the heist settings.
**{prefix}economyset :** All the economy settings.
**{prefix}slot :** Bet your credits.
**{prefix}blackjack :** Bet your casino credits with blackjack.
**{prefix}allin :** Bet everything you have.
**{prefix}pay :** Pay a user. 
**{prefix}coin :** Bet on heads or tails.      
**{prefix}cups :** Pick the cup that is hiding the gold coin. Choose 1, 2, 3...
**{prefix}dice :** Roll 2, 7, 11 or 12 to win.
**{prefix}hilo :** Pick High, Low, Seven. Lo is < 7 Hi is > 7. 6x payout on 7.
**{prefix}war :** Modified War Card Game. """
        
        economy = economy.format(prefix=ctx.prefix)
        embed=discord.Embed(title="__Economy__", colour=0xFF0000)
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.add_field(name="Commands:", value=economy)
        embed.set_author(name="Type {}help to see all the commands".format(ctx.prefix), icon_url=self.bot.user.avatar_url)
        await self.bot.say(embed=embed)
        
    @commands.command(pass_context=True, name='cooltext')
    async def _cooltext(self, ctx): 

        cooltext = """
**{prefix}3dtext**           
**{prefix}3dtext1**          
**{prefix}3dtext2**            
**{prefix}3dtext3**          
**{prefix}3dtext4**     
**{prefix}art**            
**{prefix}ascii**           
**{prefix}bigtext**         
**{prefix}blocktext**   
**{prefix}graffiti**       
**{prefix}keytext**            
**{prefix}matrix**               
**{prefix}mirrortext**        
**{prefix}puffytext**       
**{prefix}slant**  
**{prefix}speedtext** """   

        cooltext = cooltext.format(prefix=ctx.prefix)
        embed=discord.Embed(title="__Cool Text__", colour=0xFF0000)
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.add_field(name="Cool text basically turns normal text into something cool!", value=cooltext)
        embed.set_author(name="Type {}help to see all the commands".format(ctx.prefix), icon_url=self.bot.user.avatar_url)
        await self.bot.say(embed=embed) 
        
    @commands.command(pass_context=True, name='music')
    async def _music(self, ctx):

        music = """
**{prefix}play :** Plays a link / searches and play.
**{prefix}song :** Info about the current song.
**{prefix}pause :** Pauses the current song, .resume to continue.
**{prefix}resume :** Resumes a paused song or playlist.
**{prefix}skip :** Skips a song, using the set threshold if the requester isn't.
**{prefix}stop :** Stops a currently playing song or playlist.
**{prefix}volume :** Sets the volume (0 - 100).
**{prefix}queue :** Shows the current queue.
**{prefix}disconnect :** Disconnects Tarik from the voice channel. """ 

        music = music.format(prefix=ctx.prefix)
        embed=discord.Embed(title="__Music Commands__", colour=0xFF0000)
        embed.set_thumbnail(url='https://cdn0.iconfinder.com/data/icons/huge-business-vector-icons/60/music_notes-512.png')
        embed.add_field(name="All the music commands!", value=music)
        embed.set_author(name="NOTE: MUSIC IS CURRENTLY DISABLED.".format(ctx.prefix), icon_url=self.bot.user.avatar_url)
        await self.bot.say(embed=embed)         
        
def setup(bot):
    bot.remove_command('help')
    bot.add_cog(Help(bot))