import discord
from discord.ext import commands

from TOKEN import TOKEN

bot = commands.Bot(commands.when_mentioned_or("~"), intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f"{bot.user} successfully logged in")


@bot.command(aliases=['say'])
async def say(ctx, arg):

    if arg != None:
        await ctx.send(arg)
        return

    await ctx.send('Du hast nicht angegeben, was ich sagen soll.')


bot.run(TOKEN)
