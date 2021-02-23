import requests


def get_todos_positive():
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    if response.status_code == 200:
        return response.json()
    else:
        return None


def get_todos_none():
    response = requests.get("https://random_url")
    if response.status_code == 404:
        return response.json()
    else:
        return None


def create_todos():
    title = 'text'
    completed = 'where_created_elem_on_jsonplaceholder'
    payload = {'title': title, 'completed': completed, 'userId': 1}
    response = requests.post("https://jsonplaceholder.typicode.com/todos", json=payload)
    if response.status_code == 201:
        return response.json()
    else:
        return None
