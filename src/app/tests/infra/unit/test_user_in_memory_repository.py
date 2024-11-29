from domain.user.user_entity import User
from uuid import uuid4
from infra.user.in_memory_user_repository import InMemoryUserRepository

class TestSaveUser:
    # TESTAR O E POSSIVEL SALVAR USUARIOS NO REPOSITORIO
    def test_can_save_user(self):
        repository = InMemoryUserRepository()
        user1 = User(id=uuid4(), name="Test User 1")
        user2 = User(id=uuid4(), name="Test User 2")
        repository.save(user1)
        repository.save(user2)
        assert len(repository.users) == 2
        assert repository.users[0] == user1
        assert repository.users[1] == user2