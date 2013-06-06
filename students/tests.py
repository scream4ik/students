from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from models import Group, Students


class StudentsTest(TestCase):
	
	def setUp(self):
		self.client = Client()
		testuser = User.objects.create_user('admin', 'admin@example.com', 'admin')
		testuser.save()
	
	def test_students(self):
		login = self.client.login(username='admin', password='admin')
		self.assertTrue(login)
		response = self.client.get(reverse('group_add'))
		self.assertEqual(response.status_code, 200)
		response = self.client.post(reverse('group_add'), {'name':'New name'})
		self.assertEqual(response.status_code, 302)
		response = self.client.get(reverse('student_add', args=[1]))
		self.assertEqual(response.status_code, 200)
		response = self.client.post(reverse('student_add', args=[1]), {'fio':'Slava Kyrachevsky', 'birthday_month': '6', 'birthday_day': '2', 'birthday_year': '1990', 'student_card': '0004', 'group': '1'})
		self.assertEqual(response.status_code, 302)