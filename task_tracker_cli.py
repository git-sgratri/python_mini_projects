import json
import sys
from datetime import datetime as dt

def all_args():
    print("Add a task: add \"<description>\"")
    print("Update a task: update <ID> \"<description>\"")
    print("Delete a task: delete <ID>")
    print("Mark task as in-progress: mark-in-progress <ID>")
    print("Mark task as done: mark-done <ID>")
    print("List tasks: list")
    print("List tasks in-progress: list-in-progress")
    print("List tasks done: list-done")

def load_tasks():
    try:
        with open("tasks.json",'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
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
        if(task["status"]=="in-progress"):
            idx+=1
            print(f"ID:{task["id"]} -> {task["description"]}, created at: {task["created_at"]}")
    if idx==0:
        print("There are no in progress tasks.")

def dump_helper(tasks):
    with open("tasks.json",'w') as file:
        json.dump(tasks,file,indent=4)

def add_task(tasks,description):
    if tasks==[]:
        id="1"
    else:
        id = str(max(int(task["id"]) for task in tasks)+1)
    tasks.append({"id": id,"description": description,"status":"todo","created_at": str(dt.now()),"updated_at":str(dt.now())})
    dump_helper(tasks)
    print(f"Task added successfully (ID:{id})")

def main():
    tasks = load_tasks()
    n = len(sys.argv)
    if n < 2:
        print("No arguements passed")
    if n > 1:
        operation = sys.argv[1]
        match operation:
            case "add":     # add a task to json file
                if n==3:
                    add_task(tasks,str(sys.argv[2]))
                else:
                    print("Error: Expected task description <str>")
                    print("Try:\n\tadd \"<description>\"")

            case "update":  #update a task description
                if n>2:
                    x = True
                    for task in tasks:
                        if task["id"] == sys.argv[2]:
                            x = False
                            if n==4:
                                task["description"] = sys.argv[3]
                                task["updated_at"] = str(dt.now())
                                dump_helper(tasks)
                            else:
                                print("Error: Expected new description <str> for update")
                                print("Try:\n\tupdate <ID> \"<description>\"")
                            break
                    if x:
                        print("Error: No such task ID is present")
                else:
                    print("Error: Invalid arguements, expected task ID and description for update")
                    print("Try:\n\tupdate <ID> \"<description>\"")

            case "delete":  #delete a task completely
                if n==3:
                    x = True
                    for task in tasks:
                        if task["id"] == sys.argv[2]:
                            x = False
                            tasks.remove(task)
                            dump_helper(tasks)
                    if x:
                        print("Error: No such task ID exists")
                else:
                    print("Error: Invalide arguements, expected task ID to delete")
                    print("Try:\n\tdelete <ID>")

            case "mark-in-progress":    # Change task status to in-progress
                if n==3:
                    x = True
                    for task in tasks:
                        if task["id"] == sys.argv[2]:
                            x = False
                            task["status"] = "in-progress"
                            dump_helper(tasks)
                    if x:
                        print("Error: No such task ID exists")
                        print("Try:\n\tmark-in-progress <ID>")
                else:
                    print("Error: Invalide arguements, expected task ID for updating status")
                    print("Try:\n\tmark-in-progress <ID>")

            case "mark-done":   # change task status to done
                if n==3:
                    x = True
                    for task in tasks:
                        if task["id"] == sys.argv[2]:
                            x = False
                            task["status"] = "done"
                            dump_helper(tasks)
                    if x:
                        print("Error: No such task ID exists")
                        print("Try:\n\tmark-done <ID>")
                else:
                    print("Error: Invalide arguements, expected task ID for updating status")
                    print("Try:\n\tmark-done <ID>")

            case "list":    # list all tasks
                if n==2:
                    list_all(tasks)
                else:
                    print("Error: Invalid no. arguements")
                    print("Try:\n\tlist")

            case "list-todo":   # list all todo tasks
                if n==2:
                    list_todo(tasks)
                else:
                    print("Error: Invalid no. of arguements")
                    print("Try:\n\tlist-todo")

            case "list-in-progress":    # list all tasks in-progress
                if n==2:
                    list_in_progress(tasks)
                else:
                    print("Error:Invalid no. of arguements")
                    print("Try:\n\tlist-in-progress")

            case "list-done":   # list all tasks done
                if n==2:
                    list_done(tasks)
                else:
                    print("Error: Invalid no. of arguements")
                    print("Try:\n\tlist-done")
                    
            case _:
                print("Error: Invalid arguements")
                all_args()

if __name__ == "__main__":
    main()