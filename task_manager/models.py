from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional

@dataclass
class Task:
    id: int
    title: str
    description: str
    created_at: datetime = field(default_factory=datetime.now)
    due_date: Optional[datetime] = None
    completed: bool = False

    def mark_completed(self):
        self.completed = True

@dataclass
class User:
    id: int
    name: str
    email: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        self.tasks.append(task)

@dataclass
class Project:
    id: int
    name: str
    users: List[User] = field(default_factory=list)
    tasks: List[Task] = field(default_factory=list)
