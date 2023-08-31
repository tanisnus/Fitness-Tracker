import sqlite3

class UserDatabase:
    
    def __init__(self):

        self.user_file = self.get_file_name()
 
        # create file it file does not exist
        self.connection = sqlite3.connect(self.user_file)
        self.cursor = self.connection.cursor()


        self.create_table()
        self.insert_to_table()
        self.output_data()

        self.connection.commit()
        self.connection.close()


    def create_table(self):
        self.cursor.execute("""CREATE TABLE user (
            user_name text
            email text    
        )
                        
        """)

    def insert_to_table(self):
        self.cursor.execute(""" INSERT INTO user VALUES ('Tanis') 
                            
        """)
        print("insert function")

    def output_data(self):
        self.cursor.execute("SELECT * FROM user")
        print(self.cursor.fetchall())




    def get_file_name(self) -> str:
        """
            The function asks user for file name that represents their database
        """

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
                if ".db" in user_file:
                    raise ValueError("Please don't include '.db'. The system automatically add the file type after name of your file")

                invalid_file_name = False

            except Exception as error:
                print("Invalid File Name:", error)

        user_file:str = user_file + '.db'

        return user_file
    




    # def create_table(self):
    #     self.cursor.

tanis = UserDatabase()

