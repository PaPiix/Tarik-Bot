import discord
from discord.ext import commands
import random

class Penis:
    """Penis related commands."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, invoke_without_command=True)
    async def penis(self, ctx, user : discord.Member = None):
        """Detects user's penis length

        This is 100% accurate."""

        bigpenis = ['152802677867282432', '173102900514521089', '166179284266778624', '203649661611802624', '265938036481720321', '251466318824472588', '210919337953853440','162653659555954688', '287156649871802368', '218817800674869248', '166567027455033345', '226479704536907776', '213210505932832770']
        nopenis = ['270671188546682880', '256623018523099136', '240533315956768768', '156118646664462336', '239388225028751361']
        smallpenis = ['203843262891425794', '218459285376598016', '157855300198596610']

        if not user:
           embed=discord.Embed(title="Penis", description="Detects a users penis length!\n\nThis is 100% accurate!")
           embed.set_thumbnail(url='https://image.spreadshirtmedia.net/image-server/v1/compositions/105230521/views/1,width=300,height=300,version=1478003241/cheeky-penis-t-shirts-men-s-t-shirt.jpg')
           embed.add_field(name=".penis @user", value="Example: .penis @TTxFTW", inline=True)
           await self.bot.say(embed=embed)
        
        elif user.id in bigpenis:
           p = "8" + "="*1900 + "D"
           await self.bot.say("**Size:** " + p)
        
        elif user.id in nopenis:
           await self.bot.say("__***ERROR 404***__: __This user does not have a penis lmfao.__")
           
        elif user.id in smallpenis:
            await self.bot.say("**Size:** 8D")      
        
        else:
           random.seed(user.id)
           p = "8" + "="*random.randint(0, 30) + "D"
           await self.bot.say("**Size:** " + p)

def setup(bot):
    bot.add_cog(Penis(bot))
