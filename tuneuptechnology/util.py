import json


class Util():
    @staticmethod
    def pretty_print(data):
        """Pretty print JSON"""
        print(json.dumps(data, indent=4))
