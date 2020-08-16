from unittest import TestCase
from app import app


class BaseTest(TestCase):
    """
    BASE TEST Class for all System Tests
    """

    def setUp(self):
        self.app = app.test_client
