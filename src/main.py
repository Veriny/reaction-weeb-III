import discord
from discord.ext import commands
import os
import traceback
import sys

extensions = ['imgmaker']
bot = commands.Bot(command_prefix = "!")

@bot.event
async def on_ready():
    print("Reaction-Weeb is ready!")

@bot.event
async def on_command_error(ctx, error):
        """The event triggered when an error is raised while invoking a command.
        ctx   : Context
        error : Exception"""

        # This prevents any commands with local handlers being handled here in on_command_error.
        if hasattr(ctx.command, 'on_error'):
            return

        ignored = (commands.CommandNotFound, commands.UserInputError)

        # Allows us to check for original exceptions raised and sent to CommandInvokeError.
        # If nothing is found. We keep the exception passed to on_command_error.
        error = getattr(error, 'original', error)

        # Anything in ignored will return and prevent anything happening.
        if isinstance(error, ignored):
            return

        elif isinstance(error, commands.DisabledCommand):
            return await ctx.send(f'{ctx.command} has been disabled.')

        elif isinstance(error, commands.NoPrivateMessage):
            try:
                return await ctx.author.send(f'{ctx.command} can not be used in Private Messages.')
            except:
                pass
        tb_list = traceback.format_exception(etype=type(error), value=error, tb=error.__traceback__)
        tb = ""
        for line in tb_list:
            tb += line
        await ctx.send("****__ERROR__****: \n `" + tb + "`")
        # await ctx.send("ERROR: `" + traceback.extract_tb(type(error), error, error.__traceback__, file=sys.stderr) + "`" )

@bot.command()
async def load(ctx, cogname):
    if ctx.author.id == 187733221591482370 or ctx.author.id == 383116010971987971:
        try:
            bot.load_extension(cogname)
            await ctx.send("Loaded {}".format(cogname))

        except Exception as e:
            await ctx.send("Unable to load that cog. `{}`".format(str(e)))
    else:
        await ctx.send("Only Justin can use that command! This incident will be reported.")

@bot.command()
async def reload(ctx, cogname):
    if ctx.author.id == 187733221591482370 or ctx.author.id == 383116010971987971:
        try:
            bot.reload_extension(cogname)
            await ctx.send("Reloaded {}".format(cogname))
        except Exception as e:
            await ctx.send("Unable to reload that cog. `{}`".format(str(e)))
    else:
        await ctx.send("Only Justin can use that command! This incident will be reported")

for ext in extensions:
    bot.load_extension(ext)

bot.run("NjIyMTMwMzY4Mzc5ODc5NDI1.Xg0FHg.4SaB9cmHgfIOo_BjUY9zIXgAJAo")
