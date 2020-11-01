from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_massage(massage):
    try:
        if massage.author.bot:
            return
        await bot.process_commands(massege)
    except Exeption:
        await massege.channel.send(f'```\n{traceback.format_exc()}\n```')
                           
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

    
bot.run(token)
