from uuid import uuid4
from domain.user.user_entity import User
import pytest

class TestUser:

	# TESTE PARA CONSTRUIR O USUARIO
	def test_user_initialization(self):
		user_id = uuid4()
		user_name = "Filipe"
		user = User(id=user_id, name=user_name)

		assert user.id == user_id
		assert user.name == user_name

	#TESTE PARA VALIDACAO DO ID DO USUARIO
	def test_user_id_validation(self):
		with pytest.raises(Exception, match="id must be an UUID"):
			User(id="id_invalido", name="Heloisa")

	#TESTE PARA VALIDACAO DO NOME DO USUARIO
	def test_user_name_validation(self):
		user_id = uuid4()
		with pytest.raises(Exception, match="name is required"):
			User(id=user_id, name="")