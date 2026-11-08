import allure


class Endpoint:
    url = 'http://objapi.course.qa-practice.com/object'
    headers = {'Content-type': 'application/json'}
    response = None
    response_json = None

    @allure.step('Check status code')
    def check_status_code(self, expected_code):
        assert self.response.status_code == expected_code, (
            f'Expected {expected_code}, got {self.response.status_code}'
        )

    @allure.step('Check name of object')
    def check_response_name(self, expected_name):
        assert self.response_json['name'] == expected_name, (
            f'Expected {expected_name}, got {self.response_json["name"]}'
        )
