import requests
import allure

from test_api_yegorkhorokhorin.endpoints.endpoint import Endpoint


class GetObject(Endpoint):
    @allure.step('Get object')
    def get_object(self, object_id):
        self.response = requests.get(
            f'{self.url}/{object_id}'
        )

        self.response_json = None

        if self.response.status_code == 200:
            self.response_json = self.response.json(
            )
