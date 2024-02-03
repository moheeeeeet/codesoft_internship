import tkinter as tk
from tkinter import simpledialog, messagebox

tasks = []


def addTask():
    task = simpledialog.askstring("Add Task", "Please enter a task:")
    if task:
        tasks.append(task)
        tasks.sort()  # Sort tasks alphabetically
        update_task_list()
        messagebox.showinfo("Task Added", f"Task '{task}' added to the list.")


def listTasks():
    if not tasks:
        messagebox.showinfo("No Tasks", "There are no tasks currently.")
    else:
        task_list = "\n".join([f"{index + 1}. {task}" for index, task in enumerate(tasks)])
        messagebox.showinfo("Current Tasks", task_list)


def deleteTask():
    if not tasks:
        messagebox.showinfo("No Tasks", "There are no tasks to delete.")
        return

    listTasks()
    try:
        taskToDelete = simpledialog.askinteger("Delete Task", "Enter the # to delete:")
        if taskToDelete is not None and 0 < taskToDelete <= len(tasks):
            deleted_task = tasks.pop(taskToDelete - 1)
            update_task_list()
            messagebox.showinfo("Task Deleted", f"Task {taskToDelete}. '{deleted_task}' has been removed.")
        else:
            messagebox.showinfo("Task Not Found", f"Task #{taskToDelete} was not found.")
    except ValueError:
        messagebox.showinfo("Invalid Input", "Please enter a valid number.")


def update_task_list():
    task_list_var.set("\n".join([f"{index + 1}. {task}" for index, task in enumerate(tasks)]))


if __name__ == "__main__":
    app = tk.Tk()
    app.title("To-Do List App")
    app.geometry("300x500")  # Set window size

    task_list_var = tk.StringVar()

    frame = tk.Frame(app, bg="#B0E57C")  # Set background color
    frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    label = tk.Label(frame, textvariable=task_list_var, bg="#B0E57C", font=("wide line", 12))  # Set background color and font
    label.pack(fill=tk.BOTH, expand=True)

    button_add = tk.Button(app, text="Add Task", command=addTask, bg="#54A24B", fg="white")  # Set button colors
    button_add.pack(side=tk.LEFT, padx=5)

    button_delete = tk.Button(app, text="Delete Task", command=deleteTask, bg="#D04648", fg="white")
    button_delete.pack(side=tk.LEFT, padx=5)

    button_list = tk.Button(app, text="List Tasks", command=listTasks, bg="#007BFF", fg="white")
    button_list.pack(side=tk.LEFT, padx=5)

    button_quit = tk.Button(app, text="Quit", command=app.quit, bg="#6C757D", fg="white")
    button_quit.pack(side=tk.RIGHT, padx=5)

    app.mainloop()
