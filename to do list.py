import tkinter as tk
from tkinter import messagebox

def adtask():
    task_description = task_input.get()
    if task_description:
        task_list.insert(tk.END, task_description)
        task_input.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task description cannot be empty.")

def matask():
    selected_task_index = task_list.curselection()
    if selected_task_index:
        index = selected_task_index[0]
        task_list.itemconfig(index, {"bg": "light green"})
        task_list.selection_clear(0, tk.END)

def uptask():
    selected_task_index = task_list.curselection()
    if selected_task_index:
        index = selected_task_index[0]
        new_description = task_input.get()
        if new_description:
            task_list.delete(index)
            task_list.insert(index, new_description)
            task_input.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task description cannot be empty.")

def retask():
    selected_task_index = task_list.curselection()
    if selected_task_index:
        task_list.delete(selected_task_index[0])


root = tk.Tk()
root.title("To-Do List ")
root.geometry("400x400")
heading_label = tk.Label(root, text="To-Do List", font=("Calibri", 30, "bold"),bg="green",fg="yellow")
heading_label.pack(pady=20)
task_input = tk.Entry(root, width=50)
task_input.pack()

add_button = tk.Button(root, text="ADD",font="calibri",width=5,bg="blue",fg="white",command=adtask)
add_button.pack()

task_list = tk.Listbox(root, selectmode=tk.SINGLE, height=10, width=50)
task_list.pack(fill='x')
buttons = tk.Frame(root)
buttons.pack(pady = 5)
complete = tk.Button(root, text="Completed",bg="green",fg="white",command=matask)
update = tk.Button(root, text="Update ", command=uptask,bg="yellow")
remove = tk.Button(root, text="Remove ",bg="red",fg="white",command=retask)
complete.pack(side="left",expand=1,anchor='s')
update.pack(side="left",expand=1,anchor='s')
remove.pack(side="left",expand=1,anchor='s')
root.mainloop()

