import discord
from discord import Object
from __main__ import settings
from random import randint
from random import choice
tarikslogging = Object("305674037202518016")

class Globallogging:
    """Logs the bot's commands globally."""
    def __init__(self, bot):
        self.bot = bot
        self.commands = [command for command in self.bot.commands]



    async def on_message(self, message):
        if message.author.id == self.bot.user.id:
            return
        prefixes = self.bot.settings.get_prefixes(message.server)
        for prefix in prefixes:
            if message.content.startswith(prefix):
                if message.content.replace(prefix, "").split(' ', 1)[0] in self.commands:
                    colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
                    colour = int(colour, 16)
                    author = message.author
                    embed = discord.Embed(colour=discord.Colour(value=colour))
                    embed.add_field(name="Server", value = "{}".format(message.server.name))
                    embed.add_field(name="Server Owner", value="{}".format(message.server.owner))
                    embed.add_field(name="Server Users", value=len(message.server.members))
                    embed.add_field(name="Channel", value = "#{}".format(message.channel.name))
                    embed.add_field(name="User ID", value="__{}__".format(author.id), inline=True)
                    embed.add_field(name="Server ID", value="__{}__".format(message.server.id), inline=True)
                    embed.add_field(name="Channel ID", value="__{}__".format(message.channel.id), inline=True)
                    embed.add_field(name="Server Owner ID", value="__{}__".format(message.server.owner.id), inline=True)
                    embed.set_author(name="{}".format(message.content), icon_url=self.bot.user.avatar_url)
                    embed.set_footer(text="Sent by: {}".format(author), icon_url=author.avatar_url)
                    embed.set_thumbnail(url=message.server.icon_url)

                    await self.bot.send_message(tarikslogging, embed=embed)



def setup(bot):
    bot.add_cog(Globallogging(bot))
