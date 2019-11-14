from django.test import TestCase


class TestDemo(TestCase):

    def setUp(self):
        """每个测试用例执行之前做操作"""
        self.buyer_id = "99"

    def test_my_Test(self):
        resp = self.client.get("/api/query", {"buyer_id": self.buyer_id})
        self.assertEqual(resp.status_code, 200)
        json_data = resp.json()
        self.assertEqual(json_data.get("code"), 200)
