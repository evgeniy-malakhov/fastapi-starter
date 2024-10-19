from fastapi import APIRouter
from fastapi.params import Depends

from src.domain.entities.user import User
from src.domain.services.user import UserService

router = APIRouter()

"""
Maybe need to create function to passthrough user_repository_impl here
something like:

def get_notification_service(db: AsyncSession = Depends(get_db)):
    repository = NotificationRepositoryImpl(db)
    return NotificationService(repository)
"""
@router.get("/", response_model=list[User])
async def get_all_users(user_service: UserService = Depends()):
    return await user_service.get_all_users()