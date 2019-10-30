import time

from django.conf import settings
from django.test import TestCase


class TestDemo(TestCase):

    def setUp(self):
        """每个测试用例执行之前做操作"""
        self.mobile = "18773993654"
        self.password = "123456"

    def test_my_Test(self):
        resp = self.client.post("/api/login", {"mobile": self.mobile, "password": self.password})

        json_data = resp.json()
        print(json_data)
        self.assertEqual(json_data.get("code"), 200)
        self.assertContains(json_data, "OK")
