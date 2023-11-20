from lib.todo_list import TodoList

"""
Initially there are no tasks in the to do list
"""

def test_todo_list_empty():
    todo_list = TodoList()
    assert todo_list.task_list == []

"""
Searching for incomplete tasks initially returns an empty list
"""

def test_incomplete_list_empty():
    todo_list = TodoList()
    assert todo_list.incomplete() == []

"""
Searching for complete tasks initially returns an empty list
"""

def test_complete_list_empty():
    todo_list = TodoList()
    assert todo_list.complete() == []
