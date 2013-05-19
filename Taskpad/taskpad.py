#!/usr/bin/python3

import datetime

task_id = 0

class Task:  
    '''Represents a Task in a Tasklist'''
    def __init__(self, task, duedate=''):
        self.task = task
        self.duedate = str(duedate)
        self.complete = False
        #Setting task id and incrementing global counter
        global task_id
        task_id += 1
        self.id = task_id

class Tasklist:
    '''Represents a collection of tasks'''
    
    def __init__(self):
        '''Initilizes list which will hold all tasks'''
        self.tasklist = []
        
    def new_task(self, task, duedate = ''):
        '''Creates a new Task which is appended to the tasklist'''
        self.tasklist.append(Task(task, duedate))
        
    def del_task(self, id):
        '''deletes a task according to its id'''
        del (self.tasklist[id-1])
        
    def search(self, filter):
        '''Match all task for a string or a date. If searched by date, the
        date object needs to be converted to a string first'''
        return [task for task in self.tasklist if 
            filter in task.task or filter in task.duedate] 
       