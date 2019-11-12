import time
import unittest

from django.db import connection
from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient


class TestDemo(TestCase):
    token = None

    def setUp(self):
        """每个测试用例执行之前做操作"""
        self.factory = APIClient()
        self.mobile = "18773993654"
        self.password = "012356"
        self.factory.credentials(HTTP_AUTHORIZATION=self.token)
        print(self.token)

    def tearDown(self):
        """每个测试用例执行之后做操作"""
        self.token = getattr(TestDemo, "token")

    # @unittest.skip("I don't want to run this case.")
    def test_user_aregister(self):
        resp = self.client.post("/api/register", {"mobile": self.mobile, "password": self.password})
        self.assertEqual(resp.status_code, 200)
        json_data = resp.json()
        print(json_data)
        self.assertEqual(json_data.get("code"), 200, msg="注册失败： %s" % json_data.get("msg"))
        TestDemo.token = json_data.get("data").get("token")

    @unittest.skip("I don't want to run this case.")
    def test_user_login(self):
        resp = self.client.post("/api/login", {"mobile": self.mobile, "password": self.password})
        self.assertEqual(resp.status_code, 200)
        json_data = resp.json()
        # print(json_data)
        self.assertEqual(json_data.get("code"), 200, msg="服务器异常未正常返回： %s" % json_data.get("msg"))

    def test_user_info(self):
        """用户信息"""
        resp = self.factory.get("/api/user_info")
        self.assertEqual(resp.status_code, 200)
        json_data = resp.json()
        # print(json_data)
        self.assertEqual(json_data.get("code"), 200, msg=json_data.get("msg"))
