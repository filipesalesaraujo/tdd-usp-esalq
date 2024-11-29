from unittest.mock import MagicMock
from domain.user.user_repository_interface import UserRepositoryInterface
from application.user.create_user_use_case import CreateUserUseCase, CreateUserRequest, CreateUserResponse
from uuid import UUID

class TestCreateUser:
    # TESTE PARA CRIAR UM USUARIO COM DADOS VALIDOS
    def test_create_user_with_valid_data(self):
        mock_repository = MagicMock(UserRepositoryInterface)

        use_case = CreateUserUseCase(repository=mock_repository)

        request = CreateUserRequest(name="Test User")

        response = use_case.execute(request)

        assert response.id is not None
        assert isinstance(response, CreateUserResponse)
        assert isinstance(response.id, UUID)
        assert mock_repository.save.called is True
