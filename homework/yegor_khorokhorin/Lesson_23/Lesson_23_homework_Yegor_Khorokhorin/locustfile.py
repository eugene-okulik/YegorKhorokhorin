import random
from locust import HttpUser, task, between


class ObjApi(HttpUser):
    wait_time = between(1, 3)

    @task(1)
    def get_all_objects(self):
        self.client.get('/object')

    @task(3)
    def get_one_object(self):
        self.client.get(
            f'/object/{random.choice([1, 277, 292, 300])}',
            name='/object/[random_id]'
        )

    @task(1)
    def object_lifecycle(self):
        post_response = self.client.post(
            '/object',
            json={
                'name': 'yy',
                'data': {
                    'color': 'white',
                    'size': 'big'
                }
            }
        )

        if post_response.status_code != 200:
            return

        object_id = post_response.json()['id']

        try:
            put_response = self.client.put(
                f'/object/{object_id}',
                json={
                    'name': 'Updated object',
                    'data': {
                        'color': 'black',
                        'size': 'small'
                    }
                },
                name='/object/[id]'
            )

            if put_response.status_code != 200:
                return

            get_response = self.client.get(
                f'/object/{object_id}',
                name='/object/[id]'
            )

            assert get_response.status_code == 200
            assert get_response.json()['name'] == 'Updated object'

        finally:
            self.client.delete(
                f'/object/{object_id}',
                name='/object/[id]'
            )
