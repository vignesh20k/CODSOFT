todo_list=[]
def menu():
    while (True):
        print("===== Main Menu =====")
        print("1. Add a New Task")
        print("2. View All Task")
        print("3. Remove the Task")
        print("4. Mark a Task as completed")
        print("5. Exit")

        choice = input("enter the your choice")

        def add_task():
            task=input("enter the your task")
            todo_list.append({"task" : task,"status":"pending"})

            print(" this task add to successfully\n")

        def view_task():
            print(" your todo list;")
            if len(todo_list)==0:
                print("No pending tasks!")
            else:
                for index,task in enumerate(todo_list,1):
                    print(f"{index}:{task['task']}-{task['status']}")
        print("\n")
        def remove_task():
            if len(todo_list) ==0:
                print("list is Empty!")

            else:
                try:
                    search_index =int(input("Enter the task number that your want to reomve:")) -1
                    if 0<= search_index < len(todo_list):
                        removed_task = todo_list.pop(search_index)
                        print(f"task removed: {removed_task}")
                    else:
                        print("Invalid tas number.")
                except ValueError:
                    print("Please Enter a Valid Task Number.")

        def mark_done():
            if len(todo_list) ==0:
                print("list is Empty!")

            else:
                try:
                    search_index =int(input("Enter the task number that you want to mark as complete: ")) -1
                    if 0<= search_index < len(todo_list):
                        todo_list [search_index] ['status'] = 'done'
                        print(f"task {todo_list[search_index]['task']} has been marked as Done.")
                    else:
                        print("Invalid tas number.")
                except ValueError:
                    print("Please Enter a Valid Task Number.")


        if choice == "1":
            add_task()
        elif choice =="2":
            view_task()
        elif choice =="3":
            remove_task()
        elif choice =="4":
            mark_done()

        elif choice =="5":
            print("Exiting the Appplication...")
            exit()
        else:
            print("invalid choice Try again!!!")


menu()
