import discord
from discord.ext import commands
from cogs.utils.dataIO import dataIO
from .utils import checks
from __main__ import send_cmd_help
# Sys
from bs4 import BeautifulSoup
import random
from random import randint
from random import choice
from random import choice as randchoice
import asyncio
import aiohttp
import time
import random
import os
import sys

DIR_DATA = "data/oboobs"
SETTINGS = DIR_DATA+"/settings.json"
DEFAULT = {"nsfw_channels": ["281499423559909376"], "invert" : False, "nsfw_msg": True, "last_update": 0,  "ama_boobs": 10548, "ama_ass": 4542}# Red's testing chan. nsfw content off by default.

#API info:
#example: "/boobs/10/20/rank/" - get 20 boobs elements, start from 10th ordered by rank; noise: "/noise/{count=1; sql limit}/",
#example: "/noise/50/" - get 50 random noise elements; model search: "/boobs/model/{model; sql ilike}/",
#example: "/boobs/model/something/" - get all boobs elements, where model name contains "something", ordered by id; author search: "/boobs/author/{author; sql ilike}/",
#example: "/boobs/author/something/" - get all boobs elements, where author name contains "something", ordered by id; get boobs by id: "/boobs/get/{id=0}/",
#example: "/boobs/get/6202/" - get boobs element with id 6202; get boobs count: "/boobs/count/"; get noise count: "/noise/count/"; vote for boobs: "/boobs/vote/{id=0}/{operation=plus;[plus,minus]}/",
#example: "/boobs/vote/6202/minus/" - negative vote for boobs with id 6202; vote for noise: "/noise/vote/{id=0}/{operation=plus;[plus,minus]}/",
#example: "/noise/vote/57/minus/" - negative vote for noise with id 57;

#example: "/butts/10/20/rank/" - get 20 butts elements, start from 10th ordered by rank; noise: "/noise/{count=1; sql limit}/",
#example: "/noise/50/" - get 50 random noise elements; model search: "/butts/model/{model; sql ilike}/",
#example: "/butts/model/something/" - get all butts elements, where model name contains "something", ordered by id; author search: "/butts/author/{author; sql ilike}/",
#example: "/butts/author/something/" - get all butts elements, where author name contains "something", ordered by id; get butts by id: "/butts/get/{id=0}/",
#example: "/butts/get/6202/" - get butts element with id 6202; get butts count: "/butts/count/"; get noise count: "/noise/count/"; vote for butts: "/butts/vote/{id=0}/{operation=plus;[plus,minus]}/",
#example: "/butts/vote/6202/minus/" - negative vote for butts with id 6202; vote for noise: "/noise/vote/{id=0}/{operation=plus;[plus,minus]}/",
#example: "/noise/vote/57/minus/" - negative vote for noise with id 57;

class nsfw:
    """
    
    Author: !TTxFTW
    
    """

    def __init__(self, bot):
        self.bot = bot
        self.settings = dataIO.load_json(SETTINGS)

    @commands.group(name="nsfw", pass_context=True)
    async def _nsfw(self, ctx):
        """NSFW settings."""
        if ctx.invoked_subcommand is None:
            embed=discord.Embed(colour=0xFF0000)
            embed.set_author(name="NSFW", icon_url=self.bot.user.avatar_url)
            embed.set_thumbnail(url=self.bot.user.avatar_url)
            embed.set_image(url='https://trending305.files.wordpress.com/2014/07/hot-ass-sexy-butt-pics-20.jpg')
            embed.add_field(name="Commands:", value="**{}nsfw toggle** - Toggles NSFW for the current channel.\n\n**{}boobs** - Displays random images of boobs.\n\n**{}ass** - Displays random images off ass.\n\n**{}yandere** - Displays random images from Yandere.\n\n**{}konachan** - Displays random images from Konachan.\n\n**{}e621** - Displays random images from e621.\n\n**{}rule34** - Displays random images from rule34.\n\n**{}danbooru** - Displays random images from Danooru.\n\n**{}gelbooru** - Displays random images from Gelbooru.\n\n**{}tbib** - Displays random images from The Big ImageBoard.\n\n**{}xbooru** - Displays random images from Xbooru.\n\n**{}furrybooru** - Displays random images from Furrybooru.\n\n**{}drunkenpumken** - Displays random images from DrunkenPumken.\n\n**{}lolibooru** - Displays random images from Lolibooru. (Disabled due to Discord's ToS.)\n\n**{}ysearch** - Searches Yandere with a tag.".format(ctx.prefix, ctx.prefix, ctx.prefix, ctx.prefix, ctx.prefix, ctx.prefix, ctx.prefix, ctx.prefix, ctx.prefix, ctx.prefix, ctx.prefix, ctx.prefix, ctx.prefix, ctx.prefix, ctx.prefix))
            #embed.add_field(name="Info:", value="```This command was made by TTxFTW as a 1000 server celebration. This command uses the http://oboobs.ru/ API to randomly generate NSFW images. There are 2 types: Ass and Boobs. NSFW can be toggled using {}nsfw toggle.```".format(ctx.prefix))
            embed.set_footer(text="1K special command.", icon_url=self.bot.user.avatar_url)
            await self.bot.say(embed=embed)
            #await send_cmd_help(ctx)
            return

    # Boobs
    @commands.command(pass_context=True, no_pm=False)
    async def boobs(self, ctx):
        """Shows some boobs."""
        author = ctx.message.author
        dis_nsfw = None
        for a in self.settings["nsfw_channels"]:
            if a == ctx.message.channel.id:
                if self.settings["invert"]:
                    dis_nsfw = False
                else:
                    dis_nsfw = True
                break
        if dis_nsfw is None and not self.settings["invert"]:
            dis_nsfw = False
        else:
            dis_nsfw = True

        try:
            rdm = random.randint(0, self.settings["ama_boobs"])
            search = ("http://api.oboobs.ru/boobs/{}".format(rdm))
            async with aiohttp.get(search) as r:
                result = await r.json()
                boob = random.choice(result)
                boob = "http://media.oboobs.ru/{}".format(boob["preview"])
        except Exception as e:
            await self.bot.reply("Error getting results.")
            return
        if not dis_nsfw:
            colour = ''.join([randchoice('0123456789ABCDEF') for x in range(6)])
            colour = int(colour, 16)
            embed=discord.Embed(colour=discord.Colour(value=colour))
            embed.set_image(url=boob)
            embed.set_author(name="Boobs", url=boob, icon_url=self.bot.user.avatar_url)
            await self.bot.say(embed=embed)
            #await self.bot.say("{}".format(boob))
        else:
            pass
            #embed=discord.Embed(colour=discord.Colour(value=colour))
            #embed.set_image(url=boob)
            #embed.set_author(name="Boobs", url=boob)
            #await self.bot.send_message(ctx.message.author, embed=embed)
            #await self.bot.send_message(ctx.message.author, "{}".format(boob))
            #if self.settings["nsfw_msg"]:
                #await self.bot.reply("nsfw content is not allowed in this channel, instead I have send you a DM.")

    # Ass
    @commands.command(pass_context=True, no_pm=False)
    async def ass(self, ctx):
        """Shows some ass."""
        author = ctx.message.author
        dis_nsfw = None
        for a in self.settings["nsfw_channels"]:
            if a == ctx.message.channel.id:
                if self.settings["invert"]:
                    dis_nsfw = False
                else:
                    dis_nsfw = True
                break
        if dis_nsfw is None and not self.settings["invert"]:
            dis_nsfw = False
        else:
            dis_nsfw = True

        try:
            rdm = random.randint(0, self.settings["ama_ass"])
            search = ("http://api.obutts.ru/butts/{}".format(rdm))
            async with aiohttp.get(search) as r:
                result = await r.json()
                ass = random.choice(result)
                ass = "http://media.obutts.ru/{}".format(ass["preview"])
        except Exception as e:
            await self.bot.reply("Error getting results.")
            return
        if not dis_nsfw:
            colour = ''.join([randchoice('0123456789ABCDEF') for x in range(6)])
            colour = int(colour, 16)
            embed=discord.Embed(colour=discord.Colour(value=colour))
            embed.set_image(url=ass)
            embed.set_author(name="Ass", url=ass, icon_url=self.bot.user.avatar_url)
            await self.bot.say(embed=embed)
            #await self.bot.say("{}".format(ass))
        else:
            pass
            #embed=discord.Embed(colour=discord.Colour(value=colour))
            #embed.set_image(url=ass)
            #embed.set_author(name="Ass", url=ass)
            #await self.bot.send_message(ctx.message.author, embed=embed)
            #if self.settings["nsfw_msg"]:
                #await self.bot.reply("nsfw content is not allowed in this channel, instead I have send you a DM.")

    @checks.admin_or_permissions(manage_server=True)
    @_nsfw.command(pass_context=True, no_pm=True)
    async def toggle(self, ctx):
        """Toggle nsfw for this channel on/off.
        Admin/owner restricted."""
        nsfwChan = None
        # Reset nsfw.
        for a in self.settings["nsfw_channels"]:
            if a == ctx.message.channel.id:
                nsfwChan = True
                self.settings["nsfw_channels"].remove(a)               
                embed=discord.Embed(colour=0xFF0000)
                embed.set_author(name="NSFW has been enabled.", icon_url=self.bot.user.avatar_url)
                await self.bot.say(embed=embed)
                #await self.bot.reply("nsfw ON")
                break
        # Set nsfw.
        if not nsfwChan:
            if ctx.message.channel not in self.settings["nsfw_channels"]:
                self.settings["nsfw_channels"].append(ctx.message.channel.id)
                embed=discord.Embed(colour=0xFF0000)
                embed.set_author(name="NSFW has been disabled.", icon_url=self.bot.user.avatar_url)
                await self.bot.say(embed=embed)
                #await self.bot.reply("nsfw OFF")
        dataIO.save_json(SETTINGS, self.settings)
        
    #@checks.admin_or_permissions(manage_server=True)
    #@_nsfw.command(pass_context=True, no_pm=True)
    #async def invert(self, ctx):
        #"""Invert nsfw blacklist to whitlist
       # Admin/owner restricted."""
        #if not self.settings["invert"]:
            #self.settings["invert"] = True
            #await self.bot.reply("The nsfw list for all servers is now: inverted.")
        #elif self.settings["invert"]:
            #self.settings["invert"] = False
            #await self.bot.reply("The nsfw list for all servers is now: default(blacklist)")
        #dataIO.save_json(SETTINGS, self.settings)    

    #@checks.admin_or_permissions(manage_server=True)
    #@_nsfw.command(pass_context=True, no_pm=True)
    #async def togglemsg(self, ctx):
        #"""Enable/Disable the oboobs nswf not allowed message
        #Admin/owner restricted."""
        # Toggle
        #if self.settings["nsfw_msg"]:
            #self.settings["nsfw_msg"] = False
            #await self.bot.replay("DM nsfw channel msg is now: Disabled.`")
        #elif not self.settings["nsfw_msg"]:
            #self.settings["nsfw_msg"] = True
            #await self.bot.reply("DM nsfw channel msg is now: Enabled.")
        #dataIO.save_json(SETTINGS, self.settings)

    @commands.command(pass_context=True, no_pm=False)
    async def yandere(self, ctx):
        """Random Image From Yandere"""
        dis_nsfw = None
        for a in self.settings["nsfw_channels"]:
            if a == ctx.message.channel.id:
                if self.settings["invert"]:
                    dis_nsfw = False
                else:
                    dis_nsfw = True
                break
        if dis_nsfw is None and not self.settings["invert"]:
            dis_nsfw = False
        else:
            dis_nsfw = True
            return
        try:
            query = ("https://yande.re/post/random")
            page = await aiohttp.get(query)
            page = await page.text()
            soup = BeautifulSoup(page, 'html.parser')
            image = soup.find(id="highres").get("href")
            colour = ''.join([randchoice('0123456789ABCDEF') for x in range(6)])
            colour = int(colour, 16)
            embed=discord.Embed(colour=discord.Colour(value=colour))
            embed.set_image(url=image)
            embed.set_author(name="Yandere", url=image, icon_url=self.bot.user.avatar_url)
            await self.bot.say(embed=embed)
        except Exception as e:
            await self.bot.say(":x: **Error:** `{}`".format(e))

    @commands.command(pass_context=True, no_pm=False)
    async def konachan(self, ctx):
        """Random Image From Konachan"""
        dis_nsfw = None
        for a in self.settings["nsfw_channels"]:
            if a == ctx.message.channel.id:
                if self.settings["invert"]:
                    dis_nsfw = False
                else:
                    dis_nsfw = True
                break
        if dis_nsfw is None and not self.settings["invert"]:
            dis_nsfw = False
        else:
            dis_nsfw = True
            return
        try:
            query = ("https://konachan.com/post/random")
            page = await aiohttp.get(query)
            page = await page.text()
            soup = BeautifulSoup(page, 'html.parser')
            image = soup.find(id="highres").get("href")
            colour = ''.join([randchoice('0123456789ABCDEF') for x in range(6)])
            colour = int(colour, 16)
            embed=discord.Embed(colour=discord.Colour(value=colour))
            embed.set_image(url='http:' + image)
            embed.set_author(name="Konachan", url=('http:' + image), icon_url=self.bot.user.avatar_url)
            await self.bot.say(embed=embed)
            #await self.bot.say('http:' + image)
        except Exception as e:
            embed=discord.Embed(colour=discord.Colour(value=colour))
            embed.set_image(url=image)
            embed.set_author(name="Konachan", url=(image), icon_url=self.bot.user.avatar_url)
            await self.bot.say(embed=embed)
            #await self.bot.say(":x: **Error:** `{}`".format(e))

    @commands.command(pass_context=True, no_pm=False)
    async def e621(self, ctx):
        """Random Image From e621"""
        dis_nsfw = None
        for a in self.settings["nsfw_channels"]:
            if a == ctx.message.channel.id:
                if self.settings["invert"]:
                    dis_nsfw = False
                else:
                    dis_nsfw = True
                break
        if dis_nsfw is None and not self.settings["invert"]:
            dis_nsfw = False
        else:
            dis_nsfw = True
            return
        try:
            query = ("https://e621.net/post/random")
            page = await aiohttp.get(query)
            page = await page.text()
            soup = BeautifulSoup(page, 'html.parser')
            image = soup.find(id="highres").get("href")
            colour = ''.join([randchoice('0123456789ABCDEF') for x in range(6)])
            colour = int(colour, 16)
            embed=discord.Embed(colour=discord.Colour(value=colour))
            embed.set_image(url=image)
            embed.set_author(name="e621", url=image, icon_url=self.bot.user.avatar_url)
            await self.bot.say(embed=embed)
        except Exception as e:
            await self.bot.say(":x: **Error:** `{}`".format(e))

    @commands.command(pass_context=True, no_pm=False)
    async def rule34(self, ctx):
        """Random Image From rule34"""
        dis_nsfw = None
        for a in self.settings["nsfw_channels"]:
            if a == ctx.message.channel.id:
                if self.settings["invert"]:
                    dis_nsfw = False
                else:
                    dis_nsfw = True
                break
        if dis_nsfw is None and not self.settings["invert"]:
            dis_nsfw = False
        else:
            dis_nsfw = True
            return
        try:
            query = ("http://rule34.xxx/index.php?page=post&s=random")
            page = await aiohttp.get(query)
            page = await page.text()
            soup = BeautifulSoup(page, 'html.parser')
            image = soup.find(id="image").get("src")
            colour = ''.join([randchoice('0123456789ABCDEF') for x in range(6)])
            colour = int(colour, 16)
            embed=discord.Embed(colour=discord.Colour(value=colour))
            embed.set_image(url='http:' + image)
            embed.set_author(name="rule34", url=('http:' + image), icon_url=self.bot.user.avatar_url)
            await self.bot.say(embed=embed)
        except Exception as e:
            await self.bot.say(":x: **Error:** `{}`".format(e))

    @commands.command(pass_context=True, no_pm=False)
    async def danbooru(self, ctx):
        """Random Image From Danbooru"""
        dis_nsfw = None
        for a in self.settings["nsfw_channels"]:
            if a == ctx.message.channel.id:
                if self.settings["invert"]:
                    dis_nsfw = False
                else:
                    dis_nsfw = True
                break
        if dis_nsfw is None and not self.settings["invert"]:
            dis_nsfw = False
        else:
            dis_nsfw = True
            return
        try:
            query = ("http://danbooru.donmai.us/posts/random")
            page = await aiohttp.get(query)
            page = await page.text()
            soup = BeautifulSoup(page, 'html.parser')
            image = soup.find(id="image").get("src")
            colour = ''.join([randchoice('0123456789ABCDEF') for x in range(6)])
            colour = int(colour, 16)
            embed=discord.Embed(colour=discord.Colour(value=colour))
            embed.set_image(url='http://danbooru.donmai.us' + image)
            embed.set_author(name="Danbooru", url=('http://danbooru.donmai.us' + image), icon_url=self.bot.user.avatar_url)
            await self.bot.say(embed=embed)
            #await self.bot.say('http://danbooru.donmai.us' + image)
        except Exception as e:
            await self.bot.say(":x: **Error:** `{}`".format(e))

    @commands.command(pass_context=True, no_pm=False)
    async def gelbooru(self, ctx):
        """Random Image From Gelbooru"""
        dis_nsfw = None
        for a in self.settings["nsfw_channels"]:
            if a == ctx.message.channel.id:
                if self.settings["invert"]:
                    dis_nsfw = False
                else:
                    dis_nsfw = True
                break
        if dis_nsfw is None and not self.settings["invert"]:
            dis_nsfw = False
        else:
            dis_nsfw = True
            return
        try:
            query = ("http://www.gelbooru.com/index.php?page=post&s=random")
            page = await aiohttp.get(query)
            page = await page.text()
            soup = BeautifulSoup(page, 'html.parser')
            image = soup.find(id="image").get("src")
            colour = ''.join([randchoice('0123456789ABCDEF') for x in range(6)])
            colour = int(colour, 16)
            embed=discord.Embed(colour=discord.Colour(value=colour))
            embed.set_image(url='http:' + image)
            embed.set_author(name="Gelbooru", url='http:' + image, icon_url=self.bot.user.avatar_url)
            await self.bot.say(embed=embed)
            #await self.bot.say(image)
        except Exception as e:
            embed=discord.Embed(colour=discord.Colour(value=colour))
            embed.set_image(url=image)
            embed.set_author(name="Gelbooru", url=image, icon_url=self.bot.user.avatar_url)
            await self.bot.say(embed=embed)
            #await self.bot.say(":x: **Error:** `{}`".format(e))

    @commands.command(pass_context=True, no_pm=False)
    async def tbib(self, ctx):
        """Random Image From DrunkenPumken"""
        dis_nsfw = None
        for a in self.settings["nsfw_channels"]:
            if a == ctx.message.channel.id:
                if self.settings["invert"]:
                    dis_nsfw = False
                else:
                    dis_nsfw = True
                break
        if dis_nsfw is None and not self.settings["invert"]:
            dis_nsfw = False
        else:
            dis_nsfw = True
            return
        try:
            query = ("http://www.tbib.org/index.php?page=post&s=random")
            page = await aiohttp.get(query)
            page = await page.text()
            soup = BeautifulSoup(page, 'html.parser')
            image = soup.find(id="image").get("src")
            colour = ''.join([randchoice('0123456789ABCDEF') for x in range(6)])
            colour = int(colour, 16)
            embed=discord.Embed(colour=discord.Colour(value=colour))
            embed.set_image(url='http:' + image)
            embed.set_author(name="The Big ImageBoard", url=('http:' + image), icon_url=self.bot.user.avatar_url)
            await self.bot.say(embed=embed)
            #await self.bot.say("http:" + image)
        except Exception as e:
            await self.bot.say(":x: **Error:** `{}`".format(e))

    @commands.command(pass_context=True, no_pm=False)
    async def xbooru(self, ctx):
        """Random Image From Xbooru"""
        dis_nsfw = None
        for a in self.settings["nsfw_channels"]:
            if a == ctx.message.channel.id:
                if self.settings["invert"]:
                    dis_nsfw = False
                else:
                    dis_nsfw = True
                break
        if dis_nsfw is None and not self.settings["invert"]:
            dis_nsfw = False
        else:
            dis_nsfw = True
            return
        try:
            query = ("http://xbooru.com/index.php?page=post&s=random")
            page = await aiohttp.get(query)
            page = await page.text()
            soup = BeautifulSoup(page, 'html.parser')
            image = soup.find(id="image").get("src")
            colour = ''.join([randchoice('0123456789ABCDEF') for x in range(6)])
            colour = int(colour, 16)
            embed=discord.Embed(colour=discord.Colour(value=colour))
            embed.set_image(url=image)
            embed.set_author(name="Xbooru", url=image, icon_url=self.bot.user.avatar_url)
            await self.bot.say(embed=embed)
            #await self.bot.say(image)
        except Exception as e:
            await self.bot.say(":x: **Error:** `{}`".format(e))

    @commands.command(pass_context=True, no_pm=False)
    async def furrybooru(self, ctx):
        """Random Image From Furrybooru"""
        dis_nsfw = None
        for a in self.settings["nsfw_channels"]:
            if a == ctx.message.channel.id:
                if self.settings["invert"]:
                    dis_nsfw = False
                else:
                    dis_nsfw = True
                break
        if dis_nsfw is None and not self.settings["invert"]:
            dis_nsfw = False
        else:
            dis_nsfw = True
            return
        try:
            query = ("http://furry.booru.org/index.php?page=post&s=random")
            page = await aiohttp.get(query)
            page = await page.text()
            soup = BeautifulSoup(page, 'html.parser')
            image = soup.find(id="image").get("src")
            colour = ''.join([randchoice('0123456789ABCDEF') for x in range(6)])
            colour = int(colour, 16)
            embed=discord.Embed(colour=discord.Colour(value=colour))
            embed.set_image(url=image)
            embed.set_author(name="Furrybooru", url=image, icon_url=self.bot.user.avatar_url)
            await self.bot.say(embed=embed)
            #await self.bot.say(image)
        except Exception as e:
            await self.bot.say(":x: **Error:** `{}`".format(e))

    @commands.command(pass_context=True, no_pm=False)
    async def drunkenpumken(self, ctx):
        """Random Image From DrunkenPumken"""
        dis_nsfw = None
        for a in self.settings["nsfw_channels"]:
            if a == ctx.message.channel.id:
                if self.settings["invert"]:
                    dis_nsfw = False
                else:
                    dis_nsfw = True
                break
        if dis_nsfw is None and not self.settings["invert"]:
            dis_nsfw = False
        else:
            dis_nsfw = True
            return
        try:
            query = ("http://drunkenpumken.booru.org/index.php?page=post&s=random")
            page = await aiohttp.get(query)
            page = await page.text()
            soup = BeautifulSoup(page, 'html.parser')
            image = soup.find(id="image").get("src")
            colour = ''.join([randchoice('0123456789ABCDEF') for x in range(6)])
            colour = int(colour, 16)
            embed=discord.Embed(colour=discord.Colour(value=colour))
            embed.set_image(url=image)
            embed.set_author(name="DrunkenPumken", url=image, icon_url=self.bot.user.avatar_url)
            await self.bot.say(embed=embed)
            #await self.bot.say(image)
        except Exception as e:
            await self.bot.say(":x: **Error:** `{}`".format(e))

    #@commands.command(pass_context=True, no_pm=False)
    #async def lolibooru(self, ctx):
        #"""Random Image From Lolibooru"""
        #dis_nsfw = None
        #for a in self.settings["nsfw_channels"]:
            #if a == ctx.message.channel.id:
                #if self.settings["invert"]:
                    #dis_nsfw = False
                #else:
                    #dis_nsfw = True
                #break
        #if dis_nsfw is None and not self.settings["invert"]:
            #dis_nsfw = False
        #else:
            #dis_nsfw = True
            #return
        #try:
            #query = ("https://lolibooru.moe/post/random/")
            #page = await aiohttp.get(query)
            #page = await page.text()
            #soup = BeautifulSoup(page, 'html.parser')
            #image = soup.find(id="image").get("src")
            #image = image.replace(' ','%20')
            #colour = ''.join([randchoice('0123456789ABCDEF') for x in range(6)])
            #colour = int(colour, 16)
            #embed=discord.Embed(colour=discord.Colour(value=colour))
            #embed.set_image(url=image)
            #embed.set_author(name="Lolibooru", url=image, icon_url=self.bot.user.avatar_url)
            #await self.bot.say(embed=embed)
            #await self.bot.say(image)
        #except Exception as e:
            #await self.bot.say(":x: **Error:** `{}`".format(e))

    @commands.command(pass_context=True, no_pm=False)
    async def ysearch(self, ctx, *tags: str):
        """Search Yandere With A Tag"""
        dis_nsfw = None
        for a in self.settings["nsfw_channels"]:
            if a == ctx.message.channel.id:
                if self.settings["invert"]:
                    dis_nsfw = False
                else:
                    dis_nsfw = True
                break
        if dis_nsfw is None and not self.settings["invert"]:
            dis_nsfw = False
        else:
            dis_nsfw = True
            return
        if tags == ():
            await self.bot.say(":warning: Tags are missing.")
        else:
            try:
                tags = ("+").join(tags)
                query = ("https://yande.re/post.json?limit=42&tags=" + tags)
                page = await aiohttp.get(query)
                json = await page.json()
                if json != []:
                    colour = ''.join([randchoice('0123456789ABCDEF') for x in range(6)])
                    colour = int(colour, 16)
                    embed=discord.Embed(colour=discord.Colour(value=colour))
                    embed.set_image(url=(random.choice(json)['jpeg_url']))
                    embed.set_author(name="Yandere", url=(random.choice(json)['jpeg_url']), icon_url=self.bot.user.avatar_url)
                    await self.bot.say(embed=embed)
                    #await self.bot.say(random.choice(json)['jpeg_url'])
                else:
                    await self.bot.say(":warning: Yande.re has no images for requested tags.")
            except Exception as e:
                await self.bot.say(":x: `{}`".format(e))
    
    async def boob_knowlegde():
        # KISS
        settings = dataIO.load_json(SETTINGS)
        now = round(time.time())
        interval = 86400*2
        if now >= settings["last_update"]+interval:
            settings["last_update"] = now
            dataIO.save_json(SETTINGS, settings)
        else:
            return
            
        async def search(url, curr):
            search = ("{}{}".format(url, curr))
            async with aiohttp.get(search) as r:
                result = await r.json()
                return result

        # Upadate boobs len
        print("Updating amount of boobs...")
        curr_boobs = settings["ama_boobs"]
        url = "http://api.oboobs.ru/boobs/"
        done = False
        reachable = curr_boobs
        step = 50
        while not done:
            q = reachable+step
            #print("Searching for boobs:", q)
            res = await search(url, q)
            if res != []:
                reachable = q
                res_dc = await search(url, q+1)
                if res_dc == []:
                    settings["ama_boobs"] = reachable
                    dataIO.save_json(SETTINGS, settings)
                    break
                else:
                    await asyncio.sleep(2.5) # Trying to be a bit gentle for the api.
                    continue
            elif res == []:
                step = round(step/2)
                if step <= 1:
                    settings["ama_boobs"] = curr_boobs
                    done = True
            await asyncio.sleep(2.5)
        print("Total amount of boobs:", settings["ama_boobs"])

        # Upadate ass len
        print("Updating amount of ass...")
        curr_ass = settings["ama_ass"]
        url = "http://api.obutts.ru/butts/"
        done = False
        reachable = curr_ass
        step = 50
        while not done:
            q = reachable+step
            #print("Searching for ass:", q)
            res = await search(url, q)
            if res != []:
                reachable = q
                res_dc = await search(url, q+1)
                if res_dc == []:
                    settings["ama_ass"] = reachable
                    dataIO.save_json(SETTINGS, settings)
                    break
                else:
                    await asyncio.sleep(2.5)
                    continue
            elif res == []:
                step = round(step/2)
                if step <= 1:
                    settings["ama_ass"] = curr_ass
                    done = True
            await asyncio.sleep(2.5)
        print("Total amount of ass:", settings["ama_ass"])

def check_folders():
    if not os.path.exists(DIR_DATA):
        print("Creating data/oboobs folder...")
        os.makedirs(DIR_DATA)

def check_files():
    if not os.path.isfile(SETTINGS):
        print("Creating default boobs ass settings.json...")
        dataIO.save_json(SETTINGS, DEFAULT)
    else:  # Key consistency check
        try:
            current = dataIO.load_json(SETTINGS)
        except JSONDecodeError:
            dataIO.save_json(SETTINGS, DEFAULT)
            current = dataIO.load_json(SETTINGS)

        if current.keys() != DEFAULT.keys():
            for key in DEFAULT.keys():
                if key not in current.keys():
                    current[key] = DEFAULT[key]
                    print( "Adding " + str(key) + " field to boobs settings.json")
            dataIO.save_json(SETTINGS, DEFAULT)

def setup(bot):
    check_folders()
    check_files()
    bot.add_cog(nsfw(bot))
    bot.loop.create_task(nsfw.boob_knowlegde())
