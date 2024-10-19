from src.domain.entities.user import User
from src.domain.repositories.user import UserRepository


class UserRepositoryImpl(UserRepository):
    async def get_all_users(self) -> list[User]:
        return [User(**{"id": 1, "name": "admin", "email": "admin@example.com"})]