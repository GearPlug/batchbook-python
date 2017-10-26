import requests
from urllib.parse import urlparse, urlencode
from batchbook import exception
import json

class Client(object):

    def __init__(self, api_key, account_name):
        self._api_key = api_key
        _name = self._get_name_url(account_name)
        self._base_url = "https://{0}.batchbook.com/api/v1".format(_name)
        try:
            self.get_contacts()
        except:
            raise exception.InvalidCredential("Invalid APIKEY or ACCOUNT NAME")

    def _get_name_url(self, url):
        _name = urlparse(url)
        if _name.scheme:
            return _name.netloc.split(".")[0]
        else:
            return url

    def _get(self, endpoint, params=None):
        return self._request('GET', endpoint, params=params)

    def _delete(self, endpoint, params=None, identifier=None):
        return self._request('DELETE', endpoint, params=params, identifier=identifier)

    def _post(self, endpoint, params=None, data=None):
        return self._request('POST', endpoint, data=data)

    def _request(self, method, endpoint, params=None, data=None, **kwargs):
        parameters = {'auth_token' : self._api_key}
        if params is not None:
            for k,v in params.items():
                parameters[k] = v
        url = '{0}/{1}{2}'.format(self._base_url, endpoint, '.json')
        response = requests.request(method, url, params=parameters, data=data)
        r = response.__dict__
        print(response.status_code)
        if response.status_code in [403, 404, 500]:
            if response.status_code == 404:
                if 'identifier' in kwargs:
                    if kwargs['identifier'] == 'contact':
                        raise exception.Not_Found("Contact not found")
                else:
                    raise exception.Not_Found("Not Found")
            if 'reason' in r:
                raise Exception(r['reason'])
            else:
                raise Exception('Unexpected error.')
        return response

    def get_contacts(self, since=None, until=None):
        """
        Args:
        Returns:
            A json.
        """
        if since and until:
            raise exception.Bad_Request("You should provide SINCE or UNTIL parameters, two values are not allowed")
        else:
            if since or until:
                if since:
                    data ={'updated_since' : since}
                if until:
                    data ={'updated_before' : until}
                return self._get(endpoint='people', data=data).json()
            else:
                return self._get(endpoint='people').json()

    def get_contact(self, contact_id):
        """
        Args: contact_id: String, Unique ID for the contact
        Returns:
            A json.
        """
        return self._get(endpoint='people/{0}'.format(contact_id), identifier='contact').json()

    def delete_contact(self, contact_id):
        """
        Args: contact_id: String, Unique ID for the contact
        Returns:
            A status_code.
        """
        return self._delete(endpoint='people/{0}'.format(contact_id), identifier='contact').status_code

    def create_contact(self):
        """
        Args: contact_id: String, Unique ID for the contact
        Returns:
            A status_code.
        """
        data = {'first_name': 'Rodrigo'}
        return self._post(endpoint='people/', data=data)

