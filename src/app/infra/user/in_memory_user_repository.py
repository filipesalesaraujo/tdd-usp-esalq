from domain.user.user_entity import User
from domain.user.user_repository_interface import UserRepositoryInterface

class InMemoryUserRepository(UserRepositoryInterface):
	
	def __init__(self):
		self.users:list[User] = [] 
	
	def save(self, user: User) -> None:
		self.users.append(user)