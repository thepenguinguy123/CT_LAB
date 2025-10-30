class Task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority
        self.status = "Pending" 

    def mark_done(self):
        self.status = "Done"
    
    def __str__(self):
        return f"[{self.status}] {self.description} (Priority: {self.priority})"

class TaskManager:
    def __init__(self):
        self.tasks = [] 

    def add_task(self, description, priority):
        self.tasks.append(Task(description, priority))
        print(f"Added task: '{description}' with priority {priority}")
    
    def mark_completed(self, description):
        for task in self.tasks:
            if task.description.lower() == description.lower():
                if task.status == "Done":
                    print(f"Task '{description}' is already completed.")
                else:
                    task.mark_done()
                    print(f"Task '{description}' marked as completed.")
                return
        print(f"Task '{description}' not found.")
    
    def change_priority(self, description, new_priority):
        for task in self.tasks:
            if task.description.lower() == description.lower():
                if task.status == "Done":
                    print(f"Cannot change priority of '{description}' because it is already completed.")
                else:
                    task.priority = new_priority
                    print(f"Priority of '{description}' changed to {new_priority}.")
                return
        print(f"Task '{description}' not found.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return

        print("---Current Task List---")
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")
        print("-----------------------")

manager = TaskManager()

manager.add_task("Finish Python project", "High")
manager.add_task("Read AI research paper", "Medium")
manager.add_task("Go for a walk", "Low")

manager.list_tasks()

manager.mark_completed("Finish Python project")
manager.change_priority("Finish Python project", "Low")
manager.change_priority("Read AI research paper", "High")

manager.list_tasks()