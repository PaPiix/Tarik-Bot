import discord
from discord.ext import commands
import os
from .utils.dataIO import fileIO
import os
import discord
import asyncio
import datetime
import unicodedata
from .utils import checks
from random import randint
from random import choice as randchoice

__author__ = "Alan"

owner_id = "173102900514521089"#pls pass the owner id here
db = {"Toggle": False, "Server Logs": False, "Error Logs" : False, "Startup": False, "Channel Logs" : False, "Channel": None, "Direct Message" : False, "Resumed": False,}

class ErrorLogger:
    """For producing error logs of Kairos and sending them to the owner or a specific channel
    Please Note: Kairos needs Embed Links permissions for this since all the responses are going to be in embeds
    Another Note: Embed Links is always set to True in Direct Messages"""

    def __init__(self, bot):
        self.bot = bot
        self.log_data = "data/errorlogger/settings.json"
    
    def time_parse(self, value : int):
        start = int(value.total_seconds())
        hours, remainder = divmod(start, 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        months, days = divmod(days, 30)
        if months:
            kek = '{mn} Months, {d} Days , {h} Hours and {m} Minutes ago'
        else:
            kek = '{d} Days, {h} Hours and {m} Minutes ago'
        return kek.format(mn = months, d = days, h = hours, m = minutes)
    @commands.group(pass_context=True, no_pm=True)
    @checks.is_owner()
    async def errorlogger(self, ctx):
        """Manage Logging Settings."""
        channel = ctx.message.channel
        server = ctx.message.server
        my = server.me
        data = fileIO(self.log_data, "load")
        if ctx.invoked_subcommand is None:
            colour = ''.join([randchoice('0123456789ABCDEF') for x in range(6)])
            colour = int(colour, 16)
            if data["Channel"] is None:
                kek = "No Channel Chosen"
            else:
                kek = "Channel: #{0.name}\nID: {0.id}".format(self.bot.get_channel(data["Channel"]))
            e = discord.Embed()
            e.colour = colour
            e.description = "Showing Error Log Settings\nDo {}help errorlogger for more info".format(ctx.prefix)
            e.set_author(name = "Error Logging")
            e.add_field(name = "Logging Enabled", value = data["Toggle"])
            e.add_field(name = "Server Logging", value = data["Server Logs"])
            e.add_field(name = "Error Logging", value = data["Error Logs"])
            e.add_field(name = "Startup Logging", value = data["Startup"])
            e.add_field(name = "Session Resume Logs", value = data["Resumed"])
            e.add_field(name = "DirectMessage Enabled", value = data["Direct Message"])
            e.add_field(name = "Channel Messages Enabled", value = data["Channel Logs"])
            e.add_field(name = "Channel Chosen", value = kek)
            e.set_footer(text = "Error Logs", icon_url = self.bot.user.avatar_url)
            await self.bot.send_message(ctx.message.channel, embed = e)
    @errorlogger.command(pass_context=True)
    async def toggle(self, ctx):
        """Enables or Disables the Logger"""
        data = fileIO(self.log_data, "load")
        data["Toggle"] = not data["Toggle"]
        if data["Toggle"] is True:
            msg = "Successfully Enabled the Error Logger"
        else:
            msg = "Successfully Disabled the Error Logger"
        await self.bot.reply(msg)
        fileIO(self.log_data, "save", data)
    @errorlogger.command(pass_context=True)
    async def serverlogs(self, ctx):
        """Enables or Disables Server Join/Leave Logging"""
        data = fileIO(self.log_data, "load")
        data["Server Logs"] = not data["Server Logs"]
        if data["Server Logs"] is True:
            msg = "Successfully Enabled Server join/ leave logging"
        else:
            msg = "Successfully Disabled the join/ leave Logger"
        await self.bot.reply(msg)
        fileIO(self.log_data, "save", data)
    @errorlogger.command(pass_context=True)
    async def errorlogs(self, ctx):
        """Enables or Disables Error Logging"""
        data = fileIO(self.log_data, "load")
        data["Error Logs"] = not data["Error Logs"]
        if data["Error Logs"] is True:
            msg = "Successfully Enabled Error Logging"
        else:
            msg = "Successfully Disabled Error Logging"
        await self.bot.reply(msg)
        fileIO(self.log_data, "save", data)
    @errorlogger.command(pass_context=True)
    async def startup(self, ctx):
        """Enables or Disables Startup Logging"""
        data = fileIO(self.log_data, "load")
        data["Startup"] = not data["Startup"]
        if data["Toggle"] is True:
            msg = "Successfully Enabled Startup Logging"
        else:
            msg = "Successfully Disabled Startup Logging"
        await self.bot.reply(msg)
        fileIO(self.log_data, "save", data)
    @errorlogger.command(pass_context=True)
    async def resumelogs(self, ctx):
        """Enables or Disables """
        data = fileIO(self.log_data, "load")
        data["Resumed"] = not data["Resumed"]
        if data["Resumed"] is True:
            msg = "Successfully Enabled the Session Resume logs"
        else:
            msg = "Successfully Disabled the Session Resume logs"
        await self.bot.reply(msg)
        fileIO(self.log_data, "save", data)
    @errorlogger.command(pass_context=True)
    async def dmlogs(self, ctx):
        """Enables or Disables the whether I will DM you errors in Private"""
        data = fileIO(self.log_data, "load")
        data["Direct Message"] = not data["Direct Message"]
        if data["Direct Message"] is True:
            msg = "I will now send you logs in Private Messages."
        else:
            msg = "I will not send you logs in Private Messages from now on."
        await self.bot.reply(msg)
        fileIO(self.log_data, "save", data)
    @errorlogger.command(pass_context=True)
    async def channellogs(self, ctx):
        """Enables or Disables whether I will send logs in Channel"""
        data = fileIO(self.log_data, "load")
        data["Channel Logs"] = not data["Channel Logs"]
        if data["Channel Logs"] is True:
            msg = "I will now send you logs in the Channel."
        else:
            msg = "I will not send you logs in the Channel."
        await self.bot.reply(msg)
        fileIO(self.log_data, "save", data)
    @errorlogger.command(pass_context=True)
    async def errorchannel(self, ctx, channel : discord.Channel):
        """Sets the error channel"""
        data = fileIO(self.log_data, "load")
        if channel.type == discord.ChannelType.voice:
            await self.bot.reply("Please pass a text channel instead of a voice channel")
            return
        data["Channel"] = channel.id
        msg = "Successfully set the channel to {0.mention}".format(channel)
        await self.bot.reply(msg)
        fileIO(self.log_data, "save", data)
    @errorlogger.command(pass_context=True)
    async def enableall(self, ctx):
        """Enables all Loggers"""
        data = fileIO(self.log_data, "load")
        data["Toggle"] = True
        data["Channel Logs"] = True
        data["Error Logs"] = True
        data["Server Logs"] = True
        data["Direct Message"] = True
        data["Startup"] = True
        data["Resumed"] = True
        await self.bot.reply("Enabled all Logging functions")
        fileIO(self.log_data, "save", data)
    @errorlogger.command(pass_context=True)
    async def disableall(self, ctx):
        """Disables all Loggers"""
        data = fileIO(self.log_data, "load")
        data["Toggle"] = False
        data["Channel Logs"] = False
        data["Error Logs"] = False
        data["Server Logs"] = False
        data["Direct Message"] = False
        data["Startup"] = False
        data["Resumed"] = False
        await self.bot.reply("Disabled all Logging functions")
        fileIO(self.log_data, "save", data)
    async def embed_serverdata(self, server):#To make it look less ugly
        """Because I think it's neater"""
        colour = ''.join([randchoice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16) 
        owner = server.owner
        namea = owner.name+"#"+owner.discriminator
        url = "http://dahoo.fr/wordpress/wp-content/uploads/2015/09/discord.jpg" if not server.icon_url else server.icon_url
        date = self.time_parse(value = (datetime.datetime.utcnow() - server.created_at))
        e = discord.Embed()
        e.title = "Joined a Server \U00002611\nMy Server Count: {}".format(len(self.bot.servers))
        e.set_thumbnail(url = url)
        e.colour = colour
        e.set_author(name = "Log : Server Joins")
        e.add_field(name = "Name", value = server.name)
        e.add_field(name = "ID", value = server.id)
        e.add_field(name = "Owner", value = namea)
        e.add_field(name = "Total Members", value = str(len(server.members)))
        e.add_field(name = "Created At", value = "{0}    ({1})".format(format(server.created_at, "%d %b %Y at %H:%M"), date))
        e.timestamp = datetime.datetime.utcnow()
        e.set_footer(text = "Server Join Logs", icon_url = self.bot.user.avatar_url)
        return e
    async def on_server_join(self, server):
        print("Error Logger: Join Server")
        owner = discord.utils.get(self.bot.get_all_members(), id = owner_id)
        data = fileIO(self.log_data, "load")
        if data["Toggle"] is True and data["Server Logs"] is True:
            info = await self.embed_serverdata(server = server)
            if data["Channel Logs"] is True:
                if data["Channel"] is not None:
                    channel = self.bot.get_channel(data["Channel"])
                    await self.bot.send_message(channel, embed = info)
                else:
                    pass
            if data["Direct Message"] is True:
                await self.bot.send_message(owner, embed = info)
            else:
                pass
        else:
            pass
    async def on_server_remove(self, server):
        print("Error Logger: Left Server")
        msg = "**Left Server** \U0000274e\n"
        msg += "```Prolog\nName : {0.name}\n\nID : {0.id}\n```".format(server)
        owner = discord.utils.get(self.bot.get_all_members(), id = owner_id)
        data = fileIO(self.log_data, "load")
        if data["Toggle"] is True and data["Server Logs"] is True:
            if data["Channel Logs"] is True:
                if data["Channel"] is not None:
                    channel = self.bot.get_channel(data["Channel"])
                    await self.bot.send_message(channel, msg)
                else:
                    pass
            if data["Direct Message"] is True:
                await self.bot.send_message(owner, msg)
            else:
                pass
        else:
            pass
    async def on_command_error(self, error, ctx):
        if isinstance(error, commands.CommandInvokeError):
            print("Error Logger: Command Error")
            owner = discord.utils.get(self.bot.get_all_members(), id = owner_id)
            data = fileIO(self.log_data, "load")
            channeldata = "#{0.name}\nID: {0.id}".format(ctx.message.channel)
            colour = ''.join([randchoice('0123456789ABCDEF') for x in range(6)])
            colour = int(colour, 16) 
            command = "{0.prefix}{0.command.qualified_name}".format(ctx)
            cmderror = "{0} : {1}".format(type(error.original).__name__, str(error.original))
            server = ctx.message.server.name
            e = discord.Embed()
            e.title = "Error Log \U0000274e".format(len(self.bot.servers))
            e.colour = colour
            e.set_author(name = "Log : Error Log")
            e.add_field(name = "Server", value = server)
            e.add_field(name = "Channel", value = channeldata)
            e.add_field(name = "Command", value = command)
            e.add_field(name = "Error Info", value = cmderror, inline = False)
            e.timestamp = ctx.message.timestamp
            e.set_footer(text = "Error Occured At |", icon_url = self.bot.user.avatar_url)
            if (data["Toggle"] is True) and (data["Server Logs"] is True):
                if data["Channel Logs"] is True:
                    if data["Channel"] is not None:
                        channel = self.bot.get_channel(data["Channel"])
                        await self.bot.send_message(channel, embed = e)
                    else:
                        pass
                if data["Direct Message"] is True:
                    await self.bot.send_message(owner, embed = e)
                else:
                    pass
            else:
                pass
        else:
            pass
    async def on_ready(self):
        print("Error Logger: On Ready")
        data = fileIO(self.log_data, "load")
        owner = discord.utils.get(self.bot.get_all_members(), id = owner_id)
        colour = ''.join([randchoice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)
        name = self.bot.user.name+"#"+self.bot.user.discriminator
        cogs = "\n".join(e for e in self.bot.cogs)
        prefix = " , ".join(e for e in self.bot.command_prefix)
        e = discord.Embed()
        e.title = "{} has Started \U00002705".format(name)
        e.set_author(name = "Log : Startup Log")
        e.add_field(name = "Commands", value = str(len(self.bot.commands)))
        e.add_field(name = "Servers", value = str(len(self.bot.servers)))
        e.add_field(name = "Prefix", value = prefix)
        e.add_field(name = "Total Cogs", value = str(len(self.bot.cogs)))
        e.add_field(name = "Cog List", value = cogs, inline = False)
        e.colour = colour
        e.timestamp = datetime.datetime.utcnow()
        e.set_footer(text = "Started At |", icon_url = self.bot.user.avatar_url)
        if data["Toggle"] is True and data["Startup"] is True:
            if data["Channel Logs"] is True:
                if data["Channel"] is not None:
                    channel = self.bot.get_channel(data["Channel"])
                    await self.bot.send_message(channel, embed = e)
                else:
                    pass
            if data["Direct Message"] is True:
                await self.bot.send_message(owner, embed = e)
            else:
                pass
        else:
            pass

    async def on_resumed(self):
        print("Error Logger: On Resumed")
        data = fileIO(self.log_data, "load")
        owner = discord.utils.get(self.bot.get_all_members(), id = owner_id)
        colour = ''.join([randchoice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)
        name = self.bot.user.name+"#"+self.bot.user.discriminator
        cogs = "\n".join(e for e in self.bot.cogs)
        prefix = " , ".join(e for e in self.bot.command_prefix)
        e = discord.Embed()
        uptime = self.bot.get_cog("Utility").get_bot_uptime()
        e.title = "{} has Resumed the Session \U00002705".format(name)
        e.set_author(name = "Log : Session Resume")
        e.add_field(name = "Commands", value = str(len(self.bot.commands)))
        e.add_field(name = "Servers", value = str(len(self.bot.servers)))
        e.add_field(name = "Prefix", value = prefix)
        e.add_field(name = "Total Cogs", value = str(len(self.bot.cogs)))
        e.add_field(name = "Uptime", value = uptime)
        e.add_field(name = "Cog List", value = cogs, inline = False)
        e.colour = colour
        e.timestamp = datetime.datetime.utcnow()
        e.set_footer(text = "Started At |", icon_url = self.bot.user.avatar_url)
        if data["Toggle"] is True and data["Startup"] is True:
            if data["Channel Logs"] is True:
                if data["Channel"] is not None:
                    channel = self.bot.get_channel(data["Channel"])
                    await self.bot.send_message(channel, embed = e)
                else:
                    pass
            if data["Direct Message"] is True:
                await self.bot.send_message(owner, embed = e)
            else:
                pass
        else:
            pass

def check_folder():
    if not os.path.exists('data/errorlogger'):
        print('Creating data/errorlogger folder...')
        os.makedirs('data/errorlogger')

def check_file():
    f = 'data/errorlogger/settings.json'
    if not fileIO(f, 'check'):
        print('Creating default settings.json...')
        fileIO(f, 'save', db)
def setup(bot):
    check_folder()
    check_file()
    n = ErrorLogger(bot)
    bot.add_cog(n)