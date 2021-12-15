from typing import List

class TaskManager:
    tasks = {}
    idCounter = 0
    
    def incrementID(self):
        self.idCounter = self.idCounter +1

    def addTask(self, userInput):
        self.incrementID()
        self.tasks[self.idCounter] = {'description': userInput[1], 'status': ' '}
    
    def removeTask(self, userInput):
        self.tasks.pop(int(userInput[1]))
    
    def updateTaskStatus(self, userInput):
        self.tasks[int(userInput[1])].update({'status':userInput[0]})

    def displayTasks(self):
        for x, y in self.tasks.items():
            print('Tasks:\n',x, ' [',y['status'],'] ',y['description'])

def task_manager_main():
    taskManager = TaskManager()
    loop = True
    while(loop):
        user_input = input("Enter a command:\n. Add task: + <description>\n. Delete task: - <id>\n. Task done: x <id>\n. Task to do: o <id>\n. Escape loop: q\n")
        command = parse_user_input(user_input)
        loop = command_switch(command,taskManager)
        taskManager.displayTasks()

def parse_user_input(input: str)-> List[str]:
    return [input[0], input[2:]]

def command_switch(input: List[str], taskManager: TaskManager):
    if(input[0] == '+'):
        taskManager.addTask(input)
    elif(input[0] == '-'):
        taskManager.removeTask(input)
    elif(input[0] == 'x'):
        taskManager.updateTaskStatus(input)
    elif(input[0] == 'o'):
        taskManager.updateTaskStatus(input)
    elif(input[0] == 'q'):
        return False
    return True

task_manager_main()