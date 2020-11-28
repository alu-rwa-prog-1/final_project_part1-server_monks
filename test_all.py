# Authors: Catherine Muthoni and Liplan Lekipising

import unittest
import datetime
from all_tasks import AllTasks
from assignment_tasks import AssignmentTasks
from class_sessions_tasks import ClassSessionsTasks
from office_hours_tasks import OfficeHoursTasks
from extra_curricular_tasks import ExtraCurricularTasks
from off_campus_tasks import OffCampusTasks
from freezegun import freeze_time

print()
print("""Testing Instructions:
Two tests are user input dependent.
-> edit task name, enter new task name as Task 2, enter no for prompt on changing due date.
-> set reminder, enter reminder date as, 2020/12/11 12:00""")
print()

class Test_all(unittest.TestCase):
    def test_name(self):
        x = AllTasks('Task 1', '2020/11/25 12:00')
        self.assertEqual(x.task_name, 'Task 1')

    @freeze_time('2020-11-26 09:27:05')  
    def test_creationdate(self):
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

    def test_edit(self):  # enter new task name as Task 2
        x = AllTasks('Task 1', '2020/11/25 12:00')
        print()
        x.edit_task()  # set new to 'Task 2'
        print()
        self.assertEqual(x.task_name, 'Task 2')


class Test_assignment(unittest.TestCase):
    def test_course(self):
        x = AssignmentTasks('Task 1', '2020/11/25 12:00', 'MFC')
        self.assertEqual(x.course, 'MFC')

    def test_groupwork(self):
        x = AssignmentTasks('Task 1', '2020/11/25 12:00', 'MFC')
        self.assertFalse(x.group_work)

    def test_platform(self):
        x = OfficeHoursTasks('OH for MFC', '2020/12/3 12:00', 'MFC', 'zoom', 'Imali')
        self.assertEqual(x.platform, 'zoom')
    
    def test_ta(self):
        x = OfficeHoursTasks('OH for MFC', '2020/12/3 12:00', 'MFC', 'zoom', 'Imali')
        self.assertNotEqual(x.teaching_assistant, 'Gilbert')


class Test_off(unittest.TestCase):
    def test_set(self):  # enter reminder date as: 2020/12/10 12:00
        x = OffCampusTasks('Visit friend A', '2020/12/14 12:00', 'Kigali')
        print()
        x.set_reminder()
        print()
        self.assertEqual(x.reminder, datetime.datetime(2020, 12, 10, 12, 0, 0, 0))


class Test_extra(unittest.TestCase):
    def test_mark(self):
        x = ExtraCurricularTasks('Club Meeting', '2020/12/25 13:00', 'Botswana room')
        x.mark_complete()
        self.assertTrue(x.complete)

class Test_class(unittest.TestCase):
    def test_platform(self):
        x = ClassSessionsTasks('Task 1', '2020/11/29 12:00', 'MFC', 'Meet', 'Arun')
        self.assertEqual(x.platform, 'Meet')


if __name__ == "__main__":
    unittest.main()