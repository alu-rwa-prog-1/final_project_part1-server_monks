from all_tasks import All_tasks
import datetime


class Class_sessions_tasks(All_tasks):
    def __init__(self, task_name, due_date, course, platform, facilitator, complete=False, creation_date=datetime.datetime.now(), reminder=None):
        super().__init__(task_name, due_date, complete=False, creation_date=datetime.datetime.now(), reminder=None)
        self.course = course
        self.platform = platform
        self.facilitator = facilitator
