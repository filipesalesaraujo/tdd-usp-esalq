from domain.user.user_entity import User
from domain.user.user_repository_interface import UserRepositoryInterface
from uuid import UUID
class InMemoryUserRepository(UserRepositoryInterface):
	
	def __init__(self):
		self.users:list[User] = [] 
	
	def save(self, user: User) -> None:
		self.users.append(user)

	def get_by_id(self, user_id: UUID) -> User:
		for user in self.users:
			if user.id == user_id:
				return user
		return None