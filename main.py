from todo import TodoList
from calculator import divide, average
from validators import is_valid_task_name

def main():
    todo = TodoList()
    todo.add_task({"name": "Buy groceries", "done": False})
    todo.add_task({"name": "Clean house", "done": False})

    print("First task:", todo.get_first_task())

    result = divide(10, 0)  # BUG: will crash, dividing by zero
    print("Division result:", result)

    print("Is valid name:", is_valid_task_name(""))

if __name__ == "__main__":
    main()
