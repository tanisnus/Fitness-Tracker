class Person:

    def __init__(self, weight: float, height: float, age:int) -> None:
        self.weight = weight
        self.height = height
        self.age = age
        self.gender = ""
        self.BMR = 0

    def get_user_data() -> None:
        TuesdayAug8_2023 = {
            "Breakfast": ["Rice", "Sausage", "Milk", "Banana"], 
            "Lunch": ["Spagetti Suace", "Spagetti Noodle""Cashew Nut"],
            "Dinner": ["Rice", "Sausage", "Orange"]
            
            }
        
    def get_workout_data(self) -> None:
        muscle_target = ["Chest", "Back", "Bicep", "Tricep", "Shoulder", "Legs", "Abs"]
        print("These are main muscle target groups")
        for item in muscle_target:
            print(item)



    def get_user_goal(self) -> None:
        goal_list = ["gain weight", "maintain weight", "lose weight", "gain muscle", "manage stress"]

        print("These are some fitness goals you may consider")
        for goal in goal_list:
            print(goal)

    def calculate_BMI(self) -> float:
        self.BMI = self.weight/self.height*self.height

        return self.BMI
    
    def calculate_carolie(self) -> float:

        # case 1: Adult Male
        if self.age >= 18 and self.gender == "Male":
            # adult male: 66 + (6.3 x body weight in lb) + (12.9 x height in inches) – (6.8 x age in years) = BMR
            self.BMR = 66 +(6.3 * self.weight) + (12.9 * self.height) - (6.8 * self.age)

        # case 2: Adult Female
        elif self.age >= 18 and self.gender == "Female":
            # adult female: 655 + (4.3 x weight in lb) + (4.7 x height in inches) – (4.7 x age in years) = BMR
            self.BMR = 655 + (4.3 * self.weight) + (4.7 * self.height) - (4.7 * self.age)

    
    # idea: create calender to keep track what they a user exercise


if __name__ == "__main__":
    Jack = Person(145.5,17.54,2)
    Jack.get_user_goal()
    Jack.get_workout_data()