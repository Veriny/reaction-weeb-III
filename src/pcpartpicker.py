# import pcpartpicker
import discord
from discord.ext.commands import bot
from discord.ext import commands
# import pcpartpicker
# from pcpartpicker import pcpartpicker

class pcpartpicker(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # pcdata = PCDATA()

    # @commands.command()
    # async def getPCPart(self, ctx, part):
    #     await ctx.send(pcdata.retrieve("{}".format(part)))


def setup(Bot):
    Bot.add_cog(pcpartpicker(Bot))
