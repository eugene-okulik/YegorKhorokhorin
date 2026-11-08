import requests
import allure

from test_api_yegorkhorokhorin.endpoints.endpoint import Endpoint


class CreateObject(Endpoint):
    @allure.step('Create new object')
    def create_new_object(self, body):
        self.response = requests.post(
            self.url,
            json=body,
            headers=self.headers
        )
        self.response_json = self.response.json()
        return self.response_json['id']
