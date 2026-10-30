from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Tasks

class TaskApiTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="Alice", password="pass12345")
        self.other = User.objects.create_user(username="Bob", password="pass12345")

    def test_guest_cannot_list_tasks(self):
        response = self.client.get("/api/tasks/")
        self.assertEqual(response.status_code, 403)

    def test_guest_send_post(self):
        response = self.client.post("/api/tasks/", {"name": "Buy Whiskey"}, format="json")
        self.assertEqual(response.status_code, 403)

    def test_user_add_task(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post("/api/tasks/", {"name": "Buy Whiskey"}, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Tasks.objects.filter(owner=self.user).count(), 1)

    def test_user_send_empty_name(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post("/api/tasks/", {"name": ""}, format="json")
        self.assertEqual(response.status_code, 400)

    def test_user_enter_other_task(self):
        task = Tasks.objects.create(name="Buy Whiskey", owner=self.other)
        self.client.force_authenticate(user=self.user)
        response = self.client.get(f"/api/tasks/{task.id}/")
        self.assertEqual(response.status_code, 404)

    def test_delete_task(self):
        task = Tasks.objects.create(name="Buy Whiskey", owner= self.user)
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(f"/api/tasks/{task.id}/")
        self.assertEqual(response.status_code, 204)
        response = self.client.get(f"/api/tasks/{task.id}/")
        self.assertEqual(response.status_code, 404)






