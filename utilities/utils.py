import json
import os


class Utils:
    def get_test_data(self):
        with open(os.path.join('data_test', 'test_data.json')) as f:
            test_data = json.load(f)
            return test_data

