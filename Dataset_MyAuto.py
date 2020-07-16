import numpy as np
import pandas as pd
import os
import random
from random import seed
from PIL import Image

class Dataset_MyAuto:

    def __init__(self, data_path: str, data_info_path: str):
        self.data_path = data_path
        self.data_info_path = data_info_path
        self.__load_all_data__()
    

    def __load_all_data__(self):
        self.data_info = pd.read_csv(self.data_info_path)

    def get_train_and_test_data_ids(self, percent = 0.8, random_seed = None):
        if(random_seed != None):
            seed(random_seed)
            np.random.seed(random_seed)
        
        id_list = self.data_info.sample(frac=1)["ID"]
        train_list = id_list.head(int(len(id_list)*(percent)))
        test_list = id_list.iloc[len(train_list):]

        return train_list, test_list
        
    def get_picture_from_id(self, car_id: int):
        car_dir_path = os.path.join(self.data_path, str(car_id))
        if os.path.exists(car_dir_path):
            img_path = os.path.join(car_dir_path, "1.jpg")
            img_array = np.array(Image.open(img_path))
            return img_array
            return None
        else:
            return None

if __name__ == "__main__":
    print("--- testing Dataset_MyAuto class ---")
    dataset = Dataset_MyAuto("../myauto_project_data/images", "../myauto_project_data/characteristics.csv")
    train_ids, test_ids = dataset.get_train_and_test_data_ids(percent=0.0001)
    print("got train of",len(train_ids), "and test of", len(test_ids))
    print(train_ids.head)
    print(test_ids.head)
    newList = []
    for id in train_ids:
        newList.append(dataset.get_picture_from_id(id))
    print(len(newList))
    print("--- testing ended successfully ---")