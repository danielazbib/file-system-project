from directory import Directory

def main():
    #allow user to establish their own root_directory
    root_directory_name = input("Enter the name of the root directory: ")
    root_directory = Directory(root_directory_name)

    while True:
        print("\nAvailable commands:")
        print("1. create_file <name> <size>")
        print("2. create_subdirectory <name>")
        print("3. move_file <file_name> <destination_directory>")
        print("4. display_contents")
        print("5. delete_file <name>")
        print("6. undo_last_operation")
        print("7. rename_file <old_name> <new_name>")
        print("8. search_file <name>")
        print("9. exit")

        #splits user input to store every input as a string in the 'command' array
        command = input("Enter a command: ").strip().split()
        if command[0] == "create_file" and len(command) == 3:  #also makes sure that the user input has three words because the create_file method takes 2 
            root_directory.create_file(command[1], command[2])#passes arguments to method by accesing the command array's position
        elif command[0] == "create_subdirectory" and len(command) == 2:
            root_directory.create_subdirectory(command[1])
        elif command[0] == "move_file" and len(command) == 3:
            root_directory.move_file(command[1], command[2])
        elif command[0] == "display_contents":
            root_directory.display_contents()
        elif command[0] == "delete_file" and len(command) == 2:
            root_directory.delete_file(command[1])
        elif command[0] == "undo_last_operation":
            root_directory.undo_last_operation()
        elif command[0] == "rename_file" and len(command) == 3:
            root_directory.rename_file(command[1], command[2])
        elif command[0] == "search_file" and len(command) == 2:
            result = root_directory.search_file(command[1])
            if result:
                print(f"File '{command[1]}' found.")
            else:
                print(f"File '{command[1]}' not found.")
        elif command[0] == "exit":
            print("Exiting...")
            break
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()