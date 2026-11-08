import pytest

TEST_BODY = [
        {"name": "egor", "data": {"color": "white", "size": "big"}},
        {"name": "Eduard", "data": {"color": "black", "size": "small"}},
        {"name": "Edward", "data": {"color": "red", "size": "medium"}}]

TEST_BODY_FOR_PUT = [
    {'name': 'Object for put',
        'data': {
            'color': 'white',
            'size': 'small'}}
]

TEST_BODY_FOR_PATCH = [
    {
        'name': 'Object after patch'
    }
]


@pytest.mark.parametrize('body', TEST_BODY)
def test_create_object(create_object, body):
    create_object.create_new_object(body)
    create_object.check_status_code(200)
    create_object.check_response_name(body['name'])


def test_get_object(get_object, created_object):
    get_object.get_object(created_object)
    get_object.check_status_code(200)
    get_object.check_response_name('Object for testing')


@pytest.mark.parametrize('body', TEST_BODY_FOR_PUT)
def test_put_object(put_object, body, created_object):
    put_object.put_object(created_object, body)
    put_object.check_status_code(200)
    put_object.check_response_name(body['name'])


@pytest.mark.parametrize('body', TEST_BODY_FOR_PATCH)
def test_patch_object(patch_object, body, created_object):
    patch_object.patch_object(created_object, body)
    patch_object.check_status_code(200)
    patch_object.check_response_name(body['name'])


def test_delete_new_object(delete_object, object_for_delete, get_object):
    delete_object.delete_new_object(object_for_delete)
    delete_object.check_status_code(200)

    get_object.get_object(object_for_delete)
    get_object.check_status_code(404)
