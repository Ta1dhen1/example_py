from typing import List, Optional
from .models import Project, User, Task

class TaskManager:
    def __init__(self):
        self.projects: List[Project] = []

    def create_project(self, project_name: str) -> Project:
        project_id = len(self.projects) + 1
        project = Project(id=project_id, name=project_name)
        self.projects.append(project)
        return project

    def get_project_by_id(self, project_id: int) -> Optional[Project]:
        return next((p for p in self.projects if p.id == project_id), None)

    def add_user_to_project(self, project_id: int, user: User):
        project = self.get_project_by_id(project_id)
        if not project:
            raise ValueError(f"Project with id {project_id} not found")
        project.users.append(user)

    def add_task_to_project(self, project_id: int, task: Task, user_id: int):
        project = self.get_project_by_id(project_id)
        if not project:
            raise ValueError(f"Project with id {project_id} not found")
        user = next((u for u in project.users if u.id == user_id), None)
        if not user:
            raise ValueError(f"User with id {user_id} not found in project {project_id}")
        project.tasks.append(task)
        user.add_task(task)
