import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_message(message):
    if message.content == "Vem har rätt?":
        await bot.send_message(message.channel, "Jag håller med <@282858592472793089>")

bot.run("NDgxOTMwODUxNTQyODkyNTQ0.Dl_udg.8_18sqdsOsKUDVI_gTdc0wWHXB0")
