import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Manager")
        self.root.geometry("400x400")

        # Task entry
        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.pack(pady=10)

        # Buttons
        tk.Button(root, text="Add Task", command=self.add_task).pack(pady=5)
        tk.Button(root, text="Mark as Done", command=self.mark_done).pack(pady=5)
        tk.Button(root, text="Delete Task", command=self.delete_task).pack(pady=5)

        # Task list
        self.task_listbox = tk.Listbox(root, width=40, height=10, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        # Load saved tasks
        self.load_tasks()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
            self.save_tasks()
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def mark_done(self):
        try:
            index = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(index)
            self.task_listbox.delete(index)
            self.task_listbox.insert(tk.END, f"✔ {task}")
            self.save_tasks()
        except:
            messagebox.showwarning("Warning", "Please select a task to mark done")

    def delete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(index)
            self.save_tasks()
        except:
            messagebox.showwarning("Warning", "Please select a task to delete")

    def save_tasks(self):
        tasks = self.task_listbox.get(0, tk.END)
        with open("tasks.txt", "w") as f:
            for task in tasks:
                f.write(task + "\n")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as f:
                for task in f.readlines():
                    self.task_listbox.insert(tk.END, task.strip())
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
