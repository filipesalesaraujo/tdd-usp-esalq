from abc import ABC, abstractmethod
from domain.user.user_entity import User

class UserRepositoryInterface(ABC):
	@abstractmethod
	def save(self, user) -> None:
		raise NotImplementedError