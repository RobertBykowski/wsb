import json
import os


# loading test data from the test_data.json file
def get_test_data():
    with open(os.path.join('data_test', 'test_data.json')) as f:
        test_data = json.load(f)
        return test_data
