from task_manager.models import Task, User
from task_manager.services import TaskManager

manager = TaskManager()
project = manager.create_project("Example Project")
user = User(id=1, name="Alice", email="alice@example.com")
manager.add_user_to_project(project.id, user)
task = Task(id=1, title="Example Task", description="This is a test task")
manager.add_task_to_project(project.id, task, user.id)
print(f"Project: {project}")
