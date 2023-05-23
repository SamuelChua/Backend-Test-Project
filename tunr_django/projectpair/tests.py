from django.test import TestCase
from django.contrib.auth.models import User
from .models import ProjectPair

class ProjectPairTestCase(TestCase):
    def test_project_pair_creation(self):
        # Create a user
        user = User.objects.create(username='samchua')

        # Create a project pair associated with the user
        project_pair = ProjectPair.objects.create(user=user, email='samuelchua2001@gmail.com')

        # Assert that the project pair is correctly created and associated with the user
        self.assertEqual(project_pair.user, user)
