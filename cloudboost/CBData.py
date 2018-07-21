from CBUrls import CBUrls
from CBRequests import CBRequests


class CBData(object):

    def __init__(self, key, app_id, url):
        self.key = key
        self.url = CBUrls(url, app_id)
        self.api = CBRequests()

    def save(self, tablename, data):
        post_data = {
            "key": self.key,
            "document": self.set_save_data(tablename, data),
        }
        response = self.api.put_request(self.url.get_table_url(tablename),
                                        post_data)
        return response

    def find(self, tablename, query_param):
        data = self.set_query(query_param)
        response = self.api.post_request(self.url.get_table_find_url(tablename),
                                         data)
        return response

    def count(self, tablename, query_param):
        data = self.set_query(query_param)
        response = self.api.post_request(self.url.get_table_count_url(tablename),
                                         data)
        return response

    def delete(self, tablename, object):
        data = {
            "key": self.key,
            "document": object,
            "method": "DELETE"
        }
        response = self.api.put_request(self.url.get_table_url(tablename), data)
        return response

    def set_query(self, query_param):
        sort = {}
        select = {}
        query = {"$includeList": [], "$include": []}
        query.update(query_param)
        data = {
            "key": self.key,
            "sort": sort,
            "select": select,
            "query": query
        }

        return data

    def set_save_data(self, tablename, data):
        mod_list = ["createdAt", "updatedAt", "ACL", "expires"] + list(data)
        default_data = {"_type": "custom",
                        "expires": None,
                        "_modifiedColumns": mod_list,
                        "_tableName": tablename,
                        "ACL": {
                            "write": {
                                "allow": {
                                 "role": [],
                                 "user": ["all"]
                                },
                                "deny": {
                                    "role": [],
                                    "user": []
                                }
                            },
                            "read": {
                                "allow": {
                                    "role": [],
                                    "user": ["all"]
                                },
                                "deny": {
                                    "role": [],
                                    "user": []
                                }
                            }
                        },
                        "_isModified": True
                        }
        default_data.update(data)
        return default_data
