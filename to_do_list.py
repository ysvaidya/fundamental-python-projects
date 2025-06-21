import json
file_name = "file.json"

def data_read():
    with open (file_name, "r") as file:
        data = json.load(file)
    return data

def file_check():
    global file_name
    try:
        with open (file_name, "r") as file:
            data = json.load(file)
            for data_line in data:
                for key, value in data_line.items():
                    print(f"{key} : {value}")
                print("-------")
    except (FileNotFoundError, json.JSONDecodeError):
        data = []


def new_task(status = "Incomplete"):
    global file_name

    choice = input("Is this a new data in empty database (Y/n): ")
    task = input("Please enter your today's work: ")

    if choice == "Y" or choice == "y":
        value = [{"task" : task, "status" : status}]
        with open(file_name, "w") as file:
            json.dump(value, file)
        
    else:
        with open (file_name, "r") as file:
            data = json.load(file)
            value = {"task" : task, "status" : status}
            data.append(value)

        with open(file_name, "w") as file:
            json.dump(data,file)


def updet_comp():
    global file_name
    func = data_read()
    for index, val in enumerate(func, start = 1):
        print(f"{index}. {val}")
    index = int(input("Number for which you want to complete: "))

    # with open (file_name, "r") as file:
    #     data = json.load(file)
    func[index-1]["status"] = "Complete"
    

    with open (file_name, "w") as file:
        json.dump(func, file)

def del_data_file():
    global file_name
    data = data_read()
    # with open(file_name, "r") as file:
    #     data = json.load(file)
    index = int(input("The number you want to delete: "))
    del data[index - 1]
    with open (file_name, "w") as file:
        json.dump(data, file)


def main():

    while True:
        print("""
Do you want to make your to_do list_
Be carefull you are not allow to put something that you can't do.
----------------------------------------------------------

1. Want to chect your list.
2. Want to add any new task.
3. Want to put 'complete' in your tasks.
4. Want to remove any task that are 'complete only'.
5. Exit
                """)
            
        value = str(input("So what is your option: "))

    
        match value:
            case "1":
                file_check()
            case "2":
                new_task()
            case "3":
                updet_comp()
            case "4":
                del_data_file()
            case "5":
                break
            case _:
                print("Sorry, NO!")
        

if __name__ == "__main__":
    main()