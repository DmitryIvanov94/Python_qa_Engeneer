import json
from jsonschema import validate, ValidationError


def assert_valid_schema(data, schema_file):
    with open(schema_file) as f:
        schema = json.load(f)
    try:
        validate(instance=data, schema=schema)
        return validate(instance=data, schema=schema)
    except:
        return ValidationError


# Getting a resource
def test_get_todo_positive(session, base_url):
    resp = session.get(url=f'{base_url}/1')
    assert_valid_schema(resp.json(), 'lesson4/schemas/todo_schema.json')


def test_get_todo_content_positive(session, base_url):
    resp = session.get(url=f'{base_url}/1')
    json_resp = resp.json()

    assert json_resp['title'] == 'delectus aut autem'
    assert json_resp['userId'] == 1
    assert json_resp['id'] == 1
    assert not json_resp['completed']


def test_get_novalid_todo_negative(session, base_url):
    resp = session.get(url=f'{base_url}/1')
    assert assert_valid_schema(resp.json(), 'lesson4/schemas/todo_novalid_schema.json') == ValidationError


def test_get_nonetype_todo_negative(session, base_url):
    resp = session.get(url=f'{base_url}/1')
    assert assert_valid_schema(resp.json(), 'lesson4/schemas/todo_nonetype_schema.json') == ValidationError


# Listing all resources
def test_list_todos_positive(session, base_url):
    resp = session.get(url=base_url)
    assert_valid_schema(resp.json(), 'lesson4/schemas/todos_schema.json')


def test_list_todos_content_positive(session, base_url):
    resp = session.get(url=base_url)
    assert len(resp.json()) == 200


def test_list_novalid_todos_negative(session, base_url):
    resp = session.get(url=base_url)
    assert assert_valid_schema(resp.json(), 'lesson4/schemas/todos_novalid_schema.json') == ValidationError


def test_list_noref_todos_negative(session, base_url):
    resp = session.get(url=base_url)
    assert assert_valid_schema(resp.json(), 'lesson4/schemas/todos_noref_schema.json') == ValidationError
