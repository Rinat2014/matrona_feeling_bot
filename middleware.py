from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware
from datetime import datetime, timedelta
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram.types import TelegramObject



# Add middleware Scheduler
class SchedulerMiddleware(BaseMiddleware):
    def __init__(self, scheduler: AsyncIOScheduler):
        self.scheduler = scheduler

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        # add apscheduler to data
        data["apscheduler"] = self.scheduler
        return await handler(event, data)