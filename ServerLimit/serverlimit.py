import discord
import traceback
class Serverjoinlimit:
    def __init__(self, bot):
        self.bot = bot
        
    # This is a cog I made for Tarik Bot which basically makes the bot leave any server that has less than 25 members when it joins.
	
	async def on_server_join(self, server):
        if len(server.members) <= 25:
            try:
                await self.bot.send_message(server.default_channel, "I can only join servers which have more than 10 members. Sorry but I have to leave now, bye :wave:")
            except:
                traceback.print_exc()
            await self.bot.leave_server(server)
        
        else:
            pass
        
def setup(bot):
    bot.add_cog(Serverjoinlimit(bot))       
