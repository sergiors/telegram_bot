from enum import Enum
from dataclasses import dataclass

from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message
from telebot.asyncio_handler_backends import BaseMiddleware, CancelUpdate


class Role(str, Enum):
    ADMIN = 'ADMIN'
    USER = 'USER'


@dataclass
class User:
    id: str
    name: str
    role: Role = Role.USER


ADMIN = User(id='132203844', name='Sérgio', role=Role.ADMIN)
USERS = [ADMIN, User(id='5790500892', name='Isadora')]


class AuthMiddleware(BaseMiddleware):
    def __init__(self, bot: AsyncTeleBot, users: list[User]) -> None:
        self.bot = bot
        self.users = [user.id for user in users]
        self.update_types = ['message']

    async def pre_process(self, message: Message, data):
        user_id = str(message.from_user.id)
        users = self.users

        if user_id in users:
            return

        await self.bot.send_message(message.chat.id, '🤖 Sem permissão.')
        return CancelUpdate()

    async def post_process(self, message, data, exception):
        pass
