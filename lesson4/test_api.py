import pytest

TODOS_MAX = 200


# positive/negative тесты для Getting a resource
@pytest.mark.parametrize('todos_id', [1, 100, TODOS_MAX])
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


def test_list_num_positive(session, base_url):
    resp = session.get(url=f'{base_url}')
    assert len(resp.json()) == 200


# positive тесты для Creating a resource
def test_create_positive(session, base_url):
    title = 'text'
    body = 'where_created_elem_on_jsonplaceholder'
    payload = {'title': title, 'body': body, 'userId': 1}
    resp = session.post(url=base_url, json=payload)

    assert resp.status_code == 201


def test_create_content_positive(session, base_url):
    title = 'text'
    body = 'where_created_elem_on_jsonplaceholder'
    payload = {'title': title, 'body': body, 'userId': 1}
    resp = session.post(url=base_url, json=payload)
    json_resp = resp.json()

    assert json_resp['id'] == TODOS_MAX + 1
    assert json_resp['userId'] == 1
    assert json_resp['title'] == title
    assert json_resp['body'] == body
    assert len(json_resp) == 4


# positive/negative тесты для Updating a resource with PUT
def test_update_positive(session, base_url):
    todos_id = 100
    title = 'poem'
    body = 'u_luckomoria_dub_zeleniy'
    payload = {'title': title, 'body': body, 'id': todos_id, 'userId': 1}
    resp = session.put(url=f'{base_url}/{todos_id}', json=payload)

    assert resp.status_code == 200


def test_update_content_positive(session, base_url):
    todos_id = 100
    title = 'poem'
    body = 'u_luckomoria_dub_zeleniy'
    payload = {'title': title, 'body': body, 'id': todos_id, 'userId': 1}
    resp = session.put(url=f'{base_url}/{todos_id}', json=payload)
    json_resp = resp.json()

    assert json_resp['title'] == title
    assert json_resp['body'] == body
    assert len(json_resp) == 4


def test_update_url_negative(session, base_url):
    todos_id = 100
    title = 'poem'
    body = 'u_luckomoria_dub_zeleniy'
    payload = {'title': title, 'body': body, 'id': todos_id, 'userId': 1}
    resp = session.put(url=f'{base_url}/{todos_id}/abra_cadabra', json=payload)

    assert resp.status_code == 404


def test_update_url_id_negative(session, base_url):
    todos_id = 100
    title = 'poem'
    body = 'u_luckomoria_dub_zeleniy'
    payload = {'title': title, 'body': body, 'id': todos_id, 'userId': 1}
    resp = session.put(url=f'{base_url}/{todos_id + 500000}', json=payload)

    assert resp.status_code == 500


# positive тесты для Updating a resource with PATCH
def test_update_positive_patch(session, base_url):
    todos_id = 100
    title = 'poema'
    payload = {'title': title, 'id': todos_id, 'userId': 1}
    resp = session.patch(url=f'{base_url}/{todos_id}', json=payload)

    assert resp.status_code == 200


def test_update_positive_patch_no_body(session, base_url):
    todos_id = 100
    title = 'poema'
    payload = {'title': title, 'id': todos_id, 'userId': 1}
    resp = session.patch(url=f'{base_url}/{todos_id}', json=payload)
    json_resp = resp.json()

    assert json_resp['title'] == 'poema'
    assert json_resp['userId'] == 1
    assert json_resp['id'] == 100
    assert not json_resp['completed']
    assert len(json_resp) == 4


# positive тесты для Deleting a resource
@pytest.mark.parametrize('todos_id', [1, 100, TODOS_MAX])
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
def test_filtering_title_positive(session, base_url):
    title = 'et porro tempora'
    todos_filter_title = 'title={}'.format(title)
    resp = session.get(url=f'{base_url}/?{todos_filter_title}')
    json_resp = resp.json()

    assert resp.status_code == 200
    assert json_resp[0]['title'] == 'et porro tempora'
    assert json_resp[0]['userId'] == 1
    assert json_resp[0]['id'] == 4
    assert json_resp[0]['completed']


@pytest.mark.parametrize('filter', ['userId', 'id', 'title', 'completed'])
def test_filtering_negative(session, base_url, filter):
    value = ['abra_kadabra']
    todos_filter = '{}={}'.format(filter, value)
    resp = session.get(url=f'{base_url}/?{todos_filter}')
    json_resp = resp.json()

    assert resp.status_code == 200
    assert json_resp == []
