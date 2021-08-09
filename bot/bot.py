import os

from discord import Intents
from discord.ext import commands

from config import KAGGLE_SERVER_ID, MUTE_ROLE_ID

__all__ = (
    'bot',
)

intents = Intents.default()
intents.members = True


class KaggleBot(commands.Bot):
    spam_cache = {}


bot = KaggleBot(command_prefix='k=', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user.name} connected to discord')


async def load_up():
    await bot.wait_until_ready()
    kaggle_guild = bot.get_guild(KAGGLE_SERVER_ID)
    mute_role = kaggle_guild.get_role(MUTE_ROLE_ID)
    bot.kaggle_guild = kaggle_guild
    bot.kaggle_mute_role = mute_role

    for filename in os.listdir('./bot/cogs'):
        if filename.endswith('.py'):
            bot.load_extension(('bot.cogs.' + filename[:-3]))
    print('Finished loading up...')


bot.loop.create_task(load_up())
