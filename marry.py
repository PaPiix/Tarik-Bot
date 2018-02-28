import discord
import os, re, aiohttp

from discord.ext import commands
from cogs.utils.dataIO import dataIO
from cogs.utils import checks
from .utils.dataIO import fileIO
from discord import Object

marry_log = Object('314512279053926410')


class Marry:
    """You can get married to a user by using !marry @someone"""

    def __init__(self, bot):
        self.bot = bot
        self.profile = "data/marry/server_marry.json"
        self.Tarik = dataIO.load_json(self.profile)

    @commands.command(pass_context=True)
    @checks.admin_or_permissions(manage_server=True)
    async def marryset(self, ctx, channel : discord.Channel = None):
        """Set the channel for marry logs. Defaults to none."""
        server = ctx.message.server
        if not channel:
            await self.bot.say("Marriage logging disabled.")
            if server.id not in self.Tarik:
                self.Tarik[server.id] = {}
            self.Tarik[server.id]['enabled'] = False
            dataIO.save_json(self.profile, self.Tarik)
            return
        if server.id not in self.Tarik:
            self.Tarik[server.id] = {}
        self.Tarik[server.id]['enabled'] = True
        self.Tarik[server.id]['channel'] = channel.id
        dataIO.save_json(self.profile, self.Tarik)
        await self.bot.say("Marriage log has been set to: {}".format(channel.mention))



    @commands.command(pass_context=True)
    async def marry(self, ctx, user : discord.Member):
        """Marry a user"""

        #declare vars
        server  = ctx.message.server
        author  = ctx.message.author
        channel = ctx.message.channel
        user    = user

        #checks if user already has data in the json
        await self._check(server, user, author)

        if user == author:
            embed = discord.Embed(description="You can't marry yourself!", color=0XF23636)
            await self.bot.say(embed=embed)
            return
        elif user.bot:
            embed = discord.Embed(description="You can't marry a bot!", color=0XF23636)
            await self.bot.say(embed=embed)
            return


        #checks if user is married
        if self.Tarik[server.id][user.id]['married'] or self.Tarik[server.id][author.id]['married']:
            if 'married_to' in self.Tarik[server.id][user.id]:
                if self.Tarik[server.id][user.id]['married_to'] == author.id:
                    msg = "You are already married to {}, {}!".format(user.mention, author.mention)
                    embed = discord.Embed(description=msg, color=0XF23636)
                    await self.bot.say(embed=embed)
                    return
                married_to_id = self.Tarik[server.id][user.id]['married_to']
                married_to = discord.utils.get(server.members, id=married_to_id)
                msg = "{} is already married to {}!".format(user.mention, married_to.mention)
                embed = discord.Embed(description=msg, color=0XF23636)
                await self.bot.say(embed=embed)
            if 'married_to' in self.Tarik[server.id][author.id]:
                married_to_id = self.Tarik[server.id][author.id]['married_to']
                married_to = discord.utils.get(server.members, id=married_to_id)
                msg = "{} is already married to {}!".format(author.mention, married_to.mention)
                embed = discord.Embed(description=msg, color=0XF23636)
                await self.bot.say(embed=embed)
            return

        #the proposal
        desc = ":ring:" + author.mention + " *has proposed to* " + user.mention + ":ring:"
        name = ":church:" + user.name + ",  Do you accept? :church:"

        embed = discord.Embed(description=desc, color=0XF23636)
        embed.add_field(name=name, value='Type `yes` to accept or `no` to decline.')

        await self.bot.say(embed=embed)

        #wait for a response
        response = await self.bot.wait_for_message(author=user,
                                                   channel=channel,
                                                   timeout=10)

        #if there is no reponse, except statement shoots out
        try:
            response_content = response.content.lower()
            if response_content != 'yes':
                response_content = 'no'
        except Exception as e:
            print(e)
            msg = "Nevermind then."
            embed = discord.Embed(description=msg, color=0XF23636)
            await self.bot.say(embed=embed)
            return

        #checks reponse
        if response_content == 'yes':
            await self._marry_user(server, user, author)
            msg = ":heart: Congratulations " + author.mention + " and " + user.mention + " :heart:"
            embed = discord.Embed(description=msg, color=0XF23636)
            await self.bot.say(embed=embed)
        else:
            msg = "Nevermind then."
            embed = discord.Embed(description=msg, color=0XF23636)
            await self.bot.say(embed=embed)


        #logs to server log
        if 'enabled' in self.Tarik[server.id]:
            if self.Tarik[server.id]['enabled']:
                channel_id = self.Tarik[server.id]['channel']
                marry_log_channel = discord.utils.get(self.bot.get_all_channels(), id=channel_id)
                embed=discord.Embed(title="Server Marriages", colour=0xFF0000)
                embed.set_thumbnail(url=self.bot.user.avatar_url)
                embed.add_field(name="Marry", value="{} has married {}.".format(author.name, user.mention))
                await self.bot.send_message(marry_log_channel, embed=embed)

        #sends to tarik server
        embed=discord.Embed(title="Global Marriages", colour=0xFF0000)
        embed.set_thumbnail(url=author.server.icon_url)
        embed.add_field(name="Marry", value="{} has married to {} in {}.".format(author.name, user.name, server))
        await self.bot.send_message(marry_log, embed=embed)


    @commands.command(pass_context=True)
    async def divorce(self, ctx, user : discord.Member):
        """divorce a user"""

        #declare vars
        server  = ctx.message.server
        author  = ctx.message.author
        channel = ctx.message.channel
        user    = user

        if user == author:
            embed = discord.Embed(description="You can't divorce yourself!", color=0XF23636)
            await self.bot.say(embed=embed)
            return
        elif user.bot:
            embed = discord.Embed(description="You can't divorce a bot!", color=0XF23636)
            await self.bot.say(embed=embed)
            return


        await self._check(server, user, author)

        if self.Tarik[server.id][author.id]['married']:
            if self.Tarik[server.id][author.id]['married_to'] == user.id:
                msg = author.mention + ' *has divorced* ' + user.mention + '.'
                embed = discord.Embed(description=msg, color=0XF23636)
                await self.bot.say(embed=embed)
                await self._divorce_user(server, user, author)
            else:
                msg = "You aren't married to that user!"
                embed = discord.Embed(description=msg, color=0XF23636)
                await self.bot.say(embed=embed)
        else:
            msg = "You aren't married!"
            embed = discord.Embed(description=msg, color=0XF23636)
            await self.bot.say(embed=embed)

        if 'enabled' in self.Tarik[server.id]:
            if self.Tarik[server.id]['enabled']:
                channel_id = self.Tarik[server.id]['channel']
                marry_log_channel = discord.utils.get(self.bot.get_all_channels(), id=channel_id)
                embed=discord.Embed(title="Server Marriages", colour=0xFF0000)
                embed.set_thumbnail(url=self.bot.user.avatar_url)
                embed.add_field(name="Marry", value="{} has divorced {}.".format(author.name, user.mention))
                await self.bot.send_message(marry_log_channel, embed=embed)

        embed=discord.Embed(title="Global Marriages", colour=0xFF0000)
        embed.set_thumbnail(url=author.server.icon_url)
        embed.add_field(name="Marry", value="{} has married to {} in {}.".format(author.name, user.name, server))
        await self.bot.send_message(marry_log, embed=embed)



    #checks if things are in the json
    async def _check(self, server, user, author):
        if server.id not in self.Tarik:
            self.Tarik[server.id] = {}
        if user.id not in self.Tarik[server.id]:
            self.Tarik[server.id][user.id] = {}
            self.Tarik[server.id][user.id]['married'] = False
        if author.id not in self.Tarik[server.id]:
            self.Tarik[server.id][author.id] = {}
            self.Tarik[server.id][author.id]['married'] = False
        dataIO.save_json(self.profile, self.Tarik)

    #marries a user
    async def _marry_user(self, server, user, author):
        self.Tarik[server.id][user.id]['married'] = True
        self.Tarik[server.id][user.id]['married_to'] = author.id
        self.Tarik[server.id][author.id]['married'] = True
        self.Tarik[server.id][author.id]['married_to'] = user.id
        dataIO.save_json(self.profile, self.Tarik)

    #divorces a user
    async def _divorce_user(self, server, user, author):
        self.Tarik[server.id][user.id]['married'] = False
        self.Tarik[server.id][author.id]['married'] = False
        dataIO.save_json(self.profile, self.Tarik)



def check_folder():
    if not os.path.exists('data/marry'):
        print('Creating data/marry folder...')
        os.makedirs('data/marry')

def check_files():

    f = 'data/marry/server_marry.json'
    if not dataIO.is_valid_json(f):
        dataIO.save_json(f, {})
        print('Creating default server_marry.json...')

def setup(bot):
    check_folder()
    check_files()
    bot.add_cog(Marry(bot))
