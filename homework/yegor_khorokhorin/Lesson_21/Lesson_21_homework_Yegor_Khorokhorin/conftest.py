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
