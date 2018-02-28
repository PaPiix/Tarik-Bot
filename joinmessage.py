import time
import discord
from discord.ext import commands
from .utils.chat_formatting import *
from random import randint
from random import choice as randchoice
import asyncio

class Joinmessage:
    def __init__(self, bot):
        self.bot = bot

    async def on_server_join(self, server):
        channel = server.default_channel
        users = str(len(set(self.bot.get_all_members())))
        servers = len(self.bot.servers)
        sinv = "http://www.tarikbot.com"
        inv ="https://discordapp.com/oauth2/authorize?client_id=263080353680457728&scope=bot&permissions=2146958463"
        oserver ="https://discord.gg/5E7hrVk"
        msg = "__Hello, my name is Tarik! Thank you for inviting me to {}__.\n**I am a multi-functional bot with hundreds of commands! I'm based off of Red and coded in python! \n\n :warning: **Here are some features:** :warning: : \n :black_medium_small_square:  **Music** (Currently Disabled)\n :black_medium_small_square:  **Moderation**\n :black_medium_small_square: **Fun**\n :black_medium_small_square: **Banking system**\n :black_medium_small_square: **Shop system**\n :black_medium_small_square: **Custom server commands**\n :black_medium_small_square: **Server Prefix\n\nType `.help` to see the commands.".format(server.name)
        em = discord.Embed(description=msg, colour=0xEC2323, timestamp=__import__('datetime').datetime.utcnow())
        if self.bot.user.avatar_url:
            em.set_author(name="", url=self.bot.user.avatar_url)
            em.set_footer(text="Currently supporting {} servers and {} users.".format(servers, users), icon_url=self.bot.user.avatar_url)
            em.add_field(name="Invite", value="[Click Here]({})".format(inv))
            em.add_field(name="Website", value="[Click Here]({})".format(sinv))
            em.add_field(name="Owner", value="**-** TTxFTW")
            em.add_field(name="Official Server", value="[Click Here]({})".format(oserver))
            em.add_field(name="Devs", value="**-** Nino\n**-** ImBursting\n**-** FwiedWice")
            em.set_thumbnail(url=self.bot.user.avatar_url)
            em.set_image(url=self.bot.user.avatar_url)        
        await self.bot.send_message(server, embed=em)

def setup(bot):
    n = Joinmessage(bot)
    bot.add_cog(n)