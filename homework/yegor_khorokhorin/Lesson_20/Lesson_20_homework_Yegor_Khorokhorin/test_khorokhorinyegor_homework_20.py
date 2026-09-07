import requests
import pytest


@pytest.fixture(scope='session')
def start_testing_completed():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.fixture()
def before_testing_after():
    print('before test')
    yield
    print('after test')


@pytest.mark.parametrize('body', [
    {"name": "egor", "data": {"color": "white", "size": "big"}},
    {"name": "Eduard", "data": {"color": "black", "size": "small"}},
    {"name": "Edward", "data": {"color": "red", "size": "medium"}}
])
def test_post_of_new_object(body,
                            start_testing_completed, before_testing_after):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=body,
        headers=headers
    )
    assert response.status_code == 200, 'Status code is incorrect'
    print(response.status_code)
    print(response.json())
    print(response.json()['id'])


@pytest.fixture()
def post_an_object():
    body = {
        "name": "egor",
        "data": {"color": "white", "size": "big"}
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=body,
        headers=headers
    )
    assert response.status_code == 200, 'Status code is incorrect'
    print(response.status_code)
    print(response.json())
    object_id = response.json()['id']
    yield object_id
    response = requests.get(f'http://objapi.course.qa-practice.com/object/'
                            f'{object_id}')
    assert response.status_code == 200, 'Status code is incorrect'
    print(response.status_code)
    response_body = response.json()
    assert int(response_body['id']) == object_id
    print(response_body)
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/'
                               f'{object_id}')
    assert response.status_code == 200, 'Status code is incorrect'
    print(response.status_code, "Объект удален")
    response = requests.get(
        f'http://objapi.course.qa-practice.com/object/{object_id}'
    )
    assert response.status_code == 404, 'Status code is incorrect'
    print(response.status_code, 'Объект не найден')


@pytest.mark.critical
def test_put_an_object(post_an_object,
                       start_testing_completed, before_testing_after):
    body = {
        "name": "Edward",
        "data": {"color": "black", "size": "small"}
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'http://objapi.course.qa-practice.com/object/{post_an_object}',
        json=body,
        headers=headers
    )
    assert response.status_code == 200, 'Status code is incorrect'
    print(response.status_code)
    response_body = response.json()
    assert response_body["name"] == "Edward"
    print(response_body)


@pytest.mark.medium
def test_patch_an_object(post_an_object,
                         start_testing_completed, before_testing_after):
    body = {
        "name": "Eduard"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'http://objapi.course.qa-practice.com/object/{post_an_object}',
        json=body,
        headers=headers
    )
    assert response.status_code == 200, 'Status code is incorrect'
    print(response.status_code)
    response_body = response.json()
    assert response_body["name"] == "Eduard"
    print(response_body)


@pytest.fixture()
def post_an_object_for_test_get_an_object_by_id():
    body = {
        "name": "egor",
        "data": {"color": "white", "size": "big"}
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=body,
        headers=headers
    )
    assert response.status_code == 200, 'Status code is incorrect'
    print(response.status_code)
    print(response.json())
    object_id = response.json()['id']
    yield object_id
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/'
                               f'{object_id}')
    assert response.status_code == 200, 'Status code is incorrect'
    print(response.status_code, "Объект удален")
    response = requests.get(
        f'http://objapi.course.qa-practice.com/object/{object_id}'
    )
    assert response.status_code == 404, 'Status code is incorrect'
    print(response.status_code, 'Объект не найден')


def test_get_an_object_by_id(post_an_object_for_test_get_an_object_by_id,
                             start_testing_completed, before_testing_after):
    response = requests.get(f'http://objapi.course.qa-practice.com/object/'
                            f'{post_an_object_for_test_get_an_object_by_id}')
    assert response.status_code == 200, 'Status code is incorrect'
    print(response.status_code)
    response_body = response.json()
    assert (int(response_body['id']) ==
            post_an_object_for_test_get_an_object_by_id)
    print(response_body)


@pytest.fixture()
def post_an_object_for_test_deleting():
    body = {
        "name": "egor",
        "data": {"color": "white", "size": "big"}
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=body,
        headers=headers
    )
    assert response.status_code == 200, 'Status code is incorrect'
    print(response.status_code)
    print(response.json())
    object_id = response.json()['id']
    yield object_id
    response = requests.get(
        f'http://objapi.course.qa-practice.com/object/'
        f'{object_id}'
    )
    assert response.status_code == 404, 'Status code is incorrect'
    print(response.status_code, 'Объект не найден')


def test_delete_an_object(post_an_object_for_test_deleting,
                          start_testing_completed, before_testing_after):
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/'
                               f'{post_an_object_for_test_deleting}')
    assert response.status_code == 200, 'Status code is incorrect'
    print(response.status_code, 'Объект удален')
