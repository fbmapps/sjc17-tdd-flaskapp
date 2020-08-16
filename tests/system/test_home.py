"""
Simplify Testing Import
"""
import json
from tests.system.base_data import BaseTest


class HomeTest(BaseTest):
    def test_home_page(self):
        with self.app() as client:
            resp = client.get("/")
            self.assertEqual(resp.status_code, 200)
            self.assertEqual(json.loads(resp.get_data()), {"message": "Hello, world!"})
