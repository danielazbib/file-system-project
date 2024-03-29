from file_module import File
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, name, size):
        new_file = File(name, size)
        if not self.head:
            self.head = new_file
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_file
    # function to remove node by name                                       
    def remove(self, file_to_remove):
        current = self.head
        prev = None
        while current:
            if current == file_to_remove:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                del current
                return
            prev = current
            current = current.next
    def display(self, indent=""):
        current = self.head
        while current:
            print(f"{indent}File: {current.name}, Size: {current.size}")
            current = current.next     
                     