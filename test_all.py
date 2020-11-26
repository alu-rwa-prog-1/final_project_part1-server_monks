# Authors: Catherine Muthoni and Liplan Lekipising

import unittest
import datetime
from all_tasks import AllTasks
from assignment_tasks import AssignmentTasks
from class_sessions_tasks import ClasssessionsTasks
from office_hours_tasks import OfficeHoursTasks
from extra_curricular_tasks import ExtraCurricularTasks
from off_campus_tasks import OffCampusTasks
from freezegun import freeze_time


class Test_all(unittest.TestCase):
    def test_name(self):
        x = AllTasks('Task 1', '2020/11/25 12:00')
        self.assertEqual(x.task_name, 'Task 1')
      
    def test_creationdate(self):
        x = AllTasks('Task 1', '2020/11/25 12:00')
        self.assertEqual(x.creation_date.date(), datetime.date(2020, 11, 24))
        
    def test_duedate(self):
        x = AllTasks('Task 1', '2020/11/25 12:00')
        self.assertEqual(x.due_date, datetime.datetime(2020, 11, 25, 12, 0))

    def test_wrongname(self):
        x = AllTasks('Task 1', '2020/11/25 12:00')
        self.assertNotEqual(x.task_name, 'Task 2')

    def test_wrongdue(self):
        x = AllTasks('Task 1', '2020/11/25 12:00')
        self.assertNotEqual(x.due_date, '2020/12/25 12:00')

    def test_complete(self):
        x = AllTasks('Task 1', '2020/11/25 12:00')
        self.assertFalse(x.complete)

    @freeze_time('2020-11-24 09:27:05')
    def test_checktime(self):
        x = AllTasks('Task 1', '2020/11/25 12:00')
        self.assertEqual(x.check_time(), '26 hours 32 minutes')
    
    def test_markcomplete(self):
        x = AllTasks('Task 1', '2020/11/25 12:00')
        x.mark_complete()
        self.assertTrue(x.complete)

    def test_course(self):
        x = AssignmentTasks('Task 1', '2020/11/25 12:00', 'MFC')
        self.assertEqual(x.course, 'MFC')

    def test_groupwork(self):
        x = AssignmentTasks('Task 1', '2020/11/25 12:00', 'MFC')
        self.assertFalse(x.group_work)

    def test_edit(self):
        x = AllTasks('Task 1', '2020/11/25 12:00')
        x.edit_task()  # set new to 'Task 2'
        self.assertEqual(x.task_name, 'Task 2')


if __name__ == '__main__':
    unittest.main()
