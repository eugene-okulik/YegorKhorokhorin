import pytest

from test_api_yegorkhorokhorin.endpoints.create_object import CreateObject
from test_api_yegorkhorokhorin.endpoints.get_object import GetObject
from test_api_yegorkhorokhorin.endpoints.put_object import PutObject
from test_api_yegorkhorokhorin.endpoints.patch_object import PatchObject
from test_api_yegorkhorokhorin.endpoints.delete_object import DeleteObject


@pytest.fixture
def create_object():
    return CreateObject()


@pytest.fixture
def created_object(create_object, delete_object):
    body = {
        'name': 'Object for testing',
        'data': {
            'color': 'black',
            'size': 'medium'
        }
    }

    object_id = create_object.create_new_object(body)
    create_object.check_status_code(200)

    yield object_id

    delete_object.delete_new_object(object_id)


@pytest.fixture
def get_object():
    return GetObject()


@pytest.fixture
def put_object():
    return PutObject()


@pytest.fixture
def patch_object():
    return PatchObject()


@pytest.fixture
def object_for_delete(create_object):
    body = {
        'name': 'Object for deletion',
        'data': {
            'color': 'black',
            'size': 'medium'
        }
    }

    object_id = create_object.create_new_object(body)
    create_object.check_status_code(200)

    return object_id


@pytest.fixture
def delete_object():
    return DeleteObject()
