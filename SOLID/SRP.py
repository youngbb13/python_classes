'''Single Responsibility Principle'''

class Task:
    def __init__(self, description):
        self.description = description

class TaskManager:
    def delete_task(self, task):
        self.task = "delete task"

'''Один клас — одна відповідальність'''