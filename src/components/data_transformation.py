import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from src import logger
from pathlib import Path
from src.utils.common import save_bin
from src.entity.config_entity import DataTransformationConfig
from src.configuration.config import ConfigurationManager

class DataTransformation:
    def __init__(self,config:DataTransformationConfig):
        self.config=config

    def data_transformation(self,data):
        logger.info("data transformation object start creating \n")
        column=data.columns
        column_save=column.drop("quality")

        p1=Pipeline(steps=[
        ('standard_scaler',StandardScaler())
        ])

        ct=ColumnTransformer(transformers=[
        ('std_scaler',p1,column_save)
        ])
        logger.info("data Transformation object creation completed ")
        return ct
    

    def train_test_split(self):
        data=pd.read_csv(self.config.data_path)

        logger.info("data are splitted into train and test")

        train_data,test_data=train_test_split(data,test_size=0.2,random_state=5)
        logger.info(f"train data shape {train_data.shape}")
        logger.info(f"test data shape {test_data.shape}")

        logger.info(f"train data column : {list(train_data.columns)}\n")
        logger.info(f"test data column {list(test_data.columns)}\n")

        logger.info("train,test data saved to path")
        train_data.to_csv(os.path.join(self.config.root_dir,"train.csv"),index=False)
        test_data.to_csv(os.path.join(self.config.root_dir,"test.csv"),index=False)

        logger.info("preprocessor object")
        preproc_obj=self.data_transformation(train_data)

        TARGET_COLUMN='quality'
        logger.info("splitting target column from train data")
        train_df=train_data.drop(TARGET_COLUMN,axis=1)
        target_train=train_data[TARGET_COLUMN]
        logger.info("Target column splitted from train data")

        logger.info("splitting target column from test data")
        test_df=test_data.drop(TARGET_COLUMN,axis=1)
        target_test=test_data[TARGET_COLUMN]
        logger.info("target column splitted from test data")

        logger.info("Transform data")

        train_trans=preproc_obj.fit_transform(train_df)
        test_trans=preproc_obj.transform(test_df)

        train_arr=np.c_[train_trans,np.array(target_train)]
        test_arr=np.c_[test_trans,np.array(target_test)]

        #train_arr.to_csv(os.path.join(self.config.root_dir,"train_arr.csv"))
        #test_arr.to_csv(os.path.join(self.config.root_dir,'test_arr.csv'))

        logger.info("save preprocessor object")
        path=Path(self.config.pkl_path)
        save_bin(preproc_obj,path)
        logger.info("Returned train array , test array:")
        logger.info(f"train array shape {train_arr.shape}")
        logger.info(f"test array shape {test_arr.shape}")
        return train_arr,test_arr
    

if __name__ == "__main__":
    pass