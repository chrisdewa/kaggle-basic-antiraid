import asyncio
from datetime import datetime

from discord.ext import tasks
from discord.ext.commands import Cog
from odmantic import field

from modules.database import MemberModel
from modules.database import engine


class MuteCog(Cog, name='mute-cog'):
    def __init__(self, bot):
        self.bot = bot
        self.auto_unmute.start()
        print(f'[+] {self.qualified_name} loaded')

    async def cog_unload(self):
        self.auto_unmute.cancel()
        print(f'[-] {self.qualified_name} unloaded')

    @tasks.loop(seconds=5)
    async def auto_unmute(self):
        member_dbs = await engine.find(MemberModel, field.ne(MemberModel.unmute_on, None))
        now = datetime.utcnow()
        muted_members = [
            m for m in self.bot.kaggle_guild.members
            if self.bot.kaggle_mute_role in m.roles
            and m.id in [mdb.member_id for mdb in member_dbs]
        ]

        async def unmute(member):
            mdb = next(m for m in member_dbs if m.member_id == member.id)
            if now > mdb.unmute_on:
                mdb.unmute_on = None
                await member.remove_roles(self.bot.kaggle_mute_role)
                await mdb.save()

        await asyncio.gather(
            *[unmute(m) for m in muted_members]
        )


def setup(bot):
    bot.add_cog(MuteCog(bot))
