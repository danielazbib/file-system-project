class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    #adds new file to linked list data structure
    def append(self, name, size):
        new_file = File(name, size)
        if not self.head:
            self.head = new_file
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_file
    #display contents of linked list
    def display(self):
        current = self.head
        while current:
            print(f"File: {current.name}, Size: {current.size}")
            current = current.next

class Directory:
    def __init__(self, name) -> None:
        self.name = name
        self.files = [] #initilize files as a list
        self.subdirectories = [] #initialize subdirectories as a list

    #method to create a file
    def create_file(self, name, size):
        name = File(name, size)
        #append new file to directory files list
        self.files.append(name)                  
    
    #method to display contents
    def display_content(self, files):
        for element in files:
            print(element)

    #method for creating subdirectories
    def create_subdirectory(self, name):
        subdirectory = Directory(name)
        self.subdirectories.append(subdirectory)

    #method to delete a file
    def delete_file(self, name):
        #find file by name

        #removes file from files list
        pass

def main():
    root_directory = Directory("root")
    
    command = input("Enter a command:")
    while True:
        #parse through command to set off specific conditional to deliver function

        if command == "mkdir":
            root_directory.create_subdirectory()
        elif command == "file":
            root_directory.create_file()

if __name__ == "__main__":
    main()