from lesson33.get_todos import get_todos_positive, get_todos_none, create_todos
from unittest import mock
import pytest

TODOS_MAX = 200


@pytest.mark.parametrize('todos_id, expected_result',
                         [(1, {'userId': 1, 'id': 1, 'title': 'deleus aut autem', 'completed': False}),
                          (TODOS_MAX, {"userId": 10, "id": 200, "title": "ipsam aperiam voluptates qui",
                                       "completed": False})])
@mock.patch("lesson33.get_todos.requests.get")
def test_get_id_positive(mock_requests_get, todos_id, expected_result):
    mock_requests_get.return_value = mock.Mock(name='mock response',
                                               **{'status_code': 200, 'json.return_value':
                                                   {'userId': 1, 'id': todos_id, 'title': 'deleus aut autem',
                                                    'completed': False}})

    assert get_todos_positive()['id'] == expected_result['id']
    mock_requests_get.assert_called_once()


@pytest.mark.parametrize('todos_id, expected_result', [(-1, {}), (0, {}), (TODOS_MAX + 1, {})])
@mock.patch("lesson33.get_todos.requests.get")
def test_get_id_negative(mock_requests_get, todos_id, expected_result):
    mock_requests_get.return_value = mock.Mock(name='mock response', **{'status_code': 404, 'json.return_value': {}})

    assert len(get_todos_none()) == len(expected_result) == 0
    mock_requests_get.assert_called_once()


@mock.patch("lesson33.get_todos.requests.post")
def test_create_content_positive(mock_requests_post):
    mock_requests_post.return_value = mock.Mock(name='mock response', **{'status_code': 201,
                                                                         'json.return_value': {'userId': 1,
                                                                                               'id': TODOS_MAX + 1,
                                                                                               'title': 'text',
                                                                                               'completed': 'true'}})

    assert create_todos()['id'] == TODOS_MAX + 1
    assert create_todos()['userId'] == 1
    assert create_todos()['title'] == 'text'
    assert create_todos()['completed'] == 'true'
    assert len(create_todos()) == 4
