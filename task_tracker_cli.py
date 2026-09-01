import json
from datetime import datetime as dt

def load_tasks():
    try:
        with open("tasks.json",'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def list_tasks(tasks):
    print("Which tasks do u want to list: ")
    print("1. All tasks")
    print("2. Tasks todo(not started)")
    print("3. Tasks that are completed")
    print("4. Tasks in progress")
    choice = int(input("enter your choice: "))
    print("##########################################################")
    match choice:
        case 1:
            list_all(tasks)
        case 2:
            list_todo(tasks)
        case 3:
            list_done(tasks)
        case 4:
            list_in_progress(tasks)
        case _:
            print("invalid choice")
    print("##########################################################")
    
def list_all(tasks):
    if tasks == []:
        print("There are no tasks present right now.")
    for task in tasks:
        print(f"ID:{task["id"]} -> {task["description"]}: {task["status"]}  (created at: {task["created_at"]})")

def list_done(tasks):
    idx=0
    for task in tasks:
        if(task["status"]=="done"):
            idx+=1
            print(f"ID:{task["id"]} -> {task["description"]}, created at: {task["created_at"]}")
    if idx==0:
        print("There are no completed tasks.")

def list_todo(tasks):
    idx = 0
    for task in tasks:
        if(task["status"]=="todo"):
            idx+=1
            print(f"ID:{task["id"]} -> {task["description"]}, created at: {task["created_at"]}")
    if idx==0:
        print("There are no incomplete tasks.")

def list_in_progress(tasks):
    idx = 0
    for task in tasks:
        if(task["status"]=="in progress"):
            idx+=1
            print(f"ID:{task["id"]} -> {task["description"]}, created at: {task["created_at"]}")
    if idx==0:
        print("There are no in progress tasks.")

def dump_helper(tasks):
    with open("tasks.json",'w') as file:
        json.dump(tasks,file,indent=4)

def add_task(tasks):
    description = input("Task description: ")
    if tasks==[]:
        id=0
    else:
        id = max(task["id"] for task in tasks)+1
    tasks.append({"id": id,"description": description,"status":"todo","created_at": str(dt.now()),"updated_at":str(dt.now())})
    dump_helper(tasks)

def update_task(tasks):
    print("which task do u want to update?")
    list_all(tasks)
    idx = int(input("Enter task id: "))
    print("What do u want to update?")
    print("1. Task description")
    print("2. Task status")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            for i,task in enumerate(tasks):
                if task["id"]==idx:
                    des = input("Enter new description: ")
                    tasks[i]["description"] = des
                    tasks[i]["updated_at"] = str(dt.now())
                    dump_helper(tasks)
                    break
        case 2:
             for i,task in enumerate(tasks):
                if task["id"]==idx:
                    print("Which status you want to assign to this task: \n1. todo\n2. in progress\n3. done")
                    st = int(input("enter your choice: "))
                    if 0>st>3:
                        print("invalid choice!")
                        return
                    elif st==1:
                        tasks[i]["status"] = "todo"
                    elif st==2:
                        tasks[i]["status"] = "in progress"
                    else:
                        tasks[i]["status"] = "done"
                    tasks[i]["updated_at"] = str(dt.now())
                    dump_helper(tasks)
                    break
        case _:
            print("invalid choice!")           

def delete_task(tasks):
    list_all(tasks)
    print("Which task you want to delete?")
    idx = int(input("Enter task ID: "))
    for task in tasks:
        if task["id"]==idx:
            tasks.remove(task)
            dump_helper(tasks)
            return
    print("No such task exists!")

id = 1
def main():
    while True:
        print("\n********************************************************************")
        tasks = load_tasks()
        print("Welcome to my task manger! Select your choice")
        print("1. Add a task.")
        print("2. Update a task.")
        print("3. Delete a task.")
        print("4. List tasks.")
        print("5. exit")
        print("*********************************************************************\n")
        choice = int(input("enter your choice of operation: "))
        
        match choice:
            case 1:
                add_task(tasks)
            case 2:
                update_task(tasks)
            case 3:
                delete_task(tasks)
            case 4:
                list_tasks(tasks)
            case 5:
                break
            case _:
                print("invalid choice!")

if __name__ == "__main__":
    main()