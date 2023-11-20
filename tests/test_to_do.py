from lib.todo import Todo
import pytest #type: ignore

"""
Construct a todo instance and get the task and complete property
"""
def test_get_task_and_complete_properties():
    todo = Todo("Walk the dog")
    assert todo.task == "Walk the dog"
    assert todo.complete == False

"""
Construct a todo instance and when it is marked as complete, 
the complete property returns True
"""

def test_task_is_complete():
    todo = Todo("Walk the dog")
    todo.mark_complete()
    assert todo.complete == True

"""
Construct a todo instance and if the todo string is empty, return an error
"""

def test_empty_todo_string():
    with pytest.raises(Exception) as e:
        todo = Todo("")
    assert str(e.value) == "No todo text has been entered"
