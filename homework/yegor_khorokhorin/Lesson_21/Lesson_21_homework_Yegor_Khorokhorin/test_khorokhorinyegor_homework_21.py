import requests
import pytest
import allure


@allure.feature('Objects')
@allure.story('Creating of new object')
@allure.title('Создание нового объекта')
@allure.description('Просто создаем разные 3 объекта, проверяем статус код')
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


@allure.feature('Objects')
@allure.story('Editing of new object by put method')
@pytest.mark.critical
def test_put_an_object(post_an_object,
                       start_testing_completed, before_testing_after):
    with allure.step('Информация об изменение объекта'):
        body = {
            "name": "Edward",
            "data": {"color": "black", "size": "small"}
        }
        headers = {'Content-Type': 'application/json'}
    with allure.step('Выполнение метода put'):
        response = requests.put(
            f'http://objapi.course.qa-practice.com/object/{post_an_object}',
            json=body,
            headers=headers
        )
    with allure.step('Проверка статус кода'):
        assert response.status_code == 200, 'Status code is incorrect'
    print(response.status_code)
    response_body = response.json()
    assert response_body["name"] == "Edward"
    print(response_body)


@allure.feature('Objects')
@allure.story('Editing of new object by patch method')
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


@allure.feature('Objects')
@allure.story('Getting of new object')
def test_get_an_object_by_id(post_an_object_for_test_get_an_object_by_id,
                             start_testing_completed, before_testing_after):
    response = requests.get(f'http://objapi.course.qa-practice.com/object/'
                            f'{post_an_object_for_test_get_an_object_by_id}')
    assert response.status_code == 200, 'Status code is incorrect'
    print(response.status_code)
    response_body = response.json()
    assert (int(response_body['id'])
            == post_an_object_for_test_get_an_object_by_id)
    print(response_body)


@allure.feature('Objects')
@allure.story('Deleting of new object')
def test_delete_an_object(post_an_object_for_test_deleting,
                          start_testing_completed, before_testing_after):
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/'
                               f'{post_an_object_for_test_deleting}')
    assert response.status_code == 200, 'Status code is incorrect'
    print(response.status_code, 'Объект удален')
