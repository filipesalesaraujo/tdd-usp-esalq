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

    # testar se o metodo get_by_id do InMemoryUserRepository esta retornando o usuario correto
    def test_when_user_does_not_exist_should_return_none(self):
        repository = InMemoryUserRepository()
        user1 = User(id=uuid4(), name="Test User 1")
        user2 = User(id=uuid4(), name="Test User 2")
        repository.save(user1)
        repository.save(user2)
        user = repository.get_by_id(user_id=uuid4())
        assert user == None


class TestUpdateUser:

    # TESTE PARA TESTAR SE E POSSIVEL ATUALZIAR O NOME DE UM USUARIO
    def test_update_user(self):
        repository = InMemoryUserRepository()
        user1 = User(id=uuid4(), name="Test User 1")
        user2 = User(id=uuid4(), name="Test User 2")
        repository.save(user1)
        repository.save(user2)
        user1.name = "Test User 1 Updated"
        repository.update(user1)
        updated_user = repository.get_by_id(user_id=user1.id)
        assert updated_user.name == "Test User 1 Updated"
