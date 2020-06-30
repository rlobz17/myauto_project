import numpy as np
import pandas as pd
import os

class Dataset_MyAuto:

    def __init__(self):
        pass

    # get fully changed dataset of train data
    def get_train_data(self, train_data_path):
        pass

    # get fully changed dataset of test data
    def get_test_data(self, test_data_path):
        pass

    # get fully changed picture from train data
    def get_train_data_picture(self, train_data_picture_path):
        pass

    # get fully changed picture from test data   
    def get_test_data_picture(self, test_data_picture_path):
        pass

    # get picture path from train data
    def get_train_data_picture_path(self, train_data_path):
        pass

    # get picture path from test data   
    def get_test_data_picture_path(self, test_data_path):
        pass

    # get pathes of auto with id=id pictures from train or test data
    def get_pictures_for_auto(self, data_path, auto_id):
        auto_directory = os.path.join(data_path, auto_id)
        if(os.path.exists(auto_directory)):
            return_list = []
            path, dirs, files = next(os.walk(auto_directory))
            for file_path in  files:
                return_list.append(os.path.join(auto_directory, file_path))
            return return_list
        else:
            return None



if __name__ == "__main__":
    print("--- testing Dataset_MyAuto class ---")
    dataset = Dataset_MyAuto()
    print(dataset.get_pictures_for_auto("../myauto_project_data/data/images", '1042'))
    print("--- testing ended successfully ---")