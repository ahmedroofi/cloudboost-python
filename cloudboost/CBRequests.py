import json
import requests


class CBRequests(object):

    headers = {"Content-type": "application/json"}

    def post_request(self, url, data):
        data = json.dumps(data)
        response = requests.post(url, data=data, headers=self.headers)
        return response

    def put_request(self, url, data):
        data = json.dumps(data)
        response = requests.put(url, data=data, headers=self.headers)
        return response
