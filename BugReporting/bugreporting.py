import discord
import os
from discord.ext import commands
from cogs.utils import checks
from discord import Object
from cogs.utils.dataIO import dataIO
from __main__ import settings
from random import randint
from random import choice

# This is a feature I released for my bot in the past. I decided to share my code with you guys since I disabled it due to abuse.

class Bugreporting:
    """Bug reporting for Tarik."""
    def __init__(self, bot):
        self.bot = bot
        self.file_path = "data/bug/bugchannels.json"
        self.json_data = dataIO.load_json(self.file_path)


    @checks.is_owner()
    @commands.command(pass_context=True)
    async def reportchannel(self, ctx, channel : discord.Channel):
            self.json_data["channel"] = channel.id
            dataIO.save_json(self.file_path, self.json_data)
            em = discord.Embed(colour=0xFF0000)
            em.set_author(name="Channel set!")
            await self.bot.say(embed=em)

    @commands.command(pass_context=True, no_pm=True)
    async def report(self, ctx, *, text):
        """Allows to report a bug to Tarik's developer, abuse will get you blacklisted. Please use appropriately"""
        try:
            channel = self.bot.get_channel(self.json_data["channel"])
            colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
            colour = int(colour, 16)
            server = ctx.message.server
            author = ctx.message.author
            embed = discord.Embed(description=text, colour=discord.Colour(value=colour))
            embed.set_author(name="A report from {}".format(server.name), icon_url=author.avatar_url)
            embed.set_footer(text="Reported by {} ({})".format(author.name, author.id), icon_url=author.avatar_url)
            embed.set_thumbnail(url=ctx.message.server.icon_url)
            #embed.add_field(name="Server Name", value=server.name)
            #embed.add_field(name="Server ID", value=server.id)
            #embed.add_field(name="Server Members", value=server.members)
            await self.bot.send_message(channel, embed=embed)
            await self.bot.say("Successfully reported :ok_hand:")          
        except:
            raise
            #await self.bot.say("You have not set a channel.")

def check_folders():
    if not os.path.exists("data/bug"):
        print("Creating data/bug folder...")
        os.makedirs("data/bug")

def check_files():
    system = {}
    f = "data/bug/bugchannels.json"
    if not dataIO.is_valid_json(f):
        print("Creating default bugchannels.json...")
        dataIO.save_json(f, system)

def setup(bot):
    check_folders()
    check_files()
    n = Bugreporting(bot)
    bot.add_cog(n)
