# Authors: Catherine Muthoni and Liplan Lekipising

from all_tasks import AllTasks
import datetime


class ExtraCurricularTasks(AllTasks):
    def __init__(self, task_name, due_date, platform_venue, complete=False, creation_date=datetime.datetime.now(), reminder=None):
        super().__init__(task_name, due_date, complete=False, creation_date=datetime.datetime.now(), reminder=None)
        self.platform_venue = platform_venue
