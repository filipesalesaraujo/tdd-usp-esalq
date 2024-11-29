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


class TestGetUserById:
    # TESTAR SE E POSSIVEL RETORNAR UM USUARIO PELO ID DELE
    def test_can_get_user_by_id(self):
        repository = InMemoryUserRepository()
        user1 = User(id=uuid4(), name="Test User 1")
        user2 = User(id=uuid4(), name="Test User 2")
        repository.save(user1)
        repository.save(user2)

        user = repository.get_by_id(user1.id)
        assert user.id == user1.id
        assert user.name == user1.name
