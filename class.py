class Person:

    def __init__(self, weight: float, height: float, age:int) -> None:
        self.weight = weight
        self.height = height
        self.age = age

    def get_user_goal(self) -> None:
        goal_list = ["gain weight", "maintain weight", "lose weight", "gain muscle", "manage stress"]

        print("These are some fitness goals you may consider")
        for goal in goal_list:
            print(goal)

    def calculate_BMI(self) -> float:
        self.BMI = self.weight/self.height*self.height

        return self.BMI


if __name__ == "__main__":
    Jack = Person(145.5,17.54,2)
    Jack.get_user_goal()
    print(Jack.calculate_BMI())