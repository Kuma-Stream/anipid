import asyncio
from pyrogram import idle
from . import anibot, has_user, session
from .utils.db import _close_db

user = None
if has_user:
    from . import user

async def main():
    async with asyncio.gather(
        anibot.start(),
        user.start() if user is not None else asyncio.sleep(0)
    ) as gather_tasks:
        await asyncio.wait(gather_tasks)

    await idle()

    await anibot.stop()
    if user is not None:
        await user.stop()
    _close_db()
    await session.close()

if __name__ == '__main__':
    asyncio.run(main())
