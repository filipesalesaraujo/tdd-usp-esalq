from abc import ABC, abstractmethod
from domain.user.user_entity import User
from uuid import UUID
class UserRepositoryInterface(ABC):
	@abstractmethod
	def save(self, user) -> None:
		raise NotImplementedError
	
	@abstractmethod
	def get_by_id(self, user_id:UUID) -> User:
		raise NotImplementedError