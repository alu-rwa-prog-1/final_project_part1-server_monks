# Authors: Catherine Muthoni and Liplan Lekipising

from all_tasks import AllTasks
import datetime


class AssignmentTasks(AllTasks):
    def __init__(self, task_name, due_date, course, complete=False, creation_date=datetime.datetime.now(), reminder=None, group_work=False):
        super().__init__(task_name, due_date, complete=False, creation_date=datetime.datetime.now(), reminder=None)
        self.course = course
        self.group_work = group_work
