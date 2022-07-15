from locust import HttpUser, between, task

class WebsiteUser(HttpUser):
    wait_time = between(5, 15)
    
    @task
    def index(self):
        self.client.get("/")


# from locust import HttpLocust, TaskSet, between

# def index(l):
#     l.client.get("/")

# class UserBehavior(TaskSet):
#     tasks = {index: 1}

# class WebsiteUser(HttpLocust):
#     task_set = UserBehavior
#     wait_time = between(5.0, 9.0)