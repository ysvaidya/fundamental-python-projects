import json
import os
file_name = "content.json"

def file_check():
    try:
        with open(file_name, "r") as file:
            data = json.load(file)
            return data
    except (FileNotFoundError):
        data = {}
        with open (file_name, "w")as file:
            json.dump(data, file)
            return data


def add_content():
    data_check = file_check()
    name = input("\tName -:- ")
    number = input("\tNumber -:- ")
    email = input("\tE-mail -:- ")

    data_check[name] = {
        "Phone No" : number,
        "Address" : email
        }
    
    with open (file_name, "w") as file:
        json.dump(data_check, file)



def view_data_print():
    data_check = file_check()

    if os.stat(file_name).st_size != 0:
        for name, info in data_check.items():
            print(f"{name} -- {info['Phone No']} -- {info['Address']}")
    else:
        print("Sorry, Empty!")



def check_info():
    data_check = file_check()

    if os.stat(file_name).st_size != 0:

        name = input("\tName -:- ")
        if name in data_check:
            print(f"{name} -- {data_check[name]['Phone No']} -- {data_check[name]['Address']}")
        else:
            print("Name not found!")   
    else:
        print("Sorry, Empty file! No Updates!")
        


def contant_update():

    def inside_update():
        while True:
                print("Choose one...")
                print("1. Name.")
                print("2. Phone Number.")
                print("3. E-Mail Address.")
                choice = input("\tYour Choice -:- ")
                match choice:
                    case "1":
                        new_name = input("\tNew Name -:- ")
                        data_check[new_name] = data_check[name]
                        del data_check[name]

                    case "2":
                        new_Ph_no = int(input("\tNew Phone Number -:- "))
                        data_check[name]['Phone No'] = new_Ph_no

                    case "3":
                        new_address = input("\tNew Address -:- ")
                        data_check[name]['Address'] = new_address

                    case _:
                        print("exiting...")
                        break
                    
                with open (file_name, "w") as file:
                    json.dump(data_check, file)
                    print("\tData has been Updated...\n")

    data_check = file_check()
    name = input("\tName -:- ")

    if os.stat(file_name).st_size != 0:
        if name in data_check:
            print(f"{name} -- {data_check[name]['Phone No']} -- {data_check[name]['Address']}")
            inside_update()
        else:
            print("Name not found!")  
    else:
        print("Sorry, Empty file! No Updates!")


def contant_delete():
    data_check = file_check()

    print("Sorry, you are deleting whole name data...\n")
    delete_name = input("\tName for Delete -:- ")

    if os.stat(file_name).st_size != 0:
        if delete_name in data_check:
            del data_check[delete_name]
            with open(file_name, "w") as file:
                json.dump(data_check, file)
        else:
            print("Name not found!")  
    else:
        print("Sorry, Empty file! No Updates!")


def main():
    while True:
        print("""  
    Contact Book
              
    1. Add Contact.
    2. View all Contact.
    3. Search for Contact.
    4. Update a Contact.
    5. Delete a Contact.
    6. Exit""")
        choice = input(" Choose One -:- ")
        
        match choice:
            case '1':
                add_content()
            case "2":
                view_data_print()
            case "3":
                check_info()
            case "4":
                contant_update()
            case "5":
                contant_delete()
            case "6":
                print("Thank you for using me, exiting...")
                break
            case _:
                print("Sorry, invalide input..")
        
        



if __name__ == "__main__":
    main()