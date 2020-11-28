# Authors: Catherine Muthoni and Liplan Lekipising

from sched import scheduler
from all_tasks import AllTasks
from assignment_tasks import AssignmentTasks
from class_sessions_tasks import ClassSessionsTasks
from office_hours_tasks import OfficeHoursTasks
from extra_curricular_tasks import ExtraCurricularTasks
from off_campus_tasks import OffCampusTasks
import datetime
import sched
import time


# Welcome message and instructions
print("""Hi, welcome to your to-do program. We care about your productivity.
This program enables you to:
- Add tasks while specifying the type
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
        # get ttributes
        get_name1 = input('Enter task name: ')
        get_due_date1 = input('Enter the due date in this format: YYYY/MM/DD H:M ')
        get_course1 = input('Enter the course: ')
        # add attributes to the object and create a dictionary element
        my_tasks['assignment']['T' + str(task_no)] = AssignmentTasks(get_name1, get_due_date1, get_course1)
        print('Assignment task created successfully with id T' + str(task_no))

    elif get_type == 'class':
        # get attributes
        get_name2 = input('Enter task name: ')
        get_due_date2 = input('Enter the date for the class in this format: YYYY/MM/DD H:M ')
        get_course2 = input('Enter the course: ')
        get_platform2 = input('Enter the online platform for the class: ')
        get_facilitator2 = input('Enter the facilitator name: ')
        # add attributes to the  object and create a dictionary element
        my_tasks['class']['T' + str(task_no)] = ClassSessionsTasks(get_name2, get_due_date2, get_course2, get_platform2,
                                                                   get_facilitator2)
        print('Class session task created successfully with id T' + str(task_no))
        
    elif get_type == 'office':
        # get attributes
        get_name3 = input('Enter task name: ')
        get_due_date3 = input('Enter the office hours date in this format: YYYY/MM/DD H:M ')
        get_course3 = input('Enter the course: ')
        get_platform3 = input('Enter the online platform for the class: ')
        get_ta3 = input('Enter the teaching assistant name: ')
        # add attributes to the  object and create a dictionary element
        my_tasks['office']['T' + str(task_no)] = OfficeHoursTasks(get_name3, get_due_date3, get_course3, get_platform3,
                                                                  get_ta3)
        print('Office hours task created successfully with id T' + str(task_no))
        
    elif get_type == 'extra':
        # get attributes
        get_name4 = input('Enter task name: ')
        get_due_date4 = input('Enter the date of the activity in this format: YYYY/MM/DD H:M ')
        get_platform_venue4 = input('Enter the platform or venue for the task: ')
        # add attributes to the  object and create a dictionary element
        my_tasks['extra']['T' + str(task_no)] = ExtraCurricularTasks(get_name4, get_due_date4, get_platform_venue4)
        print('Extra curricular task created successfully with id T' + str(task_no))
        
    elif get_type == 'off':
        # get attributes
        get_name5 = input('Enter task name: ')
        get_due_date5 = input('Enter the due date in this format: YYYY/MM/DD H:M ')
        get_venue5 = input('Enter the venue for the task: ')
        # add attributes to the  object and create a dictionary element
        my_tasks['off']['T' + str(task_no)] = OffCampusTasks(get_name5, get_due_date5, get_venue5)
        print('Off campus task created successfully with id T' + str(task_no))
        
    elif get_type == 'exit':
        break

    else:
        print('Invalid input')
        print()
        continue
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
        print()
        break

# The action menu with the functions to be performed on the tasks
print("""Welcome to the action menu
You will prompted for task ID and then choose an action

Available options:

Edit tasks
Set reminder
Check time remaining
Mark as complete""")
check = 0  # assist in validating Task ID
n = 0  # assist in breaking out of loops if invalid Task is entered
print()

# A while loop that runs as long as a user wants to enter a task
while True:
    # Asking for and verifying the Task id
    task_id = input('Please enter task ID: ').upper()
    for k, v in my_tasks.items():
        if task_id not in v:  # check if task ID is not available
            check += 1

        elif task_id in v:  # check if task ID is available
            check = 0

        if check == 5:  # check if Task ID was not found in all 5 types and break out
            print('Invalid Task ID!')
            check = 0
            n += 1
            break

        for k1, v1 in v.items():  # check if the found task is already marked as complete
            if task_id == k1:
                if my_tasks[k][k1].complete is True:
                    print('Sorry, task already marked as complete')
                    print()
                    n += 1
                    break

                else:  # inform user the task they selected
                    print('You selected task: ' + my_tasks[k][k1].task_name)
                    print()
                    break

    if n == 1:  #start loop if invalid task was encounted
        n = 0
        continue

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
            print()
            continue

        # Asking user if they want to perform another action on the task
        other_action = input('Perform another action? Yes/No ').lower()
        if other_action == 'yes':
            for k, v in my_tasks.items():
                for k1, v1 in v.items():
                    if task_id == k1:
                        if my_tasks[k][k1].complete:  # check task has already been marked as complete
                            print('Task already marked as complete!')
                            print()
                            n += 1
                            break
                        elif my_tasks[k][k1].complete is False:
                            print()
                            continue
            if n == 1:  # break loop if task was marked as complete
                n = 0
                break

        else:
            print()
            break

    # Asking user if they want to select another task to edit
    other_task = input('Select another task?: Yes/No ').lower()
    if other_task == 'yes':
        check = 0
        print()
        continue
    else:
        print()
        break


notify_all = []  # list to hold all notifications

print()
# scheduler for notifications for the tasks due date
for k, v in my_tasks.items():
    for k1, v1 in v.items():
        if my_tasks[k][k1].complete is True:  # check if there was a task already marked as complete
            print('Task : ' + my_tasks[k][k1].task_name + ' is already marked as complete hence no notification')
            print()
        else:  # create notifications

            def notification():
                print(my_tasks[k][k1].task_name + ' due NOW! ')  #notification for due now
            
            def notification1():
                print(my_tasks[k][k1].task_name + ' reminder is NOW! ')  # notification for reminders
            
            if my_tasks[k][k1].reminder is not None:  # this sections runs if a reminder was set
                seconds_to_rem = (my_tasks[k][k1].reminder - datetime.datetime.now()).total_seconds()
                notify_rem = time.time() + seconds_to_rem
                s1 = sched.scheduler(time.time)
                s1.enterabs(notify_rem, 1, notification1)

                seconds_to = (my_tasks[k][k1].due_date - datetime.datetime.now()).total_seconds()
                notify = time.time() + seconds_to
                s = sched.scheduler(time.time)
                s.enterabs(notify, 2, notification)
                print()
                notify_all.append(s1)
                notify_all.append(s)
                print()
                
            else:  # sections runs if no reminder was set 
                seconds_to = (my_tasks[k][k1].due_date - datetime.datetime.now()).total_seconds()
                notify = time.time() + seconds_to
                s = sched.scheduler(time.time)
                s.enterabs(notify, 1, notification)
                print()
                notify_all.append(s)


print('Waiting for notifications!...')
print()

for n in notify_all:  # run notifcations
    n.run()
