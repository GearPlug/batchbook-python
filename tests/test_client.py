import os
import time
from unittest import TestCase
from batchbook.client import Client



class BatchbookTestCases(TestCase):
    def setUp(self):
        self.api_key = os.environ.get('apikey')
        self.account_name = os.environ.get('account_name')
        self.my_contact = {
                            "person":
                              {
                              "prefix":"Nuevo",
                              "first_name":"Nuevo",
                              "middle_name":"Nuevo",
                              "last_name":"Nuevo",
                              "emails":[
                                {
                                  "address":"nuevo@gmail.com",
                                  "label":"work",
                                  "primary": True
                                }],
                               }
                            }
        self.client = Client(api_key=self.api_key, account_name=self.account_name)

    def test_name_url(self):
        _url = "https://{0}.batchbook.com/api/v1".format(self.account_name)
        result = self.client._get_name_url(_url)
        self.assertEqual(self.account_name, result)

    def test_get_contacts(self):
        result_create = self.client.create_contact(data=self.my_contact)
        time.sleep(10)
        result = self.client.get_contacts()
        _id = ""
        for r in result:
            if (r['id'] == result_create['id']):
                _id = r['id']
        self.assertEqual(_id, result_create['id'])
        self.client.delete_contact(contact_id=result_create['id'])

    def test_get_contact(self):
        result_create = self.client.create_contact(data=self.my_contact)
        result = self.client.get_contact(result_create['id'])
        self.assertEqual(result['id'], result_create['id'])
        self.client.delete_contact(contact_id=result_create['id'])

    def test_delete_contact(self):
        result_create = self.client.create_contact(data=self.my_contact)
        self.client.delete_contact(contact_id=result_create['id'])
        try:
            self.client.get_contact(result_create['id'])
            result = False
        except:
            result = True
        self.assertTrue(result)


