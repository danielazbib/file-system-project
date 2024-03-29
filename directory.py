from linkedList import LinkedList
from queue_1 import Queue
from stack import Stack
class Directory:
    def __init__(self, name):
        self.name = name
        self.files = LinkedList()
        self.subdirectories = []
        self.file_queue = Queue()  #initialize file_queue for each directory
        self.undo_stack = Stack()  #initialize Stack for undoing file operations


    #method to create a file
    def create_file(self, name, size):
         # add files to linkedList File 
        self.files.append(name, size)
        self.undo_stack.push(("create_file", name))  
    #method to display contents
    def display_contents(self, indent=""):
        print(f"{indent}Contents of {self.name}:")
        self.files.display(indent + "  ")  #display files in the current directory

        for subdir in self.subdirectories:
            subdir.display_contents(indent + "  ")  #recursively display contents of subdirectories

    #method for creating subdirectories
    def create_subdirectory(self, name):
        subdirectory = Directory(name)
        self.subdirectories.append(subdirectory)
        self.undo_stack.push(("create_subdirectory", name))

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
            self.undo_stack.push(("delete_file", name))
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
                self.undo_stack.push(("move_file", file_name, destination_directory_name))
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
        
    def undo_last_operation(self):
        if not self.undo_stack.is_empty():
            last_operation = self.undo_stack.pop()
            operation_type = last_operation[0]
            if operation_type == "create_file":
                _, file_name = last_operation
                self.delete_file(file_name)
            elif operation_type == "create_subdirectory":
                _, subdir_name = last_operation
                for subdir in self.subdirectories:
                    if subdir.name == subdir_name:
                        self.subdirectories.remove(subdir)
                        break
            elif operation_type == "move_file":
                _, file_name, destination_directory_name = last_operation
                destination_directory = None
                for subdir in self.subdirectories:
                    if subdir.name == destination_directory_name:
                        destination_directory = subdir
                        break
                if destination_directory:
                    for file in destination_directory.files:
                        if file.name == file_name:
                            destination_directory.files.remove(file)
                            self.files.append(file_name, file.size)
                            print(f"Undo: Moved file '{file_name}' from '{destination_directory_name}' back to '{self.name}'.")
                            break
                else:
                    print(f"Undo: Destination directory '{destination_directory_name}' not found.")
            elif operation_type == "delete_file":
                _, file_name = last_operation
                self.create_file(file_name, "")  #create an empty file with the same name to undo deletion
        else:
            print("Nothing to undo.")
            
        
