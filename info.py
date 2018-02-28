import discord
import psutil
import time
starttime = time.time()
import os
from discord.ext import commands

class Stats:
    def __init__(self, bot):
        self.bot = bot
        self.cache_path = "data/audio/cache"
        
    @commands.command(pass_context=True)
    async def info(self, ctx):
        """Tarik's Information."""
        text_channels = 0
        voice_channels = 0
        list2 = []
        list = []
        for i in self.bot.servers:
            if i.me.voice_channel is not None:
                list.append(i.me.voice_channel)
        for c in list:
            list2.extend(c.voice_members)
        mem_v = psutil.virtual_memory()
        cpu_p = psutil.cpu_percent(interval=None, percpu=True)
        cpu_usage = sum(cpu_p)/len(cpu_p)
        online = len([e.name for e in self.bot.get_all_members() if not e.bot and e.status == discord.Status.online])
        idle = len([e.name for e in self.bot.get_all_members() if not e.bot and e.status == discord.Status.idle])
        dnd = len([e.name for e in self.bot.get_all_members() if not e.bot and e.status == discord.Status.dnd])
        offline = len([e.name for e in self.bot.get_all_members() if not e.bot and e.status == discord.Status.offline])
        seconds = time.time() - starttime
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)
        w, d = divmod(d, 7)
        t1 = time.perf_counter()
        await self.bot.type()
        t2 = time.perf_counter()
        data = discord.Embed(description="Here is all my information:", colour=0xFF0000)
        data.add_field(name="Owner", value="TTxFTW")
        data.add_field(name="Ping", value="{}ms".format(round((t2-t1)*1000)))
        data.add_field(name="Servers", value=len(self.bot.servers))
        data.add_field(name="Api version", value=discord.__version__)
        data.add_field(name="Users", value="{} Online<:vpOnline:212789758110334977>\n{} Idle<:vpAway:212789859071426561>\n{} Dnd<:vpDnD:236744731088912384>\n{} Offline<:vpOffline:212790005943369728>".format(online, idle, dnd, offline))
        data.add_field(name="Channels", value="{} Voice Channels\n\n{} Text Channels".format(len([e for e in self.bot.get_all_channels() if e.type == discord.ChannelType.voice]), len([e for e in self.bot.get_all_channels() if e.type == discord.ChannelType.text])))
        data.add_field(name='CPU usage', value='{0:.1f}%'.format(cpu_usage))
        data.add_field(name='Memory usage', value='{0:.1f}%'.format(mem_v.percent))
        data.add_field(name="Commands", value="{0} active modules, with {1} commands...".format(len(self.bot.cogs), len(self.bot.commands)))
        data.add_field(name='Uptime', value="%d Weeks," % (w) + " %d Days," % (d) + " %d Hours,"
                                   % (
                h) + " %d Minutes," % (m) + " and %d Seconds!" % (s))
        data.add_field(name="Voice Stats:", value="Connected to {} voice channels, with a total of {} users, and {:.3f} MB of cache.".format(len(list), len(list2), self._cache_size()), inline=False)
        data.add_field(name="Official Server", value="[Click Here]({})".format("https://discord.gg/5E7hrVk"))
        data.add_field(name="Invite Me", value="[Click Here]({})".format("https://discordapp.com/oauth2/authorize?client_id=263080353680457728&scope=bot&permissions=2146958463"))
        data.add_field(name="Website", value="[Click Here]({})".format("http://www.tarikbot.com"))
        data.set_author(name="Tarik", icon_url=self.bot.user.avatar_url)
        data.set_thumbnail(url=self.bot.user.avatar_url)
        data.set_image(url=self.bot.user.avatar_url)
        data.set_footer(text="tarikbot.com")
        await self.bot.say(embed=data)
        
    def _cache_size(self):
        songs = os.listdir(self.cache_path)
        size = sum(map(lambda s: os.path.getsize(
            os.path.join(self.cache_path, s)) / 10**6, songs))
        return size
        
def setup(bot):
    n = Stats(bot)
    bot.add_cog(n)