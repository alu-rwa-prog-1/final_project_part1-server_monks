from all_tasks import All_tasks
import datetime


class Assignment_tasks(All_tasks):
    def __init__(self, task_name, due_date, course, complete=False, creation_date=datetime.datetime.now(), reminder=None, group_work=False):
        super().__init__(task_name, due_date, complete=False, creation_date=datetime.datetime.now(), reminder=None)
        self.course = course
        self.group_work = group_work
