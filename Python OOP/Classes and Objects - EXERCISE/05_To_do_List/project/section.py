class Section:
    def __init__(self, name:str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task):
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"
        return f"Task is already in the section {self.name}"

    def complete_task(self, task_name:str):
        for task in self.tasks:
            if task_name == task.name:
                task.completed = True
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        amount_tasks = 0
        for task in self.tasks:
            if task.completed:
                amount_tasks += 1
                self.tasks.remove(task)
        return f"Cleared {amount_tasks} tasks."


    def view_section(self):
        data = '\n'.join([task.details() for task in self.tasks])
        return f"Section {self.name}:\n{data}"
