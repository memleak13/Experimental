#!/usr/bin/python3
''' Right now only option 1 and 2 are supported '''

import sys
import os
import datetime
from taskpad import Tasklist, Task

class Menu:
    '''Display a menu and respond to choices when run.'''
    def __init__(self):
        self.tasklist = Tasklist()
        self.choices = {
                "1": self.show_tasks,
                "2": self.add_task,
                "3": self.search_tasks,
                "4": self.complete_task,
                "5": self.del_task,
                "6": self.quit
                }
    def run(self):
        '''Display the menu and respond to choices.'''
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def display_menu(self):
        #os.system('clear')
        print("""
            Tasklist Menu

            1. Show all Tasks
            2. Add Task
            3. Search Task
            4. Complete a Task
            5. Delete a Task
            6. Quit
            """)
    def show_tasks(self, tasks = None):
        for task in self.tasklist.tasklist:
            print ("{0} : {1}, {2}\n{3}\n".format(task.id, task.duedate,
                task.complete, task.task))
    
    def add_task(self):
        task = input("Enter a task: ")
        #TODO: Enter proper due date mechanism, this is just for testing
        self.tasklist.new_task(task, datetime.date.today())   
    
    def del_task():
        pass         
    def search_tasks(self):
        pass
    def complete_task(self):
        pass
    def quit(self):
        sys.exit(0)

if __name__ == "__main__":
    Menu().run()