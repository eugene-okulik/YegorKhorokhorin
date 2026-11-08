import requests
import allure

from test_api_yegorkhorokhorin.endpoints.endpoint import Endpoint


class DeleteObject(Endpoint):
    @allure.step('Delete new object')
    def delete_new_object(self, object_id):
        self.response = requests.delete(
            f'{self.url}/{object_id}'
        )
