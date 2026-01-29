from locust import HttpUser, task, between

class MyEventsUser(HttpUser):
    # Reduced wait time → better load generation
    wait_time = between(0.5, 1)

    def on_start(self):
        # Set user once instead of repeating query construction
        self.user = "locust_user"

    @task
    def view_my_events(self):
        with self.client.get(
            "/my-events",
            params={"user": self.user},
            name="/my-events",
            catch_response=True
        ) as response:
            if response.status_code != 200:
                response.failure(f"Failed with status {response.status_code}")
