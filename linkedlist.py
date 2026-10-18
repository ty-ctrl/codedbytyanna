from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
    def add_client(self, client):
        new_node = Node(client)
        
        if self.head is None:
            self.head = new_node
            return
        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

        print_clients(self):
        if self.head is None:
            print("There are no clients.")
            return 
        current = self.head

        while current is not None:
            print(current.data)
            current = current.next

    def find_client(self, name):
        current = self.head

        while current is not None:
            if current.data.name.lower() == name.lower()
            return current.data
            current = current.next
        return None

    def delete_client (self, name):
        if self.head is None:
            return False
        if self.head.data.name.lower() == name.lower():
            self.head = self.head.next
            return True
        current = self.head
        while current.next is not None:
            if current.next.data.name.lower() == name.lower()
            current.next = current.next.next
            return True

            current = current.next
        return False


