import json
from jsonschema import validate, ValidationError


def assert_valid_schema(data, schema_file):
    with open(schema_file) as f:
        schema = json.load(f)
    try:
        validate(instance=data, schema=schema)
        return validate(instance=data, schema=schema)
    except ValidationError:
        return 'Data and schema do not match'


# Getting a resource
def test_get_todo_positive(session, base_url):
    resp = session.get(url=f'{base_url}/1')
    json_resp = resp.json()
    assert_valid_schema(resp.json(), 'lesson4/schemas/todo_schema.json')

    assert json_resp['title'] == 'delectus aut autem'
    assert json_resp['userId'] == 1
    assert json_resp['id'] == 1
    assert not json_resp['completed']


# Listing all resources
def test_list_todos_positive(session, base_url):
    resp = session.get(url=base_url)
    assert_valid_schema(resp.json(), 'lesson4/schemas/todos_schema.json')
    assert len(resp.json()) == 200
