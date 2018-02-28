import discord
from discord.ext import commands
import asyncio


class Merge:
    """Merge avatars"""

    def __init__(self, bot):
        self.bot = bot

    @commands.group(pass_context=True, invoke_without_command=True)
    @commands.cooldown(1, 5)
    async def merge(self, ctx, *urls:str):
        """Merge/Combine Two Photos"""
        try:
            if urls and 'vertical' in urls:
                vertical = True
            else:
                vertical = False
            get_images = await self.get_images(ctx, urls=urls, limit=20)
            if get_images and len(get_images) == 1:
                await self.bot.say('You gonna merge one image?')
                return
            elif not get_images:
                return
            xx = await self.bot.send_message(ctx.message.channel, "ok, processing")
            count = 0
            list_im = []
            for url in get_images:
                count += 1
                b = await self.bytes_download(url)
                if sys.getsizeof(b) == 215:
                    await self.bot.say(":no_entry: Image `{0}` is invalid!".format(str(count)))
                    continue
                list_im.append(b)
            imgs = [PIL.Image.open(i).convert('RGBA') for i in list_im]
            if vertical:
                max_shape = sorted([(np.sum(i.size), i.size) for i in imgs])[1][1]
                imgs_comb = np.vstack((np.asarray(i.resize(max_shape)) for i in imgs))
            else:
                min_shape = sorted([(np.sum(i.size), i.size) for i in imgs])[0][1]
                imgs_comb = np.hstack((np.asarray(i.resize(min_shape)) for i in imgs))
            imgs_comb = PIL.Image.fromarray(imgs_comb)
            final = BytesIO()
            imgs_comb.save(final, 'png')
            final.seek(0)
            await self.bot.delete_message(xx)
            await self.bot.upload(final, filename='merge.png')
        except Exception as e:
            await self.bot.say(code.format(e))


def setup(bot):
    bot.add_cog(Merge(bot))
