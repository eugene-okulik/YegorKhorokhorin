import requests


def post_an_object():
    body = {
        "name": "yegor",
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
    return response.json()['id']


def put_an_object(object_id):
    body = {
        "name": "Edward",
        "data": {"color": "black", "size": "small"}
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'http://objapi.course.qa-practice.com/object/{object_id}',
        json=body,
        headers=headers
    )
    assert response.status_code == 200, 'Status code is incorrect'
    print(response.status_code)
    response_body = response.json()
    assert response_body["name"] == "Edward"
    print(response_body)


def patch_an_object(object_id):
    body = {
        "name": "Eduard"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'http://objapi.course.qa-practice.com/object/{object_id}',
        json=body,
        headers=headers
    )
    assert response.status_code == 200, 'Status code is incorrect'
    print(response.status_code)
    response_body = response.json()
    assert response_body["name"] == "Eduard"
    print(response_body)


def one_object(object_id):
    response = requests.get(f'http://objapi.course.qa-practice.com/object/{object_id}')
    assert response.status_code == 200, 'Status code is incorrect'
    print(response.status_code)
    response_body = response.json()
    assert int(response_body['id']) == object_id
    print(response_body)


def clear(object_id):
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{object_id}')
    assert response.status_code == 200, 'Status code is incorrect'
    print(response.status_code, 'Объект удален')


def check_object_deleted(object_id):
    response = requests.get(
        f'http://objapi.course.qa-practice.com/object/{object_id}'
    )

    assert response.status_code == 404, 'Status code is incorrect'
    print(response.status_code, 'Объект не найден')


object_id = post_an_object()
one_object(object_id)
put_an_object(object_id)
one_object(object_id)
patch_an_object(object_id)
one_object(object_id)
clear(object_id)
check_object_deleted(object_id)
