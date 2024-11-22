from domain.user.user_entity import User
from domain.task.task_entity import Task
from uuid import uuid4

class TestUserWithTasks:
	# TESTE PARA ADICIONAR TAREFAS AO USUARIO
	def test_collect_tasks(self):
		user = User(id=uuid4(), name="Test User")
		task1 = Task(id=uuid4(), user_id=user.id, title="Task 1", description="Task 1 description", completed=False)
		task2 = Task(id=uuid4(), user_id=user.id, title="Task 2", description="Task 2 description", completed=False)
		user.collect_task([task1, task2])

		assert len(user.tasks) == 2
		assert task1 in user.tasks
		assert task2 in user.tasks