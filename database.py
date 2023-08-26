import sqlite3

class UserDatabase:
    
    def __init__(self):

        self.get_file_name()
 
        # create file it file does not exist
        self.connection = sqlite3.connect(self.user_file)
        self.cursor = self.connection.cursor()

    def get_file_name(self):
        try:
            self.file = input("Please specify file name to store your data")
            if not isinstance(self.file, str):
                raise ValueError("Please specify file name in a string format")
        except ValueError as e:
            print("Error:", e)

        self.user_file = self.file + '.db'

        return user_file


    # def create_table(self):
    #     self.cursor.

tanis = UserDatabase()

