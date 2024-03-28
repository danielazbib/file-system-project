class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.next = None

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

    def display(self):
        current = self.head
        while current:
            print(f"File: {current.name}, Size: {current.size}")
            current = current.next

class Directory:
    def __init__(self, name):
        self.name = name
        self.files = LinkedList()
        self.subdirectories = []
    #method to create a file
    def create_file(self, name, size):
         # add files to linkedList File 
        self.files.append(name, size)  
    #method to display contents
    def display_contents(self):
        print("Files in", self.name + ":")
        self.files.display()
        print("Subdirectories:")
        for subdir in self.subdirectories:
            print(subdir.name)

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
        print("\nAvailable commands:")
        print("1. create_file <name> <size>")
        print("2. create_subdirectory <name>")
        print("3. display_contents")
        print("4. delete_file <name>")
        print("5. exit")

        #splits user input to store every input as a string in the 'command' arrar
        command = input("Enter a command: ").strip().split()

        #compares the position of word in command to specific file
        if command[0] == "create_file" and len(command) == 3: #also makes sure that the user input has three words because the create_file method takes 2 inputs
            root_directory.create_file(command[1], command[2]) #passes arguments to method by accesing the command array's position
        elif command[0] == "create_subdirectory" and len(command) == 2:
            root_directory.create_subdirectory(command[1])
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