import requests
import allure

from test_api_yegorkhorokhorin.endpoints.endpoint import Endpoint


class PutObject(Endpoint):
    @allure.step('Update object with put')
    def put_object(self, object_id, body):
        self.response = requests.put(f'{self.url}/{object_id}',
                                     json=body,
                                     headers=self.headers)
        self.response_json = self.response.json()
