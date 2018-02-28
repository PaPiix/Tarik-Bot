import discord
import traceback
class Serverjoinlimit:
    def __init__(self, bot):
        self.bot = bot
        
    async def on_server_join(self, server):
        if len(server.members) <= 10:
            try:
                await self.bot.send_message(server.default_channel, "I can only join servers which have more than 10 members. Sorry but I have to leave now, bye :wave:")
            except:
                traceback.print_exc()
            await self.bot.leave_server(server)
        
        else:
            pass
        
def setup(bot):
    bot.add_cog(Serverjoinlimit(bot))       