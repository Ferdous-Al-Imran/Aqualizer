from django.test import TestCase
from .models import User,ParameterList,ValueEntry,ParameterIdeals


class CreateUser(TestCase):
	def setUp(self):
		User.objects.create(username="Nazrul Islam",password="password1")
		User.objects.create(username="Anjan Bashak",password="password2")
		# User.objects.create(username="Nazrul Islam",password="password3")


	def test_user_is_created(self):
		user1=User.objects.get(username="Nazrul Islam")
		self.assertEqual(user1.username,"Nazrul Islam")

	
	def test_password_matches(self):
		user1=User.objects.get(username="Nazrul Islam")
		self.assertEqual(user1.password,"password1")













