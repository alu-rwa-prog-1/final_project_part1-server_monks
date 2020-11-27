import datetime


class All_tasks:
    def __init__(self, task_name, due_date, complete=False, creation_date=datetime.datetime.now(), reminder=None):
        """Holds all the variables for classes

        Args:
            task_name (string): Holds the name of the task
            due_date (date): Holds the due date in this format YYYY/MM/DD H:M
            complete (bool, optional): Used for status of task, still due ot complete. Defaults to False(Not complete)
            creation_date ([date, optional): Holds the date the task was created.
            reminder (date, optional): Holds the date for the reminder. Defaults to None.
        """
        self.task_name = task_name
        self.due_date = due_date

        try:
            d_date = datetime.datetime.strptime(due_date, '%Y/%m/%d %H:%M')
            if isinstance(d_date, datetime.datetime):
                self.due_date = d_date
        except ValueError:
            print('Wrong due date format, correct is YYYY/MM/DD H:M')
            quit()

        self.complete = complete
        self.creation_date = creation_date
        self.reminder = reminder

    def edit_task(self):
        """This method is used to a task.
        Input (string): Task attribute such as task name
        Output: New attribute value
        """
        val = input('Would like to edit task name? Yes/No ').lower()
        if val == 'yes':
            new_name = input('Enter the new task name: ')
            self.task_name = new_name
            print('Task Name changed successfully')

        val2 = input('Would like to edit the due date? Yes/No ').lower()
        if val2 == 'yes':
            try:
                new_date = input('Enter the new due date: YYYY/MM/DD HH:MM ')
                self.due_date = datetime.datetime.strptime(new_date, '%Y/%m/%d %H:%M')
                print('Task due date updated successully')
            except ValueError:
                print('Invalid Input. Follow this format YYYY/MM/DD H:M')

    def mark_complete(self):
        """Mark Complete
        """
        self.complete = True
        print(f'Great! {self.task_name} Task marked as complete')

    def set_reminder(self):
        """This method is used to set the reminder for a task
        Input (date): date for the reminder YYYY/MM/DD H:M
        Output: A reminder to notify user
        """
        try:
            reminder_input = input('Please the enter the date and time for reminder: YYYY/MM/DD H:M ')
            rem_dt = datetime.datetime.strptime(reminder_input, '%Y/%m/%d %H:%M')
            if rem_dt > self.due_date:
                print('Sorry, reminder has to be set before due date ')
            else:
                if rem_dt < self.creation_date:
                    print('Sorry, reminder has to be after the creation date ')
                else:
                    self.reminder = rem_dt
                    print(f'Reminder set successfully for {self.task_name}')
        except ValueError:
            print('Invalid Input. Follow this format YYYY/MM/DD H:M')

    def check_time(self):
        """This method is used to check amount of time remaining in hours and minutes
        Output: time remaining for a particular task
        """
        time_remaining = self.due_date - datetime.datetime.now()
        days, seconds = time_remaining.days, time_remaining.seconds
        hours = (days * 24) + (seconds // 3600)
        minutes = (seconds % 3600) // 60
        print('Amount of time remaining for ' + self.task_name + ' is:')
        return str(hours) + ' hours ' + str(minutes) + ' minutes'
