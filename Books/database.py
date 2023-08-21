import requests
def books_data(add):

    url = f"https://www.googleapis.com/books/v1/volumes?q={add}+inauthor:keyes&key=AIzaSyCLf1J-zhHycgx9PvwNX5lOAAXrcYiiNt0"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.json()


from django.contrib.auth import get_user_model

users = get_user_model().objects.all()

print(users)