import io
import sys

from taskManager import task_manager
from taskManager import parse_user_input
from taskManager import command_switch
from taskManager import TaskManager

#https://stackoverflow.com/questions/33767627/python-write-unittest-for-console-print
#for testing purposes concerning the print in display tasks function

# def test_task_manager(monkeypatch):
#     monkeypatch.setattr('builtins.input', lambda _: "+ dormir")
#     assert task_manager() == 'add'

def test_parse_user_input():
    assert parse_user_input('+ dormir') == ['+','dormir']
    assert parse_user_input('- 5') == ['-','5']
    assert parse_user_input('x 2') == ['x','2']
    assert parse_user_input('o 2') == ['o','2']
    assert parse_user_input('q') == ['q','']

def test_command_switch_add():
    input = ['+','vincent']
    taskManager = TaskManager()
    command_switch(input,taskManager)
    assert taskManager.tasks == {1: {'description':'vincent','status':' '}}
    assert taskManager.idCounter == 1

def test_command_switch_remove():
    input = ['+','vincent']
    taskManager = TaskManager()
    command_switch(input,taskManager)
    input = ['-',1]
    command_switch(input,taskManager)
    assert taskManager.tasks == {}

def test_command_switch_update():
    input = ['+','vincent']
    taskManager = TaskManager()
    command_switch(input,taskManager)
    input = ['x',1]
    command_switch(input,taskManager)
    assert taskManager.tasks == {1: {'description':'vincent','status':'x'}}

def test_display_tasks():
    input = ['+','vincent']
    taskManager = TaskManager()
    command_switch(input,taskManager)
    capturedOutput = io.StringIO()          # Create StringIO object
    sys.stdout = capturedOutput                   #  and redirect stdout.
    taskManager.displayTasks()                                   # Call unchanged function.
    sys.stdout = sys.__stdout__                   # Reset redirect.
    assert capturedOutput.getvalue()  == '1  [   ]  vincent\n'