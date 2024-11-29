from infra.user.in_memory_user_repository import InMemoryUserRepository
from application.user.create_user_use_case import (
    CreateUserUseCase,
    CreateUserRequest,
)
from uuid import UUID


class TestCreateUser:
    # TESTE PARA CRIAR UM USUARIO COM DADOS VALIDOS
    def test_create_user_with_valid_data(self):
        repository = InMemoryUserRepository()

        use_case = CreateUserUseCase(repository=repository)

        request = CreateUserRequest(name="Test User")

        response = use_case.execute(request)
        assert len(repository.users) == 1
        assert isinstance(response.id, UUID)
        persited_user = repository.users[0]
        assert persited_user.id == response.id
        assert persited_user.name == "Test User"
