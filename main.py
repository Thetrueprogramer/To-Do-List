print("Welcome to your to-do list")
todo = []
while True:
    print("Choose what you want to do")
    print("1. Add, 2. Remove, 3. View list, 4 Export, 5. Import")
    action = int(input())
    if action == 1:
        print("What do you want to add")
        todo.append(input())
    if action == 2:
        print("Type the id of the item you want to delete")
        todo
        del todo[int(input())]
    if action == 3:
        print("Here is your list")
        print(todo)
    if action == 4:
        with open("todo.txt", "w", encoding="utf-8") as file:
            file.write(str(todo))
    if action == 5:
        with open("todo.txt", "r", encoding="utf-8") as file:
            Import = file.readline()
            todo = Import.strip().split(',')