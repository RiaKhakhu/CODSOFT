import tkinter as tk
from tkinter import ttk
"""
 A to-do list helps a user effectively organize tasks
 Author: Khakhu Ria
 Version: 19/09/2024
"""


class ScrollableFrame(ttk.Frame):
    """A custom frame that includes a scrollbar for its content."""

    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)

        # Bind the frame's size to the canvas's scroll region
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")


class TaskFrame:
    """Represents a single task in the to-do list."""

    def __init__(self, root, task):
        self.frame = ttk.Frame(root)
        self.task = task
        self.create_widgets()

    def create_widgets(self):
        """Create and set up the widgets for this task."""
        self.taskText = tk.Text(self.frame, height=2, width=40, font=("Arial", 12),
                                bg="#f5f5f5", fg="#333333", relief=tk.FLAT, padx=10, pady=5)
        self.taskText.insert(tk.END, self.task)
        self.taskText.config(state=tk.DISABLED)

        self.editButton = ttk.Button(self.frame, text="✎ EDIT", command=self.toggle_edit, style="Task.TButton")
        self.completeButton = ttk.Button(self.frame, text="✔", command=self.complete_task, style="Task.TButton")
        self.deleteButton = ttk.Button(self.frame, text="✖", command=self.delete_task, style="Task.TButton")

        self.taskText.pack(side=tk.LEFT, padx=10, pady=5)
        for button in (self.editButton, self.completeButton, self.deleteButton):
            button.pack(side=tk.LEFT, padx=5, pady=5)

        self.editing = False

    def toggle_edit(self):
        """Toggle between edit and read-only modes for the task text."""
        self.editing = not self.editing
        new_state = tk.NORMAL if self.editing else tk.DISABLED
        new_text = "SAVE" if self.editing else "✎ EDIT"
        self.taskText.config(state=new_state)
        self.editButton.config(text=new_text)
        if self.editing:
            self.taskText.focus_set()

    def complete_task(self):
        """Mark the task as complete by applying a strikethrough effect."""
        self.taskText.config(state=tk.NORMAL)
        self.taskText.tag_add("strike", "1.0", tk.END)
        self.taskText.tag_configure("strike", overstrike=True)
        self.taskText.config(state=tk.DISABLED)
        for button in (self.completeButton, self.editButton):
            button.config(state=tk.DISABLED)

    def delete_task(self):
        """Remove this task from the list."""
        self.frame.destroy()


class ToDoList:
    """Main application class for the To-Do List."""

    def __init__(self):
        self.root_window = tk.Tk()
        self.root_window.title("To-Do List")
        self.root_window.geometry("800x450")
        self.create_widgets()

    def create_widgets(self):
        """Create and set up the main widgets for the application."""
        self.addTaskText = tk.Text(self.root_window, height=3, width=50, font=("Arial", 12), bg="#e0e0e0", fg="#555",
                                   relief=tk.SUNKEN, padx=10, pady=5)
        self.addTaskText.insert(tk.END, "Add task")
        self.addTaskText.bind("<FocusIn>", self.clear_default_text)
        self.addTaskText.bind("<KeyRelease>", self.add_task)
        self.addTaskText.pack(padx=10, pady=10)

        self.scrollable_frame = ScrollableFrame(self.root_window)
        self.scrollable_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.tasksFrame = self.scrollable_frame.scrollable_frame

        style = ttk.Style()
        style.configure("Task.TButton", font=("Arial", 10, "bold"), padding=6)

    def clear_default_text(self, event):
        """Clear the default 'Add task' text when the input box is focused."""
        if self.addTaskText.get("1.0", tk.END).strip() == "Add task":
            self.addTaskText.delete("1.0", tk.END)

    def add_task(self, event):
        """Add a new task when the user presses Enter in the input box."""
        if event.keysym == "Return" and not event.state & 0x1:
            task = self.addTaskText.get("1.0", "end-1c").strip()
            if task and task != "Add task":
                TaskFrame(self.tasksFrame, task).frame.pack(fill=tk.X, padx=5, pady=5)
                self.addTaskText.delete("1.0", tk.END)
                self.addTaskText.insert(tk.END, "Add task")
            return "break"

    def run(self):
        """Start the main event loop of the application."""
        self.root_window.mainloop()


if __name__ == "__main__":
    ToDoList().run()
