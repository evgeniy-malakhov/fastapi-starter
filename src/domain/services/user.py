from fastapi import Depends

from src.domain.entities.user import User
from src.infrastructure.repositories.user_repository_impl import UserRepositoryImpl


class UserService:
    def __init__(self, user_repository: UserRepositoryImpl = Depends()):
        self.user_repository = user_repository

    async def get_all_users(self) -> list[User]:
        return await self.user_repository.get_all_users()