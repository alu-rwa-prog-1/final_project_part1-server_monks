# Authors: Catherine Muthoni and Liplan Lekipising

from all_tasks import AllTasks
from assignment_tasks import AssignmentTasks
from class_sessions_tasks import ClasssessionsTasks
from office_hours_tasks import OfficeHoursTasks
from extra_curricular_tasks import ExtraCurricularTasks
from off_campus_tasks import OffCampusTasks
import datetime
import sched, time

# Welcome message and instructions
print("""Hi, welcome to your to-do program. We care about your productivity.
This program enables you to:
- Add tasks while specifying type
- edit tasks
- check time remaining for any task
- set reminder for any task""")
print()

# Hold all tasks created in a dictionary and nested dictionaries
my_tasks = {'assignment': {}, 'class': {}, 'office': {}, 'extra': {}, 'off': {}}

task_no = 100  # task ID start at 100

# While loop, runs as long user want to create an task
while True:
    get_type = input('Enter type off task to add: assignment, class, office, extra, off: ').lower()
    print()
    if get_type == 'assignment':
        get_name1 = input('Enter task name: ')
        get_due_date1 = input('Enter the due date in this format: YYYY/MM/DD H:M ')
        get_course1 = input('Enter the course: ')
        my_tasks['assignment']['T' + str(task_no)] = AssignmentTasks(get_name1, get_due_date1, get_course1)
        print('Assignment task created successfully with id T' + str(task_no))
        print(task_no)
    elif get_type == 'class':
        get_name2 = input('Enter task name: ')
        get_due_date2 = input('Enter the date for the class in this format: YYYY/MM/DD H:M ')
        get_course2 = input('Enter the course: ')
        get_platform2 = input('Enter the online platform for the class: ')
        get_facilitator2 = input('Enter the facilitator name: ')
        my_tasks['class']['T' + str(task_no)] = ClasssessionsTasks(get_name2, get_due_date2, get_course2, get_platform2,
                                                                   get_facilitator2)
        print('Class session task created successfully with id T' + str(task_no))
        print(task_no)
    elif get_type == 'office':
        get_name3 = input('Enter task name: ')
        get_due_date3 = input('Enter the office hours date in this format: YYYY/MM/DD H:M ')
        get_course3 = input('Enter the course: ')
        get_platform3 = input('Enter the online platform for the class: ')
        get_ta3 = input('Enter the teaching assistant name: ')
        my_tasks['office']['T' + str(task_no)] = OfficeHoursTasks(get_name3, get_due_date3, get_course3, get_platform3,
                                                                  get_ta3)
        print('Office hours task created successfully with id T' + str(task_no))
        print(task_no)
    elif get_type == 'extra':
        get_name4 = input('Enter task name: ')
        get_due_date4 = input('Enter the date of the activity in this format: YYYY/MM/DD H:M ')
        get_platform_venue4 = input('Enter the platform or venue for the task: ')
        my_tasks['extra']['T' + str(task_no)] = ExtraCurricularTasks(get_name4, get_due_date4, get_platform_venue4)
        print('Extra curricular task created successfully with id T' + str(task_no))
        print(task_no)
    elif get_type == 'off':
        get_name5 = input('Enter task name: ')
        get_due_date5 = input('Enter the due date in this format: YYYY/MM/DD H:M ')
        get_venue5 = input('Enter the venue for the task: ')
        my_tasks['off']['T' + str(task_no)] = OffCampusTasks(get_name5, get_due_date5, get_venue5)
        print('Off campus task created successfully with id T' + str(task_no))
        print(task_no)
    elif get_type == 'exit':
        break

    else:
        print('Invalid input')
        quit()
    print()

    # ask user if they want to create another task
    other = input('Add another task? Yes/No ').lower()
    print()
    if other == 'yes':
        print()
        task_no = task_no + 1  # increment the task ID for the next task
        continue
    elif other == 'no':
        break
    else:
        print('Invalid input')
        quit()

# The menu with the functions to be performed on the tasks
print("""Welcome to the action menu
You will prompted for task ID and then choose an action

Available options:

Edit tasks
Set reminder
Check time remaining
Mark as complete""")
n = 0
print()

# A while loop that runs as long as a user is acting on their task
while True:
    # Asking for and verifying the Task id
    task_id = input('Please enter task ID: ').upper()
    for k, v in my_tasks.items():
        if n == 1:
            break
        for k1, v1 in v.items():
            if task_id == k1:
                if my_tasks[k][k1].complete is True:
                    print('Sorry, task already marked as complete')
                    print()
                    n += 1
                    break
                else:
                    print('You selected task: ' + my_tasks[k][k1].task_name)
                    print()
                    break
            else:
                print("Invalid Task id")
                quit()

    if n == 1:
        break
    print()
    # Specific while loop for just selecting the actions
    while True:
        action = input('Please choose action:\nedit, mark, set, check \n:: ').lower()
        print()
        if action == 'edit':
            for k, v in my_tasks.items():
                for k1, v1 in v.items():
                    if task_id == k1:
                        my_tasks[k][k1].edit_task()
                        print()

        elif action == 'set':
            for k, v in my_tasks.items():
                for k1, v1 in v.items():
                    if task_id == k1:
                        my_tasks[k][k1].set_reminder()
                        print()

        elif action == 'mark':
            for k, v in my_tasks.items():
                for k1, v1 in v.items():
                    if task_id == k1:
                        my_tasks[k][k1].mark_complete()
                        print()

        elif action == 'check':
            for k, v in my_tasks.items():
                for k1, v1 in v.items():
                    if task_id == k1:
                        print(my_tasks[k][k1].check_time())
                        print()

        else:
            print('Invalid input!')
            quit()

        # Asking user if they want to perform another action
        other_action = input('Perform another action? Yes/No ').lower()
        if other_action == 'yes':
            print()
            continue
        else:
            print()
            break

    # Asking user if they want to select another task to edit
    other_task = input('Select another task?: Yes/No ').lower()
    if other_task == 'yes':
        print()
        continue
    else:
        print()
        break

print()

# scheduler for notifications for the tasks due date
for k, v in my_tasks.items():
    for k1, v1 in v.items():
        if my_tasks[k][k1].complete is True:
            print('There are no notifications for completed tasks')
            print()
        else:

            def notification():
                print(my_tasks[k][k1].task_name + ' due NOW! ')


            seconds_to = (my_tasks[k][k1].due_date - datetime.datetime.now()).total_seconds()
            notify = time.time() + seconds_to
            s = sched.scheduler(time.time)
            s.enterabs(notify, 1, notification)
            print('Waiting for notifications!...')
            s.run()