from src.configuration.config import ConfigurationManager
from src.components.data_transformation import DataTransformation
from src import logger


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        with open("data/data_validation/status.txt","r") as f:
            status=f.read().split(" ")[-1]
        if status=="True":
            obj1=ConfigurationManager()
            data_trans=obj1.data_transformation_config()
            obj=DataTransformation(data_trans)
            train_arr,test_arr=obj.train_test_split()
            return train_arr,test_arr
        