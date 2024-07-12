from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import CustomUser, Todo
from django.utils import timezone
from datetime import timedelta

class TodoTests(APITestCase):

    def setUp(self):
        self.admin_user = CustomUser.objects.create_user(username='admin', password='adminpassword', role='admin')
        self.user = CustomUser.objects.create_user(username='user', password='userpassword', role='user')
        self.todo_data = {
            'title': 'Test Todo',
            'description': 'Test Description',
            'expires_at': timezone.now() + timedelta(days=28),
            'updated_at': timezone.now(),
        }
        self.admin_token = self.get_token('admin', 'adminpassword')
        self.user_token = self.get_token('user', 'userpassword')

    def get_token(self, username, password):
        response = self.client.post(reverse('token_obtain_pair'), {'username': username, 'password': password})
        return response.data['access']

    def test_create_todo_as_user(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.user_token)
        response = self.client.post(reverse('todos-list'), self.todo_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_todo_as_admin(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.admin_token)
        response = self.client.post(reverse('todos-list'), self.todo_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_todos(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.user_token)
        response = self.client.get(reverse('todos-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_todo_as_admin(self):
        todo = Todo.objects.create(**self.todo_data, owner=self.admin_user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.admin_token)
        response = self.client.put(reverse('todos-detail', kwargs={'pk': todo.id}), {'title': 'Updated Title', 'description': 'Updated Description'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_todo_as_admin(self):
        todo = Todo.objects.create(**self.todo_data, owner=self.admin_user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.admin_token)
        response = self.client.delete(reverse('todos-detail', kwargs={'pk': todo.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
