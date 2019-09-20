from django.test import TestCase


class TestDemo(TestCase):

    def setUp(self):
        """每个测试用例执行之前做操作"""
        self.buyer_id = input("请输入buyer_id: ")

    def test_my_Test(self):
        resp = self.client.get("/api/query", {"buyer_id": self.buyer_id})
        json_data = resp.data.decode()
        self.assertEqual(json_data.get("code"), 200)
        self.assertContains(json_data, "OK")
