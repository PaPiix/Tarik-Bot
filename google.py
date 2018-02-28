import discord
from discord.ext import commands
from .utils.chat_formatting import *
import random
from random import randint
from random import choice as randchoice
import datetime
from __main__ import send_cmd_help
import re
import urllib
import time
import aiohttp
from .utils import checks
import asyncio
from cogs.utils.dataIO import dataIO
import io, os
from .utils.dataIO import fileIO
import logging

class SimplyGoogle:
    """A non sarcastic google command"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = "google", aliases=["g"], pass_context=True, no_pm=True, invoke_without_command=True)
    @commands.cooldown(5, 60, commands.BucketType.user)
    async def _google(self, ctx, text=None):
        """Its google, you search with it.
        Example: google A french pug
        Special search options are available; Image, Images, Maps
        Example: google image You know, for kids! > Returns first image"""
        
        search_type = ctx.message.content[len(ctx.prefix+ctx.command.name)+1:].lower().split(" ")
        option = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'}
        regex = [",\"ou\":\"([^`]*?)\"", "<h3 class=\"r\"><a href=\"\/url\?url=([^`]*?)&amp;", "<h3 class=\"r\"><a href=\"([^`]*?)\""]

        if text is None:
                embed=discord.Embed(title="Google", description="Google Anything!", colour=0x0000FF)
                embed.add_field(name="Example:", value=".google A french pug", inline=False)
                embed.add_field(name="Other Search Options:", value=".google images\n.google image\n.google maps\n.google videos", inline=True)
                embed.add_field(name="Example:", value=".google images Cat", inline=False)
                embed.set_thumbnail(url='http://www.broutinwebpublishing.com/wp-content/uploads/2016/11/google.png')
                embed.set_image(url='http://www.google.com/logos/doodles/2015/googles-new-logo-5078286822539264.3-hp2x.gif')
                await self.bot.say(embed=embed)
                return
        
        #Start of Image
        
        elif search_type[0] == "image":
            search_valid = str(ctx.message.content[len(ctx.prefix+ctx.command.name)+1:].lower())
            if search_valid == "image":
                await self.bot.say(" Please actually search something :/")
            else:
                uri = "https://www.google.com/search?tbm=isch&tbs=isz:m&q="
                quary = str(ctx.message.content[len(ctx.prefix+ctx.command.name)+7:].lower())
                encode = urllib.parse.quote_plus(quary,encoding='utf-8',errors='replace')
                uir = uri+encode

                async with aiohttp.get(uir, headers = option) as resp:
                    test = await resp.content.read()
                    unicoded = test.decode("unicode_escape")
                    query_find = re.findall(regex[0], unicoded)
                    try:
                        url = query_find[0]
                        await self.bot.say(url)
                    except IndexError:
                        await self.bot.say(":interrobang: Your search yielded no results.")
            #End of Image
        #Start of Image random
        elif search_type[0] == "images":
            search_valid = str(ctx.message.content[len(ctx.prefix+ctx.command.name)+1:].lower())
            if search_valid == "image":
                await self.bot.say(":neutralFace: Please ***actually search something*** :/")
            else:
                uri = "https://www.google.com/search?tbm=isch&tbs=isz:m&q="
                quary = str(ctx.message.content[len(ctx.prefix+ctx.command.name)+7:].lower())
                encode = urllib.parse.quote_plus(quary,encoding='utf-8',errors='replace')
                uir = uri+encode
                async with aiohttp.get(uir, headers = option) as resp:
                    test = await resp.content.read()
                    unicoded = test.decode("unicode_escape")
                    query_find = re.findall(regex[0], unicoded)
                    try:
                        url = query_find[0]
                        await self.bot.say(url)
                    except IndexError:
                        await self.bot.say(":interrobang: Your search yielded no results.")
            #End of Image random
        #Start of Maps
        elif search_type[0] == "maps":
            search_valid = str(ctx.message.content[len(ctx.prefix+ctx.command.name)+1:].lower())
            if search_valid == "maps":
                await self.bot.say(":neutralFace: Please ***actually search something*** :/")
            else:
                uri = "https://www.google.com/maps/search/"
                quary = str(ctx.message.content[len(ctx.prefix+ctx.command.name)+6:].lower())
                encode = urllib.parse.quote_plus(quary,encoding='utf-8',errors='replace')
                uir = uri+encode
                await self.bot.say(uir)
            #End of Maps
        #Start of generic search
        else:
            uri = "https://www.google.com/search?q="
            quary = str(ctx.message.content[len(ctx.prefix+ctx.command.name)+1:])
            encode = urllib.parse.quote_plus(quary,encoding='utf-8',errors='replace')
            uir = uri+encode
            async with aiohttp.get(uir, headers = option) as resp:
                test = str(await resp.content.read())
                query_find = re.findall(regex[1], test)
                if query_find == []:
                    query_find = re.findall(regex[2], test)
                    try:
                        if re.search("\/url?url=", query_find[0]) == True:
                            query_find = query_find[0]
                            m = re.search("\/url?url=", query_find)
                            query_find = query_find[:m.start()] + query_find[m.end():]
                            decode = self.unescape(query_find)
                            await self.bot.say("Here is your link: {}".format(decode))
                        else:
                            decode = self.unescape(query_find[0])
                            await self.bot.say("Here is your link: {}".format(decode))
                    except IndexError:
                        await self.bot.say("Your search yielded no results.")
                elif re.search("\/url?url=", query_find[0]) == True:
                    query_find = query_find[0]
                    m = re.search("\/url?url=", query_find)
                    query_find = query_find[:m.start()] + query_find[m.end():]
                    decode = self.unescape(query_find)
                    await self.bot.say("Here is your link: {}".format(decode))
                else:
                    query_find = query_find[0]
                    decode = self.unescape(query_find)
                    await self.bot.say("Here is your link: {} ".format(decode))
            #End of generic search

    def unescape(self, msg):
        regex = ["<br \/>", "(?:\\\\[rn])", "(?:\\\\['])", "%25", "\(", "\)"]
        subs = ["\n", "", "'", "%", "%28", "%29"]

        for i in range(len(regex)):
            sub = re.sub(regex[i], subs[i], msg)
            msg = sub
        return msg

def setup(bot):
    n = SimplyGoogle(bot)
    bot.add_cog(n)
