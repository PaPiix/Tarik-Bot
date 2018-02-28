import discord
from discord.ext import commands
from cogs.utils import checks

class HexTools:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @checks.admin_or_permissions(ban_members=True)
    async def hackban(self, ctx, *, user_id: str):
        """Bans users by ID.
        This method does not require the user to be on the server."""

        server = ctx.message.server.id
        try:
            await self.bot.http.ban(user_id, server)
            await self.bot.say("User banned, was <@{}>.".format(user_id))
        except:
            await self.bot.say("Failed to ban. Either `Lacking Permissions` or `User cannot be found`.")


def setup(bot):
    bot.add_cog(HexTools(bot))
