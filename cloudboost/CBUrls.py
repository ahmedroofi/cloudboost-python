class CBUrls(object):

    def __init__(self, url, app_id):
        self.base_url = url
        self.app_id = app_id

    def get_signup_url(self):
        return self.base_url + "user/{}/{}".format(self.app_id, "signup")

    def get_table_url(self, tablename):
        return self.base_url + "data/{}/{}".format(self.app_id, tablename)

    def get_table_find_url(self, tablename):
        return self.base_url + "data/{}/{}/{}".format(self.app_id, tablename,
                                                      "find")

    def get_table_count_url(self, tablename):
        return self.base_url + "data/{}/{}/{}".format(self.app_id, tablename,
                                                      "count")
