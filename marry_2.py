import discord
from discord.ext import commands
from cogs.utils.dataIO import dataIO
from cogs.utils import checks
import os, re, aiohttp
from .utils.dataIO import fileIO
from discord import Object

marry_log = Object('295546154991484928')


class marry:
    """You can get married to a user by using !marry @someone"""

    def __init__(self, bot):
        self.bot = bot
        self.JSON = 'data/married/global_married.json'
        self.data = dataIO.load_json(self.JSON)
        self.profile = "data/married/marriage_settings.json"
        self.riceCog = dataIO.load_json(self.profile)

    @commands.command(pass_context=True)
    @checks.admin_or_permissions(manage_server=True)
    async def marryset(self, ctx, channel : discord.Channel = None):
        """Set the channel for marry logs. Defaults to none."""
        server = ctx.message.server
        if not channel:
            await self.bot.say("Marriage logging disabled.")
            if server.id not in self.riceCog:
                self.riceCog[server.id] = {}
            self.riceCog[server.id]['enabled'] = False
            dataIO.save_json(self.profile, self.riceCog)
            return
        if server.id not in self.riceCog:
            self.riceCog[server.id] = {}
        self.riceCog[server.id]['enabled'] = True
        self.riceCog[server.id]['channel'] = channel.id
        dataIO.save_json(self.profile, self.riceCog)
        await self.bot.say("Marriage log has been set to: {}".format(channel.name))





    @commands.command(pass_context=True)
    async def marry(self, ctx, user: discord.Member):
        server = ctx.message.server
        author = ctx.message.author
        me = ctx.message.author.name
        if 'user' in self.data:
            if author.id in self.data['user']:
                if 'married_to' in self.data['user'][ctx.message.author.id]:
                    if user.id in self.data['user'][ctx.message.author.id]['married_to']:
                        await self.bot.say("You are already married to {}!".format(user.name))
                        return
        desc = ":ring:" + me + " *has proposed to* " + user.name + ":ring:"
        name = ":church:" + user.name + ",  Do you accept ? :church:"
        em = discord.Embed(description=desc, color=0XF23636)
        em.add_field(name=name, value='Type yes to accept or no to decline.')
        await self.bot.say(embed=em)
        response = await self.bot.wait_for_message(author=user)

        if response.content.lower().strip() == "yes":
            await self._create_author(server, ctx, user)
            await self._create_user(server, ctx, user)
            msg = ":heart: Congratulations " + me + " and " + user.name + " :heart:"
            em1 = discord.Embed(description=msg, color=0XF23636)
            await self.bot.say(embed=em1)
            dataIO.save_json(self.JSON, self.data)
            embed=discord.Embed(title="Global Marriages", colour=0xFF0000)
            embed.set_thumbnail(url=self.bot.user.avatar_url)
            embed.add_field(name="Marry", value="{} has married to {} in {}.".format(me, user.name, server))
            await self.bot.send_message(marry_log, embed=embed)
            if server.id in self.riceCog:
                if self.riceCog[server.id]['enabled']:
                    channel_id = self.riceCog[server.id]['channel']
                    marry_log_channel = discord.utils.get(self.bot.get_all_channels(), id=channel_id)
                    embed=discord.Embed(title="Server Marriages", colour=0xFF0000)
                    embed.set_thumbnail(url=self.bot.user.avatar_url)
                    embed.add_field(name="Marry", value="{} has married to {}.".format(me, user.name))
                    await self.bot.send_message(marry_log_channel, embed=embed)

        else:
            msg = "The proposal between " + me + " and " + user.name + " has been declined."
            em2 = discord.Embed(description=msg, color=0XF23636)
            await self.bot.say(embed=em2)

    @commands.command(pass_context=True)
    async def divorce(self, ctx, user: discord.Member):
        author = ctx.message.author
        server = ctx.message.server
        if user == author:
            em0 = discord.Embed(description='You cant\'t divorce to yourself crazy guy!', color=0XF23636)
            await self.bot.say(embed=em0)
        else:
            if user.id in self.data["user"][author.id]["married_to"]:
                await self._divorce(server, ctx, user)
                me = ctx.message.author.name
                msg = me + ' *has divorced to* ' + user.name + '.'
                em = discord.Embed(description=msg, color=0XF23636)
                await self.bot.say(embed=em)
                embed=discord.Embed(title="Global Marriages", colour=0xFF0000)
                embed.set_thumbnail(url=self.bot.user.avatar_url)
                embed.add_field(name="Divorce", value="{} has divorced with {} in {}.".format(me, user.name, server))
                await self.bot.send_message(marry_log ,embed=embed)
                if server.id in self.riceCog:
                    if self.riceCog[server.id]['enabled']:
                        channel_id = self.riceCog[server.id]['channel']
                        marry_log_channel = discord.utils.get(self.bot.get_all_channels(), id=channel_id)
                        embed=discord.Embed(title="Server Marriages", colour=0xFF0000)
                        embed.set_thumbnail(url=self.bot.user.avatar_url)
                        embed.add_field(name="Divorce", value="{} has divorced with {}.".format(me, user.name))
                        await self.bot.send_message(marry_log_channel, embed=embed)
            else:
                msg = 'You can\'t divorce to the user because you aren\'t married to him.'
                em = discord.Embed(description=msg, color=0XF23636)
                await self.bot.say(embed=em)

    async def _create_author(self, server, ctx, user):
        author = ctx.message.author
        if "user" not in self.data:
            self.data["user"] = {}
            dataIO.save_json(self.JSON, self.data)
        if author.id not in self.data["user"]:
            self.data["user"][author.id] = {}
            dataIO.save_json(self.JSON, self.data)
        if "married_to" not in self.data["user"][author.id]:
            self.data["user"][author.id]["married_to"] = {}
            dataIO.save_json(self.JSON, self.data)
        if user.id not in self.data["user"][author.id]["married_to"]:
            self.data["user"][author.id]["married_to"][user.id] = {}
        dataIO.save_json(self.JSON, self.data)



    async def _create_user(self, server, ctx, user):
        author = ctx.message.author
        if "user" not in self.data:
            self.data["user"] = {}
            dataIO.save_json(self.JSON, self.data)
        if user.id not in self.data["user"]:
            self.data["user"][user.id] = {}
            dataIO.save_json(self.JSON, self.data)
        if "married_to" not in self.data["user"][user.id]:
            self.data["user"][user.id]["married_to"] = {}
            dataIO.save_json(self.JSON, self.data)
        if author.id not in self.data["user"][user.id]["married_to"]:
            self.data["user"][user.id]["married_to"][author.id] = {}
        dataIO.save_json(self.JSON, self.data)


    async def _divorce(self, server, ctx, user):
        author = ctx.message.author
        del self.data["user"][author.id]["married_to"][user.id]
        del self.data["user"][user.id]["married_to"][author.id]
        dataIO.save_json(self.JSON, self.data)




def check_folder():
    if not os.path.exists('data/married'):
        print('Creating data/married folder...')
        os.makedirs('data/married')


def check_files():

    f = 'data/married/global_married.json'
    if not dataIO.is_valid_json(f):
        dataIO.save_json(f, {})
        print('Creating default global_married.json...')
    g = "data/married/marriage_settings.json"
    if not dataIO.is_valid_json(g):
        dataIO.save_json(g, {})
        print('Creating default marriage_settings.json...')

def setup(bot):
    check_folder()
    check_files()
    bot.add_cog(marry(bot))
