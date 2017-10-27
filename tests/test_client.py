import os
from unittest import TestCase
from batchbook.client import Client



class BatchbookTestCases(TestCase):
    def setUp(self):
        self.api_key = os.environ.get('apikey')
        self.account_name = os.environ.get('account_name')
        self.client = Client(api_key=self.api_key, account_name=self.account_name)

    def test_name_url(self):
        """
        Self.account_name, is just the name form url
        :return:
        """
        _url = "https://{0}.batchbook.com/api/v1".format(self.account_name)
        result = self.client._get_name_url(_url)
        self.assertEqual(self.account_name, result)

    def test_get_contacts(self):
        """
        Self.account_name, is just the name form url
        :return:
        """
        _url = "https://{0}.batchbook.com/api/v1".format(self.account_name)
        result = self.client._get_name_url(_url)
        self.assertEqual(self.account_name, result)