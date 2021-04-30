from tkinter import *
from tkinter import messagebox


def add_task(event):
    global list_index
    if task.get() == "":
        messagebox.showwarning("Input Warning", "Please enter a task!")
    else:
        task_list.insert(list_index, task.get())
        task.set("")
        list_index += 1


def delete_task(event):
    items = select_task(event)
    # print(items)
    if len(items) == 0:
        messagebox.showwarning("Select Item", "Select items to delete")
    for index in items[::-1]:
        task_list.delete(index)


def select_task(event):
    selected_items = task_list.curselection()
    return selected_items


root = Tk()
root.geometry("500x500+800+100")    # width x height + x(from left) + y(from top)
root.configure(bg="plum")

list_index = 0
task_list = Listbox(root, bg="black", fg="white", width=60, selectmode=MULTIPLE, selectbackground="red")
task_list.bind("<<ListboxSelect>>", select_task)
task_list.grid(padx=70, pady=10)

task = StringVar()
task_entry = Entry(root, textvariable=task, width=40, bg="lightgreen", fg="maroon", bd=4, font=("arial 12 bold"))
task_entry.focus()
task_entry.grid()

add_btn = Button(text="Add Task", bg="blue", fg="white", width=15, font=("arial 10 bold"))
add_btn.bind("<Button-1>", add_task)
task_entry.bind("<Return>", add_task)
add_btn.grid(pady=15)

delete_btn = Button(text="Delete Task", bg="red", fg="white", width=15, font=("arial 10 bold"))
delete_btn.bind("<Button-1>", delete_task)
delete_btn.grid()

root.mainloop()
