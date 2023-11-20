from lib.todo import Todo
from lib.todo_list import TodoList

"""
When we add two tasks, we get those tasks back in the task list
"""

def test_add_two_tasks():
    todo_list = TodoList()
    task1 = Todo("Walk the dog")
    task2 = Todo("Cleaning")
    todo_list.add(task1)
    todo_list.add(task2)
    assert todo_list.task_list == [task1 , task2 ]

"""
When we add two tasks and request the incomplete tasks,
both tasks are returned
"""

def test_add_tasks_incomplete_returned():
    todo_list = TodoList()
    task1 = Todo("Walk the dog")
    task2 = Todo("Cleaning")
    todo_list.add(task1)
    todo_list.add(task2)
    assert todo_list.incomplete() == [task1, task2]

"""
When we add two tasks and complete one of those tasks, 
the completed task is returned when calling for a list of completed tasks,
the remaining incomplete tasks is returned when calling for a list of incomplete tasks
"""

def test_add_tasks_and_complete_one():
    todo_list = TodoList()
    task1 = Todo("Walk the dog")
    task2 = Todo("Cleaning")
    todo_list.add(task1)
    todo_list.add(task2)
    task2.mark_complete()
    assert todo_list.incomplete() == [task1]
    assert todo_list.complete() == [task2]

"""
When we add three tasks, complete one and then give-up, all tasks are then completed
"""

def test_add_tasks_then_give_up():
    todo_list = TodoList()
    task1 = Todo("Walk the dog")
    task2 = Todo("Cleaning")
    task3 = Todo("Ironing")
    todo_list.add(task1)
    todo_list.add(task2)
    todo_list.add(task3)
    task1.mark_complete()
    todo_list.give_up()
    todo_list.incomplete() == []
    assert todo_list.complete() == [task1, task2, task3]
