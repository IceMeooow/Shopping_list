shopping_list = []
print( "     What would you like? If you need help, write 'help'. ")


def show_help():
    print(""" 
              Enter 'done' to stop adding
              Enter 'help' for this help
              Enter 'show' to see your list
              Enter 'delete' to delete one element from list
              """)

def show_list():
    print("Your list: ")
    for item in shopping_list:
        print(item)

def add_item():
    shopping_list.append(new_item)
    print("{} added. List has {} items".format(new_item,len(shopping_list)))

def del_item():
    print("Which item do you want to delete?")
    del_item = input(" * ")
    shopping_list.remove(del_item)
    print("{} deleted. List has {} items".format(del_item,len(shopping_list)))



while True:
    new_item = input ("- ")
    if new_item == "done":
        break 
    elif new_item == "help":
        show_help()
        continue
    
    elif new_item == "show":
        show_list()
        continue
    elif new_item == "delete":
        del_item()
        continue      
    
    add_item()

show_list()
