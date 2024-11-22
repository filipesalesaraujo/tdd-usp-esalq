from uuid import uuid4
from domain.task.task_entity import Task
import pytest

class TestTask:

	#TESTE PARA VERIFICAR O CONSTRUTOR DA CLASSE TAREFA
	def test_task_initialization(self):
		task_id = uuid4()
		user_id = uuid4()
		title = "Estudar mais sobre testes unitarios."
		description = "Os testes unitarios sao os maiis baratos."
		completed = False

		task = Task(
			id=task_id,
			user_id=user_id,
			title=title,
			description=description,
			completed=completed
		)

		assert task.id == task_id
		assert task.user_id == user_id
		assert task.title == title
		assert task.description == description
		assert task.completed == completed

	#TESTE PARA VALIDAR O ID DA TAREFA
	def test_task_id_validation(self):
		user_id = uuid4()
		with pytest.raises(Exception, match="id must be an UUID"):
			Task(
				id=1,
				user_id=user_id,
				title="Estudar mais sobre testes unitarios.",
				description="Os testes unitarios sao os mais baratos.",
				completed=False
			)

	#TESTE PARA VALIDAR O ID DO USUARIO
	def test_tast_user_id_validation(self):
		task_id = uuid4()
		with pytest.raises(Exception, match="user_id must be an UUID"):
			Task(
				id=task_id,
				user_id=1,
				title="Estudar mais sobre testes unitarios.",
				description="Os testes unitarios sao os mais baratos.",
				completed=False
			)

	#TESTE PARA VALIDAR O TITULO DA TAREFA
	def test_task_title_validation(self):
		task_id = uuid4()
		user_id = uuid4()
		with pytest.raises(Exception, match="title is required"):
			Task(
				id=task_id,
				user_id=user_id,
				title="",
				description="Os testes unitarios sao os mais baratos.",
				completed=False
			)

	#TESTE PARA VALIDAR A DESCRICAO DA TAREFA
	def test_task_description_validation(self):
		task_id = uuid4()
		user_id = uuid4()
		with pytest.raises(Exception, match="description is required"):
			Task(
				id=task_id,
				user_id=user_id,
				title="Estudar mais sobre testes unitarios.",
				description="",
				completed=False
			)

	#TESTE PARA VALIDAR O STATUS DA TAREFA
	def test_task_completed_validation(self):
		task_id = uuid4()
		user_id = uuid4()
		with pytest.raises(Exception, match="invalid completed status: must be a boolean"):
			Task(
				id=task_id,
				user_id=user_id,
				title="Estudar mais sobre testes unitarios.",
				description="Os testes unitarios sao os mais baratos.",
				completed="not_boolean"
			)

	#TESTE PARA VALIDAR A TAREFA COMPLETA COM UMA FUNCAO mark_as_completed
	def test_mark_as_completed(self):
		task = Task(
			id=uuid4(),
			user_id=uuid4(),
			title="Estudar mais sobre testes unitarios.",
			description="Os testes unitarios sao os mais baratos.",
			completed=False
		)

		task.mark_as_completed()

		assert task.completed == True