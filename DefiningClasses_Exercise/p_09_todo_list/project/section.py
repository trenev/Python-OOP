class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        filtered_tasks = [element for element in self.tasks if element.name == task_name]
        try:
            filtered_tasks[0].completed = True
            return f"Completed task {task_name}"
        except IndexError:
            return f"Could not find task with the name {task_name}"

    def clean_section(self):
        completed_tasks = list(filter(lambda x: x.completed, self.tasks))
        self.tasks = list(filter(lambda x: not x.completed, self.tasks))
        return f"Cleared {len(completed_tasks)} tasks."

    def view_section(self):
        result = f"Section {self.name}:\n"
        for element in self.tasks:
            result += f"{element.details()}\n"
        return result
