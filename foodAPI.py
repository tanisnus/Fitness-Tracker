import requests


class Nutrition:

    def __init__(self):
        self.api_key = '1IIG2V7czC+Bvh+5asldNw==KffUmBhsNdl36chX'
        self.api_url = 'https://api.calorieninjas.com/v1/nutrition?query='

    def get_food_nutrition(self, query_food_item: str) -> dict:

        self.response = requests.get(self.api_url + query_food_item, headers={'X-Api-Key': self.api_key})

        print(self.response.text)


if __name__ == "__main__":
    chicken = Nutrition()
    chicken.get_food_nutrition('chicken')
