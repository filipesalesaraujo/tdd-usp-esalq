from fastapi import APIRouter, HTTPException
from application.user.create_user_use_case import CreateUserUseCase, CreateUserRequest, CreateUserResponse
from infra.user.in_memory_user_repository import InMemoryUserRepository

router = APIRouter(prefix="/users")
repository = InMemoryUserRepository()

repository = InMemoryUserRepository()

@router.post("/")
def create_user(request: CreateUserRequest):
		try:
			usecase = CreateUserUseCase(repository)
			response = usecase.execute(request)
			return response
		except Exception as e:
			raise HTTPException(status_code=404, detail=str(e))
			
