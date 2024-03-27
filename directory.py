from file import File
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
    

    #method for creating subdirectories
    def create_subdirectory(self, name):
        subdirectory = Directory(name)
        self.subdirectories.append(subdirectory)

    #method to delete a file
    def delete_file(self, name):
        #find file by name

        #removes file from files list
        self.files.remove(name)
    
    #method to display contents
    def display_content(self, files):
        for element in files:
            print(element)
        
