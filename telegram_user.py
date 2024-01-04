from dataclasses import dataclass
from enum import Enum


class Role(str, Enum):
    ADMIN = 'ADMIN'
    USER = 'USER'


@dataclass
class User:
    id: str
    name: str
    role: Role = Role.USER


USERS = [
    User(id='132203844', name='Sérgio', role=Role.ADMIN),
    User(id='5790500892', name='Isadora'),
]
