import datetime as dt
import requests

Base_url="http://api.openweathermap.org/data/2.5/weather?"
Api_key="54389b9edba86b0987c7ea3bb6ae2e66"

city="Londen"

url= Base_url + "appid=" + Api_key + "&q=" + city

response=requests.get(url).json()

print(response)

# ----------------------------------------------------------------------------------


# import requests
# import argparse

# # Replace 'YOUR_API_KEY' with your actual FatSecret API key
# API_KEY = '9694a554f23f436c8a85f0da4aee0396'
# BASE_URL = 'https://platform.fatsecret.com/rest/server.api'

# def search_food(dish_name):
#     params = {
#         'method': 'foods.search',
#         'search_expression': dish_name,
#         'format': 'json',
#         'oauth_consumer_key':"6d1d2fbadac1428daf975ed76335cd74",
#     }
#     response = requests.get(BASE_URL, params=params)
#     response.raise_for_status()
#     return response.json()

# def get_food_nutrition(food_id):
#     params = {
#         'method': 'food.get',
#         'food_id': food_id,
#         'format': 'json',
#         'oauth_consumer_key': API_KEY,
#     }
#     response = requests.get(BASE_URL, params=params)
#     response.raise_for_status()
#     return response.json()

# def main():


#     dish_name=input("Enter the dish name")

#     # parser = argparse.ArgumentParser(description="Food Recipe and Nutrition Details CLI")
#     # parser.add_argument('dish_name', type=str, help='Name of the dish to search for recipes')
#     # parser.add_argument('--nutrition', action='store_true', help='Display nutrition details')
    
#     # args = parser.parse_args()
#     # dish_name = args.dish_name
#     # show_nutrition = args.nutrition

#     # search_results = search_food(dish_name)
#     # if 'foods' in search_results and 'food' in search_results['foods']:
#     #     for food in search_results['foods']['food']:
#     #         print(f"Recipe: {food['food_name']}")
#     #         print(f"Description: {food.get('food_description', 'No description available')}")
#     #         if show_nutrition:
#     #             food_id = food['food_id']
#     #             nutrition_details = get_food_nutrition(food_id)
#     #             print("Nutrition Details:")
#     #             print(nutrition_details)
#     #         print("-" * 40)
#     # else:
#     #     print("No recipes found for the given dish name.")

# if __name__ == "__main__":
#     main()

# ________________________________________________________________________________________


# # 6d1d2fbadac1428daf975ed76335cd74   secreate   
# #  9694a554f23f436c8a85f0da4aee0396  id



# ------------------------------------------------------------------------------



# # import requests

# # # Example API endpoint URL
# # url = "https://platform.fatsecret.com/docs/v2/recipe_types.get"

# # # API key
# # api_key = "a4b8b71e20ae48e8b2682839f3c573ac"

# # # Parameters (this is an example, adjust according to the actual API documentation)
# # params = {
# #     "method": "recipe.get",
# #     "recipe_id": "12345",  # Replace with a valid recipe ID
# #     "format": "json"
# # }

# # # Headers
# # headers = {
# #     "Authorization": f"Bearer {api_key}",
# #     "Content-Type": "application/json"
# # }

# # # Making the GET request
# # response = requests.get(url, headers=headers, params=params)

# # # Checking the response status
# # if response.status_code == 200:
# #     print("Response content:", response.content)  # Print the raw response content
# #     try:
# #         data = response.json()
# #         print(data)
# #     except requests.exceptions.JSONDecodeError:
# #         print("Failed to decode JSON response")
# # else:
# #     print(f"Failed to retrieve data: {response.status_code}")
