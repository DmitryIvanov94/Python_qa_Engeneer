import pytest

TODOS_MAX = 200


# positive/negative тесты для Getting a resource
@pytest.mark.parametrize('todos_id', [1, TODOS_MAX])
def test_get_id_positive(session, base_url, todos_id):
    resp = session.get(url=f'{base_url}/{todos_id}')

    assert resp.status_code == 200
    assert resp.json()['id'] == todos_id


@pytest.mark.parametrize('todos_id', [-1, 0, TODOS_MAX + 1])
def test_get_id_negative(session, base_url, todos_id):
    resp = session.get(url=f'{base_url}/{todos_id}')

    assert resp.status_code == 404
    assert len(resp.json()) == 0


# positive тесты для Listing all resources
def test_list_positive(session, base_url):
    resp = session.get(url=f'{base_url}')
    assert resp.status_code == 200
    assert len(resp.json()) == 200


# positive тесты для Creating a resource
def test_create_content_positive(session, base_url):
    title = 'text'
    completed = 'where_created_elem_on_jsonplaceholder'
    payload = {'title': title, 'completed': completed, 'userId': 1}
    resp = session.post(url=base_url, json=payload)
    json_resp = resp.json()

    assert resp.status_code == 201
    assert json_resp['id'] == TODOS_MAX + 1
    assert json_resp['userId'] == 1
    assert json_resp['title'] == title
    assert json_resp['completed'] == completed
    assert len(json_resp) == 4


# positive/negative тесты для Updating a resource with PUT
def test_update_content_positive(session, base_url):
    todos_id = 100
    title = 'poem'
    completed = 'u_luckomoria_dub_zeleniy'
    payload = {'title': title, 'completed': completed,
               'id': todos_id, 'userId': 1}
    resp = session.put(url=f'{base_url}/{todos_id}', json=payload)
    json_resp = resp.json()

    assert resp.status_code == 200
    assert json_resp['title'] == title
    assert json_resp['completed'] == completed
    assert len(json_resp) == 4


@pytest.mark.parametrize('update_id', ['/abra_cadabra', TODOS_MAX + 500000])
def test_update_url_id_negative(session, base_url, update_id):
    todos_id = 100
    title = 'poem'
    body = 'u_luckomoria_dub_zeleniy'
    payload = {'title': title, 'body': body, 'id': todos_id, 'userId': 1}
    resp = session.put(url=f'{base_url}/{todos_id, update_id}', json=payload)

    if update_id == '/abra_cadabra':
        assert resp.status_code == 404
    if update_id == TODOS_MAX + 500000:
        assert resp.status_code == 500


# positive тесты для Updating a resource with PATCH
def test_update_positive_patch_no_body(session, base_url):
    todos_id = 100
    title = 'poema'
    payload = {'title': title, 'id': todos_id, 'userId': 1}
    resp = session.patch(url=f'{base_url}/{todos_id}', json=payload)
    json_resp = resp.json()

    assert resp.status_code == 200
    assert json_resp['title'] == 'poema'
    assert json_resp['userId'] == 1
    assert json_resp['id'] == 100
    assert json_resp['completed'] is False
    assert len(json_resp) == 4


# positive тесты для Deleting a resource
@pytest.mark.parametrize('todos_id', [1, TODOS_MAX])
def test_delete_positive(session, base_url, todos_id):
    resp = session.delete(url=f'{base_url}/todos_id')

    assert resp.status_code == 200
    assert not resp.json()


def test_delete_check_content_positive(session, base_url):
    resp = session.delete(url=f'{base_url}/100')
    resp_1 = session.get(url=f'{base_url}/99')
    resp_2 = session.get(url=f'{base_url}/101')

    assert len(resp.json()) == 0
    assert len(resp_1.json()) > 0
    assert len(resp_2.json()) > 0


# positive/negative тесты для Filtering resources
@pytest.mark.parametrize('filter, value',
                         [('title', 'et porro tempora'), ('userId', 10),
                          ('id', 5), ('completed', 'false')])
def test_filtering_title_positive(session, base_url, filter, value):
    todos_filter = '{}={}'.format(filter, value)
    resp = session.get(url=f'{base_url}/?{todos_filter}')
    json_resp = resp.json()

    assert resp.status_code == 200

    if filter == 'title':
        assert json_resp[0]['title'] == 'et porro tempora'
        assert json_resp[0]['userId'] == 1
        assert json_resp[0]['id'] == 4
        assert json_resp[0]['completed']
    if filter == 'userId':
        assert len(json_resp) == 20
    if filter == 'id':
        assert json_resp[0]['title'] \
               == 'laboriosam mollitia et enim ' \
                  'quasi adipisci quia provident illum'
        assert json_resp[0]['userId'] == 1
        assert json_resp[0]['id'] == 5
        assert json_resp[0]['completed'] is False
    if filter == 'completed':
        assert len(json_resp) == 110


@pytest.mark.parametrize('filter, value',
                         [('userId', 500), ('id', TODOS_MAX + 1),
                          ('title', 'novalid_value'),
                          ('completed', 'novalid_value')])
def test_filtering_negative(session, base_url, filter, value):
    todos_filter = '{}={}'.format(filter, value)
    resp = session.get(url=f'{base_url}/?{todos_filter}')
    json_resp = resp.json()

    assert resp.status_code == 200
    assert json_resp == []
