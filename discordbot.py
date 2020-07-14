from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['NzAxMzQ2MTg2ODQ5NjgxNDQ5.Xw2lHg.puQvlQM94MB8TdhsJv2O1Se2tRs']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def hello(ctx):
    await ctx.send('Hey,guys.We have gift for you')


bot.run(token)
