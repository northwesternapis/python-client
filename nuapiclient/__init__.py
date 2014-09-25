import json
import urllib
import urllib2

BASE_URL = 'api.asg.northwestern.edu'

ENDPOINTS = {
    'terms': [],
    'schools': [],
    'subjects': [],
    'courses': ['details'],
    'instructors': [],
    'buildings': [],
    'rooms': ['details'],
}


class APIRequestError(Exception):
    """An exception raised when the API responds with an error."""
    def __init__(self, response):
        self.message = response.get('error')

    def __str__(self):
        return self.message


def make_endpoint_function(endpoint):
    """
    Given an endpoint name, creates a function that calls
    the endpoint and parses the response into a native datatype.
    """
    def call_endpoint(self, **params):
        if params:
            params.update({'key': self.key})
        else:
            params = {'key': self.key}
        data = urllib.urlencode(params)
        req = urllib2.Request(self.base_url + endpoint + '?' + data)
        response = urllib2.urlopen(req)
        result = json.loads(response.read())
        if 'error' in result:
            raise APIRequestError(result)
        return result
    return call_endpoint


def add_endpoint_methods(cls):
    """A decorator that adds a method to a class for each API endpoint."""
    for key in ENDPOINTS:
        setattr(cls, key, make_endpoint_function('/%s' % key))
        for option in ENDPOINTS[key]:
            method_name = '%s_%s' % (key, option)
            setattr(cls, method_name,
                make_endpoint_function('/%s/%s' % (key, option)))
    return cls


@add_endpoint_methods
class NorthwesternAPIClient(object):
    def __init__(self, key, **kwargs):
        self.key = key
        if 'secure' in kwargs and kwargs['secure']:
            self.base_url = 'https://' + BASE_URL
        else:
            self.base_url = 'http://' + BASE_URL
