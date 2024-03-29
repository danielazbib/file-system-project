class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None
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
class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.next = None
class Directory:
    def __init__(self, name):
        self.name = name
        self.files = LinkedList()
        self.subdirectories = []
        self.file_queue = Queue()  # Initialize file_queue for each directory

    #method to create a file
    def create_file(self, name, size):
         # add files to linkedList File 
        self.files.append(name, size)  
    #method to display contents
    def display_contents(self, indent=""):
        print(f"{indent}Contents of {self.name}:")
        self.files.display(indent + "  ")  # Display files in the current directory

        for subdir in self.subdirectories:
            subdir.display_contents(indent + "  ")  # Recursively display contents of subdirectories

    #method for creating subdirectories
    def create_subdirectory(self, name):
        subdirectory = Directory(name)
        self.subdirectories.append(subdirectory)

    def delete_file(self, name):
        file_to_delete = None
        current = self.files.head
        while current:
            if current.name == name:
                file_to_delete = current
                break
            current = current.next

        if file_to_delete:
            self.files.remove(file_to_delete)
            print(f"File '{name}' deleted successfully.")
        else:
            print(f"File '{name}' not found.")

    #method for moving files between directories        
    def move_file(self, file_name, destination_directory_name):
        file_to_move = None
        current = self.files.head
        while current:
            if current.name == file_name:
                file_to_move = current
                break
            current = current.next

        if file_to_move:
            destination_directory = None
            for subdir in self.subdirectories:
                if subdir.name == destination_directory_name:
                    destination_directory = subdir
                    break

            if destination_directory:
                destination_directory.files.append(file_to_move.name, file_to_move.size)
                self.files.remove(file_to_move)  #removes the file from the current directory
                print(f"File '{file_name}' moved to '{destination_directory_name}' successfully.")
            else:
                print(f"Destination directory '{destination_directory_name}' not found.")
        else:
            print(f"File '{file_name}' not found.")   

    def execute_file_moves(self):
        while not self.file_queue.is_empty():
            file_to_move, destination_directory = self.file_queue.dequeue()
            destination_directory.files.append(file_to_move.name, file_to_move.size)
            self.files.remove(file_to_move)
            print(f"File '{file_to_move.name}' moved to '{destination_directory.name}' successfully.")
                                 

def main():
    #allow user to establish their own root_directory
    root_directory_name = input("Enter the name of the root directory: ")
    root_directory = Directory(root_directory_name)

    while True:
        print("\nAvailable commands:")
        print("1. create_file <name> <size>")
        print("2. create_subdirectory <name>")
        print("3. move_file <file_name> <destination_directory>") # move file operation using queue data structure
        print("4. display_contents")
        print("5. delete_file <name>")
        print("6. exit")
        #add undoing file operation using stack data structure

        #splits user input to store every input as a string in the 'command' array
        command = input("Enter a command: ").strip().split()

        #compares the position of word in command to specific file
        if command[0] == "create_file" and len(command) == 3: #also makes sure that the user input has three words because the create_file method takes 2 inputs
            for element in command:
                print(element)
            root_directory.create_file(command[1], command[2]) #passes arguments to method by accesing the command array's position
        elif command[0] == "create_subdirectory" and len(command) == 2:
            root_directory.create_subdirectory(command[1])
        elif command[0] == "move_file" and len(command) == 3:
            root_directory.move_file(command[1], command[2])
        elif command[0] == "display_contents":
            root_directory.display_contents()
        elif command[0] == "delete_file" and len(command) == 2:
            root_directory.delete_file(command[1])
        elif command[0] == "exit":
            print("Exiting...")
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()