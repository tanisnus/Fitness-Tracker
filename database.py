import sqlite3

class UserDatabase:
    
    def __init__(self):

        self.user_file = self.get_file_name()
 
        # create file it file does not exist
        self.connection = sqlite3.connect(self.user_file)
        self.cursor = self.connection.cursor()

    def get_file_name(self):

        invalid_file_name = True
        invalid_char = "/\:*?<>|"
        while(invalid_file_name):
            try:
                user_file = input("Please specify file name to store your data: ")
                if user_file.isspace():
                    raise ValueError("File name cannot contain any spaces")
                if " " in user_file:
                    raise ValueError("File name cannot contain any spaces")
                for char in user_file:
                    if char in invalid_char:
                        raise ValueError("File name cannot contain any these characters /\:*?<>|")

                invalid_file_name = False

            except Exception as error:
                print("Error has occured:", error)

        user_file:str = user_file + '.db'

        return user_file


    # def create_table(self):
    #     self.cursor.

tanis = UserDatabase()

