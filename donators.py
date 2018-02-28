import discord
from discord.ext import commands

class Donators:
    """Donators!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def donators(self, ctx):
        """Lists all Donators"""
        
        embed=discord.Embed(title="Donators!", colour=0xFF0000)
        embed.set_thumbnail(url='http://kingofwallpapers.com/dollar-sign/dollar-sign-003.jpg')
        embed.add_field(name="__Chaos__", value="Command: **{}chaos**\n\nTotal Donation: **$5.00**.".format(ctx.prefix))
        embed.add_field(name="__Lexia__", value="Command: **None**\n\nTotal Donation: **$5.00**.")
        embed.add_field(name="__Saki__", value="Command: **{}saki**\n\nTotal Donation: **$10.00**.".format(ctx.prefix))
        embed.add_field(name="__Playnight__", value="Command: **{}primenight**\n\nTotal Donation: **$7.50**.".format(ctx.prefix))
        embed.add_field(name="__Desolation__", value="Command: **{}desolation**\n\nTotal Donation: **$7.50**.".format(ctx.prefix))
        embed.add_field(name="__Neon__", value="Command: **{}neon**\n\nTotal Donation: **$7.50**.".format(ctx.prefix))      
        embed.set_footer(text="Thank you guys for donating ❤ Type {}donate , if you would like to donate!".format(ctx.prefix), icon_url='http://www.printable-alphabets.com/wp-content/uploads/2012/12/print-dollar-sign-large.png')
        await self.bot.say(embed=embed)
    
    @commands.command()
    async def chaos(self):
        """Chaos's Private Command!"""

        ytchannel = "https://www.youtube.com/channel/UCnRw494K2n2mPOGUtXPk7sQ"
        clanchannel = "https://www.youtube.com/channel/UCM2Eju6yBiKxCI1htmNF3tw"
        discordlink = "https://discord.gg/mTP5Tj4"
        
        embed=discord.Embed(title="__༄㋱⇀Chaos__", colour=0xFF0000)
        embed.set_thumbnail(url='https://images-ext-2.discordapp.net/.eJwFwQsKAiEQANC7eAAddWSchegs448WqhV1C4ru3ntfdY672tRtrT43Y3J56rLPfIwivet8PIy8ZMmYxllgy94TBx-DRwQDDiQ1i9QIWUKrQja6WFKKLVFh_a6pX-f-qRcLDtXvD7FsIgA.vQt15UPNbrK4hgTdsny8e31PBA8')
        embed.add_field(name="YouTube", value="[Click Here]({})".format(ytchannel))
        embed.add_field(name="Clan Channel", value="[Click Here]({})".format(clanchannel))
        embed.add_field(name="Discord", value="[Click Here]({})".format(discordlink))
        embed.set_footer(text="Total Donation: $5.00!", icon_url='https://images-ext-2.discordapp.net/.eJwFwQsKAiEQANC7eAAddWSchegs448WqhV1C4ru3ntfdY672tRtrT43Y3J56rLPfIwivet8PIy8ZMmYxllgy94TBx-DRwQDDiQ1i9QIWUKrQja6WFKKLVFh_a6pX-f-qRcLDtXvD7FsIgA.vQt15UPNbrK4hgTdsny8e31PBA8')
        embed.set_image(url='http://i.imgur.com/KoBKBqf.gif')
        await self.bot.say(embed=embed)
        
    @commands.command()
    async def saki(self):
        """Saki's Private Command"""

        embed=discord.Embed(title="__Saki__", colour=0x050000)
        embed.set_thumbnail(url='https://images-ext-2.discordapp.net/.eJwFwQsOwiAMANC7cACg7XDtEuNZyse4RB0BponL7u57h9nb0yzmMUbti3Mpv21ee9pa1lpt2l5OPzq0dYdACD74IIRMOM_eFSUMkOkeY-KJLsKaMgN5EQLhYr8l1ltff-UKHidz_gGmMSFi.4xKuEXmsRxaktexjGgN0RX6TpKw')    
        embed.add_field(name="A mysterious man ,he came from space to save people with electronic music.", value="[Subscribe Here]({})".format("https://m.youtube.com/channel/UCqwgJRxBjFeVdaHR7rcqY9w"))
        embed.add_field(name="Facebook Page", value="[Click Here]({})".format("https://m.facebook.com/SakiAshe-Productions-829766853816810/"))
        embed.add_field(name="Discord", value="[Click Here]({})".format("https://discord.gg/3dppnbc"))
        embed.set_footer(text="Total Donation: $10.00!", icon_url='https://images-ext-2.discordapp.net/.eJwFwQsOwiAMANC7cACg7XDtEuNZyse4RB0BponL7u57h9nb0yzmMUbti3Mpv21ee9pa1lpt2l5OPzq0dYdACD74IIRMOM_eFSUMkOkeY-KJLsKaMgN5EQLhYr8l1ltff-UKHidz_gGmMSFi.4xKuEXmsRxaktexjGgN0RX6TpKw') 
        embed.set_image(url='http://i.imgur.com/0flmjM4.gif')
        await self.bot.say(embed=embed)  
    
    @commands.command()
    async def primenight(self):
        """Playnight's Private Command."""
        
        embed=discord.Embed(title="__Prime Night__", colour=0xFFB800)
        embed.add_field(name="Discord", value="[Click Here]({})".format("https://discord.gg/PsnyWbK"))
        embed.add_field(name="Facebook", value="[Click Here]({})".format("https://www.facebook.com/PrimeNight-Community-673188139527290/"))
        embed.add_field(name="Twitch Community", value="[Click Here]({})".format("https://www.twitch.tv/communities/PrimeNight-Community"))
        embed.add_field(name="Twitter", value="[Click Here]({})".format("https://twitter.com/PrimeNightTV"))
        embed.add_field(name="Instagram", value="[Click Here]({})".format("https://www.instagram.com/primenighttv/?hl=de"))
        embed.add_field(name="Website", value="[Click Here]({})".format("http://www.primenight-community.com"))
        embed.set_thumbnail(url='https://images-ext-1.discordapp.net/.eJwFwVEOwiAMANC7cABooR1zidlRDBSmJOoIoB8uu7vvHerTnmpRjzFqX4yR9NapdNlbCrVq2V8mfMMIrRtLDmGi2TFMjDh7a8KNyUZC9pnoEnFLjgVyyg4jRRD0-l62tZdfviJYUucfx-4hxg.D46qZN_Et1jzi1CqdkksarikE90')
        embed.set_footer(text="Don't forget to check us out ;)", icon_url='https://images-ext-1.discordapp.net/.eJwFwVEOwiAMANC7cABooR1zidlRDBSmJOoIoB8uu7vvHerTnmpRjzFqX4yR9NapdNlbCrVq2V8mfMMIrRtLDmGi2TFMjDh7a8KNyUZC9pnoEnFLjgVyyg4jRRD0-l62tZdfviJYUucfx-4hxg.D46qZN_Et1jzi1CqdkksarikE90')
        embed.set_image(url='https://cdn.discordapp.com/attachments/290496668581888010/290504304530423808/verkleinert.png')
        await self.bot.say(embed=embed)   
        
    @commands.command()
    async def desolation(self):
        """Desolation's Private Commands."""
        
        steam1 = "http://steamcommunity.com/id/DeliciousFries/"
        steam2 = "http://steamcommunity.com/id/DeliciousFriesV2"
        
        embed=discord.Embed(title="__Desolation__", colour=0xFF00FF)
        embed.add_field(name="Snapchat", value="[Click Here]({})".format("https://www.snapchat.com/add/DesolationDG"))
        embed.add_field(name="YouTube", value="[Click Here]({})".format("https://www.youtube.com/channel/UCqO_3pe34ItRD9hfKksWjpg"))
        embed.add_field(name="Reddit", value="[Click Here]({})".format("https://www.reddit.com/user/DG-Wolf/"))
        embed.add_field(name="Instagram", value="[Click Here]({})".format("https://www.instagram.com/george_btte_18/"))
        embed.add_field(name="Steam", value="[Main Account]({})\n\n[Second Account]({})".format(steam1, steam2))
        embed.set_thumbnail(url='https://images-ext-1.discordapp.net/.eJwNylEOwiAMANC7cADKCqVjifEsXcG4RB0BponGu-v7fh9ztJtZzHWM2hcAzQ-bt657y1Kr1f0O8pQhrQNiDJzYBfIxOWaOcPGsk0MinZFU1GOe3Fwc5bBKTGhfZa3nvr3L6d-C-f4Ao00hZw.dMIEYqiUvtdfFSmdWJBbQTARGXU')
        embed.set_footer(text="Total Donation: $7.50!", icon_url='https://images-ext-1.discordapp.net/.eJwNylEOwiAMANC7cADKCqVjifEsXcG4RB0BponGu-v7fh9ztJtZzHWM2hcAzQ-bt657y1Kr1f0O8pQhrQNiDJzYBfIxOWaOcPGsk0MinZFU1GOe3Fwc5bBKTGhfZa3nvr3L6d-C-f4Ao00hZw.dMIEYqiUvtdfFSmdWJBbQTARGXU')
        embed.set_image(url='http://i.imgur.com/B7YhiCG.gif')
        await self.bot.say(embed=embed)     
        
    @commands.command()
    async def neon(self):
        """Neon's Private Commands."""
     
        embed=discord.Embed(title="__Neon__", colour=0xC0C0C0)
        embed.add_field(name="Server", value="[Click Here]({})".format("https://discord.gg/t46DrUH"))
        embed.add_field(name="Github Server", value="[Click Here]({})".format("https://discord.gg/gxG4kRf"))
        embed.add_field(name="Github", value="[Click Here]({})".format("https://davidneon.github.io/info/"))
        embed.set_thumbnail(url='https://images-ext-1.discordapp.net/.eJwNwQsKwjAMANC79AD9Z0sG4lnSpsOButJWhQ3vru-d6tXualG3MWpfjMny1LL1vDfhWnXeH4bfPLh1450joDjFPwAKkzVIcfYJxYYVhQJB8ugJQp7XgmBZf0qq174d5eKsj-r7A5f1ISk.WBgLiHyc4vcUlmRmuzurp2KQzKA')
        embed.set_footer(text="Total Donation: $7.50!", icon_url='https://images-ext-1.discordapp.net/.eJwNwQsKwjAMANC79AD9Z0sG4lnSpsOButJWhQ3vru-d6tXualG3MWpfjMny1LL1vDfhWnXeH4bfPLh1450joDjFPwAKkzVIcfYJxYYVhQJB8ugJQp7XgmBZf0qq174d5eKsj-r7A5f1ISk.WBgLiHyc4vcUlmRmuzurp2KQzKA')
        embed.set_image(url='https://cdn.discordapp.com/attachments/288031461540626432/293090675191185408/wut.png')
        await self.bot.say(embed=embed)
        
def setup(bot):
    bot.add_cog(Donators(bot))