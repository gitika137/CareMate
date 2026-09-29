class Task:
    def __init__(self, name, subject, priority):
        self.name = name
        self.subject = subject
        self.priority = priority
        self.completed = False

    def complete(self):
        self.completed = True