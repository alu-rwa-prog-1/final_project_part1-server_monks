import datetime
from all_tasks import All_tasks


class Off_campus_tasks(All_tasks):
    def __init__(self, task_name, due_date, venue, complete=False, creation_date=datetime.datetime.now(), reminder=None):
        super().__init__(task_name, due_date, complete=False, creation_date=datetime.datetime.now(), reminder=None)
        self.venue = venue
