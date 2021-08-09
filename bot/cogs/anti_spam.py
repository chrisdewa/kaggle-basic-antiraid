from datetime import datetime, timedelta

import discord
from discord.ext.commands import Cog

from config import KAGGLE_SERVER_ID, SPAM_TIME, SPAM_AMOUNT
from modules.database.members import MemberModel


class AntiSpamCog(Cog, name='anti-spam-cog'):
    def __init__(self, bot):
        self.bot = bot
        print(f'[+] {self.qualified_name} loaded')

    async def cog_unload(self):
        print(f'[-] {self.qualified_name} unloaded')

    @Cog.listener('on_message')
    async def spam_block(self, message: discord.Message):
        if not message.guild or message.guild.id != KAGGLE_SERVER_ID:
            return

        member = message.author
        member_db = await MemberModel.get(True, member_id=member.id)

        member_cache = self.bot.spam_cache.setdefault(member.id, [])
        member_cache.append(message)

        last_msgs = member_cache[-SPAM_AMOUNT:]

        if len(last_msgs) == SPAM_AMOUNT:
            delta = (last_msgs[-1].created_at - last_msgs[0].created_at).total_seconds()
            if delta >= SPAM_TIME:
                # user is spamming. proceed to mute 1 minute
                now = datetime.utcnow()
                member_db.muted_on = now
                member_db.unmute_on = now + timedelta(minutes=1)
                await member.add_roles(self.bot.kaggle_mute_role)
                await member_db.save()


def setup(bot):
    bot.add_cog(AntiSpamCog(bot))
