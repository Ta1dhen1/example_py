import pytest
from task_manager.models import Task, User, Project
from task_manager.services import TaskManager

def test_create_project():
    manager = TaskManager()
    project = manager.create_project("Test Project")
    assert project.name == "Test Project"
    assert len(manager.projects) == 1
