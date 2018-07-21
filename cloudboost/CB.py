from CBData import CBData
from CBUser import CBUser


class CB(object):

    def __init__(self, url, app_id, key):
        self.url = url
        self.key = key
        self.app_id = app_id
        self.user = CBUser(self.key, self.app_id, self.url)
        self.data = CBData(self.key, self.app_id, self.url)
