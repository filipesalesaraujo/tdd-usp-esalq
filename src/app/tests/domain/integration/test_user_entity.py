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

    # TESTE PARA CONTABILIZAR TAREFAS PENDENTES DE UM USUARIO
    def test_count_pending_tasks(self):
        user = User(id=uuid4(), name="Test User")
        task1 = Task(id=uuid4(), user_id=user.id, title="Task 1", description="Task 1 description", completed=False)
        task2 = Task(id=uuid4(), user_id=user.id, title="Task 2", description="Task 2 description", completed=False)
        task3 = Task(id=uuid4(), user_id=user.id, title="Task 3", description="Task 3 description", completed=False)

        user.collect_task([task1, task2, task3])

        pending_count = user.count_pending_tasks()
        assert pending_count == 3

		# TESTE PARA CONTABILIZAR TAREF
    def test_count_pending_tasks_empty(self):
        user = User(id=uuid4(), name="Test User")
        count_pending_tasks = user.count_pending_tasks()
        assert count_pending_tasks == 0

		# TESTAR QUANDO TODAS AS MINHAS TAREFAS ESTAO COMPLETADAS
    def test_count_pending_tasks_all_completed(self):
        user = User(id=uuid4(), name="Test User")
        task1 = Task(id=uuid4(), user_id=user.id, title="Task 1", description="Task 1 description", completed=False)
        task2 = Task(id=uuid4(), user_id=user.id, title="Task 2", description="Task 2 description", completed=False)
        task3 = Task(id=uuid4(), user_id=user.id, title="Task 3", description="Task 3 description", completed=True)

        user.collect_task([task1, task2, task3])

        user.tasks[0].mark_as_completed()
        user.tasks[1].mark_as_completed()

        count_pending_tasks = user.count_pending_tasks()

        assert count_pending_tasks == 0