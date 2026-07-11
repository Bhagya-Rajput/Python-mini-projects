import json
while True:
    try:
     choice = int(input('''
        ===== TO-DO LIST =====
          1. Add Task
          2. View Tasks
          3. Remove Task
          4. task status
          5. Exit  '''))
     try:
      with open("Text.json","r") as file:
       Task = json.load(file)
      
     except( FileNotFoundError, json.JSONDecodeError):
       with open("Text.json","w") as file:
        Task = []
    
     match(choice):
       case 1 : ## for adding a task
         task = input("Enter the task you want to add: ")
         Task.append({
           "task" : task,
           "status" : False
         })
         print(f"task is added to file")

       case 2: ## for view of all task
         for i,task in enumerate(Task,start =1):
          if task.get("status") == False:
           print(f"{i}. [] {task.get('task')}")
          else:
           print(f"{i}. [x] {task.get('task')}")
       case 3 :## for removing a existing task
         for i,task in enumerate(Task,start =1):
          print(f"{i}.{task}")
         try:
           n =int(input("enter the number of above task to remove:"))
           if 1 <= n <= len(Task):
            Task.pop(n - 1)
           else:
            print("Invalid task number")
         except ValueError as e:
            print("you have enterd some wrong input",e)
       case 4 :# for task status
        while True :
          for i,task in enumerate(Task,start =1):
           if task.get("status") == False:
            print(f"{i}. [] {task.get('task')}")
           else:
            print(f"{i}. [x] {task.get('task')}")
          try:
            n =int(input("enter the number of above task to modify :"))
            edit = input("enter the status you want to do{complete/left}...").lower()
            if 1 <= n <= len(Task):
              task = Task[n-1]
              if edit == "complete":
               task["status"] = True
              elif edit == "left":
               task["status"] = False
              else : 
                print("you enteref something wrong")
            else:
              print("Invalid task number")
          except ValueError as e:
              print("you have enterd some wrong input",e)
          for i,task in enumerate(Task,start =1):
           if task.get("status"):
            print(f"{i}. [x] {task.get('task')}")
           else:
            print(f"{i}. [] {task.get('task')}")
          exit  = input("you want to exit or continue changing{exit =1/continue = 2}")
          if exit == "1":
            break
  
       case 5:# for exiting program
         print("YOU were exiting from program")
         break
       case _:
         print("Enter wrong Input Try again")
     with open("Text.json","w") as file:
          json.dump(Task,file,indent=4)
    except ValueError as e:
      print("you have enterd some wrong input",e)