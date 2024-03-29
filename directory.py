from linkedList import LinkedList
from queue_1 import Queue

class Directory:
    def __init__(self, name):
        self.name = name
        self.files = LinkedList()
        self.subdirectories = []
        self.file_queue = Queue()  #initialize file_queue for each directory

    #method to create a file
    def create_file(self, name, size):
         # add files to linkedList File 
        self.files.append(name, size)  
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
            
        
