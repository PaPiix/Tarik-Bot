from cogs.utils.dataIO import dataIO
from discord.ext import commands
from .utils import checks
import datetime
import requests
import asyncio
import discord
import time
import os
import psutil
import aiohttp


class name:
    """help"""

    def __init__(self, bot):
        self.bot = bot
    @checks.is_owner()
    @commands.command(hidden=True)
    async def sendstats(self):
        """help"""
        geturl = "http://tarikbot.com/fetcher.php"
        try:
            uptime = abs(self.bot.uptime - int(time.perf_counter()))
        except TypeError:
            uptime = time.time() - time.mktime(self.bot.uptime.timetuple())
        up = datetime.timedelta(seconds=uptime)
        days = up.days
        hours = int(up.seconds/3600)
        minutes = int(up.seconds % 3600/60)
        users = str(len(set(self.bot.get_all_members())))
        servers = str(len(self.bot.servers))
        text_channels = 0
        voice_channels = 0

        cpu_p = psutil.cpu_percent(interval=None, percpu=True)
        cpu_usage = sum(cpu_p)/len(cpu_p)

        mem_v = psutil.virtual_memory()

        for channel in self.bot.get_all_channels():
            if channel.type == discord.ChannelType.text:
                text_channels += 1
            elif channel.type == discord.ChannelType.voice:
                voice_channels += 1
        channels = text_channels + voice_channels

        avatar = self.bot.user.avatar_url if self.bot.user.avatar else self.bot.user.default_avatar_url

        uptime = '{} D - {} H - {} M'.format(str(days), str(hours), str(minutes))
        #Servers is servers var
        #channels var
        #text_channel var
        #voice_channel var
        #str(self.recieved_messages)
        #str(self.sent_messages)
        #str(len(self.bot.commands))
        cpu = ('{0:.1f}%'.format(cpu_usage))
        memory = ('{0:.1f}%'.format(mem_v.percent))
        api = ('API version {}'.format(discord.__version__))
        param = {"uptime" : uptime, "users" : users, "server" : servers, "channels" : channels, "textc" : text_channels, "voicec" : voice_channels, "cpuu" : cpu, "memoryu" : memory, "apiv" : api, "commands" : str(len(self.bot.commands))}
        async with aiohttp.ClientSession() as session:
            async with session.get(geturl, params=param) as resp:
                response = await resp.text()
        await self.bot.say(response)
        
    async def send_stats(self):
        while not self.bot.is_closed:
            geturl = "http://tarikbot.com/fetcher.php"
            try:
                uptime = abs(self.bot.uptime - int(time.perf_counter()))
            except TypeError:
                uptime = time.time() - time.mktime(self.bot.uptime.timetuple())
            up = datetime.timedelta(seconds=uptime)
            days = up.days
            hours = int(up.seconds/3600)
            minutes = int(up.seconds % 3600/60)
            users = str(len(set(self.bot.get_all_members())))
            servers = str(len(self.bot.servers))
            text_channels = 0
            voice_channels = 0

            cpu_p = psutil.cpu_percent(interval=None, percpu=True)
            cpu_usage = sum(cpu_p)/len(cpu_p)

            mem_v = psutil.virtual_memory()

            for channel in self.bot.get_all_channels():
                if channel.type == discord.ChannelType.text:
                    text_channels += 1
                elif channel.type == discord.ChannelType.voice:
                    voice_channels += 1
            channels = text_channels + voice_channels

            avatar = self.bot.user.avatar_url if self.bot.user.avatar else self.bot.user.default_avatar_url

            uptime = '{} D - {} H - {} M'.format(str(days), str(hours), str(minutes))
            #Servers is servers var
            #channels var
            #text_channel var
            #voice_channel var
            #str(self.recieved_messages)
            #str(self.sent_messages)
            #str(len(self.bot.commands))
            cpu = ('{0:.1f}%'.format(cpu_usage))
            memory = ('{0:.1f}%'.format(mem_v.percent))
            api = ('API version {}'.format(discord.__version__))
            param = {"uptime" : uptime, "users" : users, "server" : servers, "channels" : channels, "textc" : text_channels, "voicec" : voice_channels, "cpuu" : cpu, "memoryu" : memory, "apiv" : api, "commands" : str(len(self.bot.commands))}
            async with aiohttp.ClientSession() as session:
                async with session.get(geturl, params=param) as resp:
                    response = await resp.text()
            print(response)
            await asyncio.sleep(10)



def setup(bot):
    n = name(bot)
    bot.loop.create_task(n.send_stats())
    bot.add_cog(n)
