from client import Client 
from linkedlist import LinkedList

clients = LinkedList()

while True:
    print("\nBoudreaux's Barbershop")
    print("1. Add Client")
    print("2. List Clients")
    print("3. Find Client")
    print("4. Delete Client")
    print("5. Quit.")

    choice = input("Choose an option:")

    if choice == "1":
        name = input("Enter client name:")
        phone = input("Enter phone number:")
        date_of_birth = input("Enter a date of birth:")

        client = Client(name, phone, date_of_birth)
        clients.add_client(client)

        print("Client added successfully!")

    elif choice == "2":
        print("\nClient List:")
        clients.print_clients()
    elif choice == "3":
        name_input = input("Enter the name of the client to find:")
        client = clients.find_client(name)
        
        if client is not None:
            print("Client found:")
            print(client)
        else:
            print("Client not found.")
    elif choice == "4":
        name = input("Enter the name of the client to delete:")

        if clients.delete_client(name):
            print("Client not found.")

    elif choice == "5":
        print("Goodbye!")
        break 
    else:
        print("Invalid option. Please choose a valid menu option.")
