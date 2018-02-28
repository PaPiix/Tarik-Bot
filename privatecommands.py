import discord
from discord.ext import commands

class Privatecommands:
    """Private Commands for people!"""

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def apinity(self):
        """Apinity's Private Command."""

        embed=discord.Embed(title="__Apinity__", colour=0x007AFF)
        embed.set_thumbnail(url='https://images-ext-1.discordapp.net/.eJwFwQsOwiAMANC7cABKoV3XJcaz8DMuUUcANdF4d9_7mme_mc1c52xjA8jlYcs-8tFLbM3m4w7xFWfsA1A0oAZGUhYO4lcgVceKC7GkyiJKF4o-Cbq1-EWCfdfUzmP_1BM6T-b3B4a3IJs.qItRbgwNxxm4jXTLVFvZ2fAevA0?width=250&height=250')
        embed.add_field(name="YouTube", value="[Click Here]({})".format("https://www.youtube.com/user/Apinity"))
        embed.add_field(name="Instagram", value="[Click Here]({})".format("https://www.instagram.com/apinity1/"))
        embed.add_field(name="Twitter", value="[Click Here]({})".format("https://twitter.com/apinity"))
        embed.add_field(name="Twitch", value="[Click Here]({})".format("https://www.twitch.tv/imapinity"))
        embed.add_field(name="Snapchat", value="[Click Here]({})".format("https://www.snapchat.com/add/lucm8"))
        embed.add_field(name="Clan", value="[Click Here]({})".format("https://www.youtube.com/channel/UCpLNDpAc5N43NuxcvEJI_2A"))
        embed.set_image(url='http://i.imgur.com/5qDBEfi.jpg')
        embed.set_footer(text="#ROAD TO 50K!", icon_url='https://images-ext-1.discordapp.net/.eJwFwQsOwiAMANC7cABKoV3XJcaz8DMuUUcANdF4d9_7mme_mc1c52xjA8jlYcs-8tFLbM3m4w7xFWfsA1A0oAZGUhYO4lcgVceKC7GkyiJKF4o-Cbq1-EWCfdfUzmP_1BM6T-b3B4a3IJs.qItRbgwNxxm4jXTLVFvZ2fAevA0?width=250&height=250')
        await self.bot.say(embed=embed)
        
    @commands.command()
    async def mistik(self):
        """Mistik's Private Command."""
        embed=discord.Embed(title="__Mistik__", colour=0x000AFF)
        embed.set_thumbnail(url='https://images-ext-1.discordapp.net/.eJwNyFEOwiAMANC7cABooTBYYjxLR1lcoo4A08TFu-v7fKc62l3N6jZG7bMxWZ5atp73JlyrzvvD8IsHt24QYkiOEpADAusDGEr4L2BXPMZJcFolBRKGlXyMaPW7LPXat0-5IFhS3x-NLyDZ.NrYXGnm8-GUTyXsMzpPo3o069q4')        
        embed.add_field(name="Discord", value="[Click Here]({})".format("https://discord.gg/UrjzTXd"))
        embed.add_field(name="YouTube", value="[Click Here]({})".format("https://www.youtube.com/channel/UCwafGcuGGypkqpV7eZdmlSw"))
        embed.add_field(name="Snapchat", value="[Click Here]({})".format("https://www.snapchat.com/add/MistikNBK"))
        embed.add_field(name="Twitter", value="[Click Here]({})".format("https://twitter.com/mistikyoutube"))
        embed.add_field(name="Instagram", value="[Click Here]({})".format("https://www.instagram.com/mistikyoutube/"))
        embed.add_field(name="Private Server", value="[Click Here]({})".format("http://nbk.io/"))
        embed.add_field(name="Clan Channel", value="[Click Here]({})".format("https://www.youtube.com/channel/UCSD5xFQY8qZPaLCMMCh8TQw"))
        embed.set_image(url='https://i.gyazo.com/ed6965b6220ccbdce3ffff83d3039ef2.gif')
        embed.set_footer(text="Leader of NBK Clan!", icon_url='https://images-ext-1.discordapp.net/.eJwNyFEOwiAMANC7cABooTBYYjxLR1lcoo4A08TFu-v7fKc62l3N6jZG7bMxWZ5atp73JlyrzvvD8IsHt24QYkiOEpADAusDGEr4L2BXPMZJcFolBRKGlXyMaPW7LPXat0-5IFhS3x-NLyDZ.NrYXGnm8-GUTyXsMzpPo3o069q4')
        await self.bot.say(embed=embed)
      
    @commands.command()
    async def slash(self):
        """Slash's Private Command."""
        embed=discord.Embed(title="__Slash__", colour=0x0048DF)
        embed.set_thumbnail(url='https://images-ext-2.discordapp.net/.eJwFwQEKwyAMAMC_-AA1rYlaGHtLNJYVtlXUbrDSv-_uVEd7qkU9xqh9MSbLW8vW896Ea9V5fxn-8ODWDaAPiLO1EANGIrAG5wkwOFlTdt5ziEiE6NhDkrRS0d-S6r1vv3IDOzl1_QGdtiF6.f7Gq3_C3HHj225CfzzfwGs1iCtQ?width=250&height=250')
        embed.add_field(name="YouTube", value="[Click Here]({})".format("https://www.youtube.com/channel/UCFE359CTDRwda3r0zgd716A"))
        embed.add_field(name="Instagram", value="[Click Here]({})".format("https://www.instagram.com/tyt_slash/"))
        embed.add_field(name="Twitter", value="[Click Here]({})".format("https://twitter.com/Slash_YouTube"))
        embed.add_field(name="Snapchat", value="[Click Here]({})".format("http://www.snapchat.com/add/slashgaming"))
        embed.add_field(name="Google +", value="[Click Here]({})".format("https://plus.google.com/+SlashGamingg"))
        embed.add_field(name="Website", value="[Click Here]({})".format("http://www.slashplays.com"))
        embed.set_image(url='https://media.giphy.com/media/26gR1LTtRLiw1BCLu/giphy.gif')
        embed.set_footer(text="#ROAD TO 200K!", icon_url='https://images-ext-2.discordapp.net/.eJwFwQEKwyAMAMC_-AA1rYlaGHtLNJYVtlXUbrDSv-_uVEd7qkU9xqh9MSbLW8vW896Ea9V5fxn-8ODWDaAPiLO1EANGIrAG5wkwOFlTdt5ziEiE6NhDkrRS0d-S6r1vv3IDOzl1_QGdtiF6.f7Gq3_C3HHj225CfzzfwGs1iCtQ?width=250&height=250')
        await self.bot.say(embed=embed)
    
    @commands.command()
    async def alexia(self):
        """Alexia's Private Command."""
        embed=discord.Embed(description="Alexia,  https://www.youtube.com/channel/UCC1G7u6cXWl6RKtbzoc5pXw, Hello my Name Is Alexia. I love being crazy and weird. I love and hate my Senpai. I love my family and friends. :kissing_heart::kissing_heart::kissing_heart::kissing_heart:", colour=0xFFFF00)      
        embed.set_author(name="Alexia", icon_url='https://images-ext-1.discordapp.net/.eJwFwW0OwiAMANC7cABooYNuidlRTOVDSdQRQH9ovLvvfdWr39WmbnO2sRkT01OnOuLRk7Sm4_Ew8pYpfRjrAoGjlQMFAMtMRs4Cay4-LRdkpBJzcYIo4tB6YO8Xfa1lH_WTTwiW1O8P2Uoh2A.xPYOJOIW76AY7Psgh7r2a4PplHk')
        embed.set_thumbnail(url='https://images-ext-1.discordapp.net/.eJwFwW0OwiAMANC7cABooYNuidlRTOVDSdQRQH9ovLvvfdWr39WmbnO2sRkT01OnOuLRk7Sm4_Ew8pYpfRjrAoGjlQMFAMtMRs4Cay4-LRdkpBJzcYIo4tB6YO8Xfa1lH_WTTwiW1O8P2Uoh2A.xPYOJOIW76AY7Psgh7r2a4PplHk')
        await self.bot.say(embed=embed)
        
    @commands.command()
    async def plex(self):
        """Plex's Private Command."""
        desc = """
I'm just a programmer with a dream to be as good as _qlow.
Ene mene muh, @'Steve#7740 ist eine Kuh"
MC Server IP: Play.BuzzCraft.net | 1.8.x - 1.9.x """
        embed=discord.Embed(description=desc, colour=0x32CD32)      
        embed.set_author(name="zPlex", icon_url='https://www.spigotmc.org/data/avatars/l/197/197093.jpg?1486902164')
        embed.add_field(name="Website", value="[Click Here]({})".format("http://www.buzzcraft.net/"))
        embed.add_field(name="Store", value="[Click Here]({})".format("http://buy.buzzcraft.net/"))
        embed.add_field(name="Discord Server", value="[Click Here]({})".format("https://discord.gg/fmzSsGs"))
        embed.add_field(name="Spigot", value="[Click Here]({})".format("https://www.spigotmc.org/members/zplex.197093/"))
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/318107267708747776/318396520137228288/BuzzCraft_Logo.png')
        embed.set_image(url='https://cdn.discordapp.com/attachments/318107267708747776/318396553553379328/BuzzCraft.gif')
        await self.bot.say(embed=embed) 
        
def setup(bot):
    bot.add_cog(Privatecommands(bot))      