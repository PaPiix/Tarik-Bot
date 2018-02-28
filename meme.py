import discord
import asyncio
import aiohttp
from discord.ext import commands
from io import BytesIO, StringIO

class Meme:
    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession()

    async def bytes_download(self, url:str):
        try:
            with aiohttp.Timeout(5):
                async with self.session.get(url) as resp:
                    data = await resp.read()
                    b = BytesIO(data)
                    b.seek(0)
                    return b
        except asyncio.TimeoutError:
            return False
        except Exception as e:
            print(e)
            return False

    @commands.group(pass_context=True, invoke_without_command=True)
    async def meme(self, ctx, meme:str=None, *, line=None):
        """Generates a meme."""
        if meme is None:
            embed=discord.Embed(title="Meme", description="Generate a meme from a link or user.", colour=0xFF0000) 
            embed.set_thumbnail(url='https://memegen.link/saltbae/tariks/meme-generator.jpg')
            embed.add_field(name="Example 1:", value=".meme @TTxFTW text", inline=False)
            embed.add_field(name="Example 2:", value=".meme <link> text", inline=True)
            await self.bot.say(embed=embed)
            return
        if line is None:
            embed=discord.Embed(title="Error:", description="meme has 4 parameters .meme <template> <line_one> <line_two> <style> = Optional", colour=0xFF0000) 
            await self.bot.say(embed=embed)
            return
        line2 = None
        if '|' in line:
            split = line.split('|')
            line1 = split[0]
            line2 = split[1]
        else:
            split = line.split()
            if len(split) > 2:
                line1 = ' '.join(split[:2])
                line2 = ' '.join(split[2:])
            else:
                line1 = split[0]
                if len(split) > 1:
                    line2 = ' '.join(split[1:])
        if line2 is None:
            line2 = ''
        rep = [["-","--"],["_","__"],["?","~q"],["%","~p"],[" ","%20"],["''","\""]]
        for s in rep:
            line1 = line1.replace(s[0],s[1])
            line2 = line2.replace(s[0],s[1])
        if len(ctx.message.mentions):
            link = "http://memegen.link/custom/{0}/{1}.jpg?alt={2}".format(line1, line2, 'https://discordapp.com/api/users/{0.id}/avatars/{0.avatar}.jpg'.format(ctx.message.mentions[0]))
            b = await self.bytes_download(link)
        elif meme.startswith("http"):
            link = "http://memegen.link/custom/{0}/{1}.jpg?alt={2}".format(line1, line2, meme)
            b = await self.bytes_download(link)
        else:
            link = "http://memegen.link/{0}/{1}/{2}.jpg".format(meme, line1, line2)
            b = await self.bytes_download(link)
        if b is False:
            await self.bot.say(':warning: **Command download function failed...**')
            return
        await self.bot.upload(b, filename='meme.png')

def setup(bot):
    n = Meme(bot)
    bot.add_cog(n)