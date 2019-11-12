from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):
    def on_start(self):
        """ ok, we do NOT have a session """
        with self.client.get("/", catch_response=True, name='not set') as response:
            #print(response.content)
            if response.status_code != 401:
                response.failure("Got wrong response")
            else:
                response.success()
        self.start_session()

    def start_session(self):
        with self.client.put("/", catch_response=True) as response:
            if response.status_code != 201:
                response.failure("Got wrong response")

    @task(1)
    def index(self):
        with self.client.get("/", catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Got wrong response")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000