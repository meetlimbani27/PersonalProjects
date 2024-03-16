tasks = []
menu_option= 0

def retrive_task():
    with open('tasks.txt', 'r') as f:
            tasks = f.read().split(',')
            print("retrivel successful")
            print(tasks)
            return tasks

def add_task():
    task = input("What is your task?(This will override current list) ")
    if task == "-1":
        return
    tasks.insert(0,task)
    print("task added successfully\n")

def delete_task():
    print(tasks)
    x = input("which tasks you want to delete: ")
    if x == "-1":
        return
    tasks.remove(tasks[int(x)-1])
    print("task removal successfull\n")

def list_tasks():
    print(tasks,"\n")

def mark_complete():
    print(tasks)
    x = input("which task you want to mark complete: ")
    if x == "-1":
        return
    tasks.append("COMPLETED:" + tasks[int(x)-1])
    tasks.remove(tasks[int(x)-1])
    print("task marked as complete\n")

def get_user_input():
    print("1. retrieve previous tasks list \n2. add a new task \n3. delete a task \n4. list all tasks \n5. mark task as complete \n6. quit \n7. enter -1 at any stage to reach main menu")
    return int(input("What do you want to do? "))




while menu_option != 6:
    
    menu_option = get_user_input()

    if menu_option == "-1":
        continue
    elif menu_option == 1:
        tasks = retrive_task()
    elif menu_option == 2 :
        add_task()
    elif menu_option == 3:
        delete_task()
    elif menu_option == 4:
        list_tasks()
    elif menu_option == 5:
        mark_complete()
    elif menu_option == 6:
        break
    else:
        print("invalid input\n")
print("\nThank you for using our program!")


with open('tasks.txt', 'w') as f:
    f.write(','.join(tasks))


